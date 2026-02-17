# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed Nov 12 20:44:49 2025)---
python --version
clear
!python --version
python -m pip install --upgrade pip
clear

## ---(Fri Nov 21 08:57:11 2025)---
runfile('C:/Users/UNNI/.spyder-py3/temp.py', wdir='C:/Users/UNNI/.spyder-py3')
conda update spyder
pip install --upgrade pip
pip install --upgrade spyder
pip install --upgrade pip
runfile('C:/Users/UNNI/.spyder-py3/temp.py', wdir='C:/Users/UNNI/.spyder-py3')

## ---(Mon Nov 24 20:09:58 2025)---
runfile('C:/Users/UNNI/.spyder-py3/temp.py', wdir='C:/Users/UNNI/.spyder-py3')

## ---(Fri Nov 28 09:55:27 2025)---
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')
clear
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')

## ---(Fri Dec  5 08:59:40 2025)---
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')

## ---(Tue Dec 23 22:39:51 2025)---
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')

## ---(Wed Dec 24 22:32:35 2025)---
runcell(0, 'E:/python/STMU-AI-LAB/factorial.py')
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')

## ---(Sun Dec 28 16:21:21 2025)---
runfile('E:/python/STMU-AI-LAB/factorial.py', wdir='E:/python/STMU-AI-LAB')

## ---(Fri Jan  2 08:38:00 2026)---
runfile('E:/python/STMU-AI-LAB/mid_lab_paper.py', wdir='E:/python/STMU-AI-LAB')
runcell(0, 'E:/python/STMU-AI-LAB/mid_lab_paper.py')
runfile('E:/python/STMU-AI-LAB/mid_lab_paper.py', wdir='E:/python/STMU-AI-LAB')

## ---(Tue Jan 20 16:57:59 2026)---
runfile('F:/STMU/semester-3/AI-Lab/tic-tac-toe.py', wdir='F:/STMU/semester-3/AI-Lab')

## ---(Fri Feb  6 08:41:49 2026)---
runfile('F:/STMU/semester-3/AI-Lab/untitled0.py', wdir='F:/STMU/semester-3/AI-Lab')
runfile('F:/STMU/semester-3/AI-Lab/final_paper.py', wdir='F:/STMU/semester-3/AI-Lab')
clear

runfile('F:/STMU/semester-3/AI-Lab/final_paper.py', wdir='F:/STMU/semester-3/AI-Lab')



graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 6)],
    'E': [('G', 2)],
    'F': [('G', 4)],
    'G': []
}

heuristics = {
    'A': 7, 'B': 6, 'C': 2,
    'D': 5, 'E': 2, 'F': 1,
    'G': 0
}

def greedy_best_first_search(start, goal):
    visited = []
    frontier = [(heuristics[start], start, [start])]

    while frontier:
        frontier.sort(key=lambda x: x[0])
        h, node, path = frontier.pop(0)

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return visited, path

        for neighbor, cost in graph[node]:
            frontier.append((heuristics[neighbor], neighbor, path + [neighbor]))

    return visited, []

visited_nodes, final_path = greedy_best_first_search('A', 'G')

print("Visited Nodes:", visited_nodes)
print("Path:", final_path)
