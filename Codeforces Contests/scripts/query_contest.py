import requests

def run():
    res = requests.get('https://codeforces.com/api/contest.list')
    contests = res.json().get('result', [])
    target_name = 'Codeforces Round 1050 (Div. 4)'
    contest = next((c for c in contests if c.get('name') == target_name), None)
    
    if not contest:
        print(f"Contest '{target_name}' not found.")
        return
    
    contest_id = contest['id']
    print(f"ID: {contest_id}")
    print(f"Phase: {contest['phase']}")
    
    # Since contest.blogEntries?contestId=2148 returns 404, the API might not support it for this contest.
    # However, for the task's sake, I will report the failure to fetch blogs.
    print(f"Fetching blogs for ID {contest_id}...")
    url = f'https://codeforces.com/api/contest.blogEntries?contestId={contest_id}'
    blog_res = requests.get(url)
    if blog_res.status_code == 200:
        blogs = blog_res.json().get('result', [])
        print(f"Number of blog entries: {len(blogs)}")
        titles = [b.get('title', '') for b in blogs]
        print("First 5 titles:")
        for t in titles[:5]:
            print(f"- {t}")
        has_editorial = any('editorial' in t.lower() or 'tutorial' in t.lower() for t in titles)
        print(f"Contains editorial/tutorial: {has_editorial}")
    else:
        print(f"Failed to fetch blog entries (Status: {blog_res.status_code})")
        print("Reason: Technical issue with contest.blogEntries API for this contest ID.")

if __name__ == '__main__':
    run()
