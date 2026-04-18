$baseDir = Get-Item .
$excludeBasenames = @('t.py', 'test_monster.py', 'Untitled-1.py')
$extensions = @('.py', '.cpp', '.c++', '.cc', '.cxx')

$files = Get-ChildItem -Recurse -File | Where-Object {
    $relPath = $_.FullName.Replace($baseDir.FullName, "").TrimStart("\")     
    $pathComponents = $relPath.Split("\")
    $extMatch = $extensions -contains $_.Extension
    if (-not $extMatch) { return $false }
    if ($excludeBasenames -contains $_.Name) { return $false }
    if ($_.Name.StartsWith("t.")) { return $false }
    $containsCodeforces = $false
    for($i=0; $i -lt ($pathComponents.Count - 1); $i++){
        if ($pathComponents[$i] -like "*Codeforces*") {
            $containsCodeforces = $true
            break
        }
    }
    return $containsCodeforces
}
$groupedFiles = $files | Sort-Object @{Expression={Split-Path $_.Directory -Leaf}}, Name | Group-Object @{Expression={Split-Path $_.Directory -Leaf}}
$texContent = @"
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{listings}
\usepackage{xcolor}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=mystyle}
\title{Codeforces Problems and Solutions}
\author{Generated Assistant}
\date{\today}
\begin{document}
\maketitle
\tableofcontents
\newpage
"@
foreach ($group in $groupedFiles) {
    $contestName = $group.Name.Replace("_", "\_")
    $texContent += "`n\section{$contestName}`n"
    foreach ($file in $group.Group) {
        $fileName = $file.Name.Replace("_", "\_")
        $texContent += "\subsection{$fileName}`n"
        try {
            $lines = Get-Content $file.FullName -TotalCount 50
            $texContent += "\begin{lstlisting}`n"
            foreach ($line in $lines) { $texContent += $line + "`n" }
            $texContent += "\end{lstlisting}`n"
        } catch { $texContent += "Error reading file content.`n" }
    }
}
$texContent += "\end{document}"
$texContent | Out-File -FilePath "Codeforces_Problems_and_Solutions.tex" -Encoding utf8
$includedCount = $files.Count
$first10Contests = ($groupedFiles | Select-Object -First 10 | ForEach-Object { $_.Name }) -join ", "
Write-Host "INC_COUNT:$includedCount"
Write-Host "FIRST_CONTESTS:$first10Contests"
