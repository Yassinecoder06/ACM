import html
import os
import re
from collections import defaultdict

import requests

try:
    import cloudscraper
except Exception:
    cloudscraper = None


API_BASE = 'https://codeforces.com/api'
CF_WEB_BASE = 'https://codeforces.com'
OUTPUT_TEX = 'Codeforces_Problems_and_Solutions.tex'
EXTENSIONS = {'.py', '.cpp', '.c++', '.cc', '.cxx'}
EXCLUDE_BASENAMES = {'t.py', 'test_monster.py', 'untitled-1.py'}


def get_web_client():
    if cloudscraper is not None:
        return cloudscraper.create_scraper()
    return requests.Session()


WEB_CLIENT = get_web_client()


def escape_latex(text):
    chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    return ''.join(chars.get(c, c) for c in text)


def normalize_name(text):
    return re.sub(r'[^a-z0-9]+', '', text.lower())


def is_codeforces_relpath(rel_path):
    parts = rel_path.split(os.sep)
    return any('codeforces' in p.lower() for p in parts[:-1])


def extract_problem_index(file_name):
    stem = os.path.splitext(file_name)[0]
    # Matches A_xxx, C_1_xxx, D. xxx, B-xxx
    match = re.match(r'^\s*([A-Z])(?:[._\- ]?(\d+))?', stem)
    if not match:
        return None
    letter, num = match.groups()
    return f'{letter}{num or ""}'


def clean_problem_title(file_name):
    stem = os.path.splitext(file_name)[0]
    stem = stem.replace('_', ' ').strip()
    stem = re.sub(r'\s+', ' ', stem)
    return stem


def scan_problem_files(root_dir):
    problems = []
    for root, _, files in os.walk(root_dir):
        for file_name in files:
            lower_name = file_name.lower()
            ext = os.path.splitext(lower_name)[1]
            if ext not in EXTENSIONS:
                continue
            if lower_name in EXCLUDE_BASENAMES or lower_name.startswith('t.'):
                continue

            file_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(file_path, root_dir)
            if not is_codeforces_relpath(rel_path):
                continue

            index = extract_problem_index(file_name)
            if not index:
                continue

            problems.append(
                {
                    'contest': os.path.basename(root),
                    'file_name': file_name,
                    'index': index,
                    'fallback_title': clean_problem_title(file_name),
                }
            )
    return problems


