# 2x2-cube-solver-AI
AI 2x2 Rubik's Cube solver project for T-622-ARTI at Reykjavik University

# Authors
Nina Carlson & Emma Shneidman 

## Abstract
This is a program that can solve a 2x2 Rubik's cube using a variety of search methods such as Breadth-First Search, Iterative Deepening Search, Depth-Limited search, and A* search. 
Heuristic: 3D Manhattan distance of the corners and then dividing that value by 4. This is an admissable heuristic. 


## Usage:
sh run.sh <search_method> <scramble_string>

Example:
sh run.sh bfs "F R L"