def api_get_json(path, params=None):
    response = requests.get(f'{API_BASE}/{path}', params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    if data.get('status') != 'OK':
        raise RuntimeError(f'API error for {path}: {data.get("comment", "Unknown")}')
    return data['result']


def get_contest_id_map(contest_names):
    contest_list = api_get_json('contest.list')
    normalized_to_id = {}
    for contest in contest_list:
        normalized_to_id[normalize_name(contest['name'])] = contest['id']

    result = {}
    for name in contest_names:
        key = normalize_name(name)
        if key in normalized_to_id:
            result[name] = normalized_to_id[key]

    return result


def get_problems_for_contest(contest_id):
    result = api_get_json(
        'contest.standings',
        params={'contestId': contest_id, 'from': 1, 'count': 1},
    )
    return result.get('problems', [])


def fetch_editorial_link_from_contest_page(contest_id):
    url = f'{CF_WEB_BASE}/contest/{contest_id}'
    response = WEB_CLIENT.get(url, timeout=30)
    response.raise_for_status()
    page = response.text

    anchors = re.findall(r'(?is)<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', page)
    candidates = []

    for href, anchor_html in anchors:
        text = html_to_text(anchor_html).strip()
        lower_text = text.lower()

        if '/blog/entry/' not in href:
            continue

        if href.startswith('http'):
            abs_url = href
        else:
            abs_url = f'{CF_WEB_BASE}{href}'

        score = 0
        if 'tutorial' in lower_text:
            score += 5
        if 'editorial' in lower_text:
            score += 5
        if 'analysis' in lower_text:
            score += 2

        candidates.append((score, abs_url, text or 'Blog entry'))

    if not candidates:
        return '', ''

    candidates.sort(key=lambda x: x[0], reverse=True)
    best = candidates[0]
    return best[1], best[2]


def html_to_text(fragment):
    text = fragment
    text = re.sub(r'(?i)<br\s*/?>', '\n', text)
    text = re.sub(r'(?i)</p\s*>', '\n\n', text)
    text = re.sub(r'(?i)</li\s*>', '\n', text)
    text = re.sub(r'(?i)</h[1-6]\s*>', '\n', text)
    text = re.sub(r'(?s)<[^>]+>', ' ', text)
    text = html.unescape(text)
    text = text.replace('\r', '\n')
    text = re.sub(r'\n[ \t]+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def fetch_editorial_text(blog_id):
    url = f'{CF_WEB_BASE}/blog/entry/{blog_id}'
    response = WEB_CLIENT.get(url, timeout=30)
    response.raise_for_status()
    page = response.text

    match = re.search(r'(?s)<div class="ttypography">(.*?)</div>\s*</div>', page)
    if not match:
        return ''

    return html_to_text(match.group(1))


def fetch_editorial_text_by_url(editorial_url):
    if not editorial_url:
        return ''

    match = re.search(r'/blog/entry/(\d+)', editorial_url)
    if match:
        try:
            return fetch_editorial_text(int(match.group(1)))
        except Exception:
            return ''

    response = WEB_CLIENT.get(editorial_url, timeout=30)
    response.raise_for_status()
    page = response.text
    match_div = re.search(r'(?s)<div class="ttypography">(.*?)</div>\s*</div>', page)
    if not match_div:
        return ''
    return html_to_text(match_div.group(1))


def extract_problem_section(editorial_text, index, all_indices, contest_id=None, problem_name=''):
    if not editorial_text:
        return ''

    idx = re.escape(index)
    heading_patterns = [
        rf'(?im)^\s*{contest_id if contest_id is not None else ""}\s*{idx}\s*[\-\.:\)]\s*.*$' if contest_id is not None else None,
        rf'(?im)^\s*(?:problem\s*)?{idx}\s*[\.:\-\)]\s*.*$',
        rf'(?im)^\s*(?:problem\s*)?{idx}\s*$',
    ]
    heading_patterns = [p for p in heading_patterns if p]

    start = None
    for pat in heading_patterns:
        m = re.search(pat, editorial_text)
        if m:
            start = m.start()
            break

    if start is None and problem_name:
        name_match = re.search(re.escape(problem_name), editorial_text, flags=re.IGNORECASE)
        if name_match:
            start = max(0, name_match.start() - 120)

    if start is None:
        return ''

    rest = editorial_text[start:]

    next_headers = '|'.join(re.escape(i) for i in all_indices if i != index)
    if next_headers:
        if contest_id is not None:
            next_pat = rf'(?im)^\s*(?:{contest_id})?\s*(?:problem\s*)?(?:{next_headers})\s*[\-\.:\)]\s*.*$'
        else:
            next_pat = rf'(?im)^\s*(?:problem\s*)?(?:{next_headers})\s*[\.:\-\)]\s*.*$'
        m2 = re.search(next_pat, rest)
        segment = rest[:m2.start()] if m2 else rest
    else:
        segment = rest

    lines = [ln.strip() for ln in segment.splitlines() if ln.strip()]
    if not lines:
        return ''

    # Drop likely heading line.
    body_lines = lines[1:] if len(lines) > 1 else lines
    body = ' '.join(body_lines)
    body = re.sub(r'\s+', ' ', body).strip()
    if not body:
        return ''

    # Keep concise: first 2-3 sentences.
    sentences = re.split(r'(?<=[.!?])\s+', body)
    summary = ' '.join(sentences[:3]).strip()
    if len(summary) > 520:
        summary = summary[:517].rstrip() + '...'
    return summary


def infer_fallback_solution(source_text):
    s = source_text.lower()
    if 'bisect' in s or ('mid' in s and 'while' in s):
        return 'Use binary search on the answer with a feasibility check at each midpoint.'
    if 'sort(' in s or 'sorted(' in s:
        return 'Sort values first, then apply a greedy or linear pass to satisfy constraints.'
    if 'prefix' in s or 'accumulate' in s:
        return 'Precompute prefix aggregates and answer each condition/query efficiently.'
    if 'counter' in s or 'defaultdict' in s or 'dict(' in s:
        return 'Count frequencies with a hash map and derive the result from those counts.'
    if 'set(' in s:
        return 'Use set membership checks to validate uniqueness and allowed transitions.'
    if '^' in source_text:
        return 'Use XOR properties (parity and cancellation) to simplify the condition.'
    return 'Use direct case analysis and simulation while maintaining problem invariants.'


def write_latex(root_dir, records):
    lines = [
        r'\documentclass[11pt]{article}',
        r'\usepackage[utf8]{inputenc}',
        r'\usepackage[T1]{fontenc}',
        r'\usepackage[a4paper,margin=1in]{geometry}',
        r'\usepackage[hidelinks]{hyperref}',
        r'\title{Codeforces Editorial-Based Problem Ideas}',
        r'\author{Generated from Codeforces Editorials + Workspace}',
        r'\date{\today}',
        r'\begin{document}',
        r'\maketitle',
        r'\tableofcontents',
        r'\newpage',
    ]

    current_contest = None
    for item in records:
        if item['contest'] != current_contest:
            current_contest = item['contest']
            lines.append(f"\\section{{{escape_latex(current_contest)}}}")
            if item.get('editorial_url'):
                lines.append(
                    f"\\textbf{{Editorial:}} \\href{{{item['editorial_url']}}}{{{escape_latex(item['editorial_title'])}}}"
                )
                lines.append('')

        title = f"{item['index']} - {item['problem_name']}"
        lines.append(f"\\subsection{{{escape_latex(title)}}}")
        lines.append(
            f"\\textbf{{Content:}} {escape_latex(item['content_line'])}\\\\"
        )
        lines.append(
            f"\\textbf{{Solution Idea:}} {escape_latex(item['solution_idea'])}"
        )
        lines.append('')

    lines.append(r'\end{document}')

    out_path = os.path.join(root_dir, OUTPUT_TEX)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    root_dir = os.getcwd()
    problems = scan_problem_files(root_dir)
    problems.sort(key=lambda p: (p['contest'].lower(), p['file_name'].lower()))

    contests = sorted({p['contest'] for p in problems}, key=str.lower)
    contest_to_id = get_contest_id_map(contests)

    grouped = defaultdict(list)
    for p in problems:
        grouped[p['contest']].append(p)

    records = []
    with_editorial_count = 0
    missing_contest_ids = 0

    for contest in sorted(grouped.keys(), key=str.lower):
        contest_id = contest_to_id.get(contest)
        if not contest_id:
            missing_contest_ids += len(grouped[contest])
            for p in sorted(grouped[contest], key=lambda x: x['file_name'].lower()):
                records.append(
                    {
                        'contest': contest,
                        'index': p['index'],
                        'problem_name': p['fallback_title'],
                        'content_line': (
                            f"Problem {p['index']} ({p['fallback_title']}) from {contest}. "
                            'Goal: derive the required output for each testcase under the given constraints.'
                        ),
                        'solution_idea': 'Editorial link not found automatically for this contest; fallback idea inferred from local solution structure.',
                        'editorial_url': '',
                        'editorial_title': '',
                    }
                )
            continue

        try:
            cf_problems = get_problems_for_contest(contest_id)
        except Exception:
            cf_problems = []
        index_to_problem = {x['index']: x for x in cf_problems}
        all_indices = list(index_to_problem.keys())
        if not all_indices:
            all_indices = sorted({x['index'] for x in grouped[contest]})

        editorial_text = ''
        editorial_url = ''
        editorial_title = ''

        try:
            editorial_url, editorial_title = fetch_editorial_link_from_contest_page(contest_id)
        except Exception:
            editorial_url, editorial_title = '', ''

        if editorial_url:
            editorial_text = fetch_editorial_text_by_url(editorial_url)

        for p in sorted(grouped[contest], key=lambda x: x['file_name'].lower()):
            idx = p['index']
            problem_obj = index_to_problem.get(idx, {})
            problem_name = problem_obj.get('name', p['fallback_title'])

            content_line = (
                f'Problem {idx} ({problem_name}) from {contest}. '
                'Goal: derive the required output for each testcase under the given constraints.'
            )

            solution_idea = extract_problem_section(
                editorial_text,
                idx,
                all_indices,
                contest_id=contest_id,
                problem_name=problem_name,
            )
            if solution_idea:
                with_editorial_count += 1
            else:
                file_path = os.path.join(root_dir, contest, p['file_name'])
                source = ''
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        source = f.read()
                except OSError:
                    source = ''
                solution_idea = infer_fallback_solution(source)

            records.append(
                {
                    'contest': contest,
                    'index': idx,
                    'problem_name': problem_name,
                    'content_line': content_line,
                    'solution_idea': solution_idea,
                    'editorial_url': editorial_url,
                    'editorial_title': editorial_title,
                }
            )

    write_latex(root_dir, records)

    print(f'Problems: {len(records)}')
    print(f'Editorial-based summaries found: {with_editorial_count}')
    print(f'Problems with missing contest-id mapping: {missing_contest_ids}')
    print(f'TeX: {os.path.join(root_dir, OUTPUT_TEX)}')


if __name__ == '__main__':
    main()
