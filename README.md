Conway's Game of Life
======================
[Source](https://bitstorm.org/gameoflife/)  
Python implementation of Conway's Game of Life, a "cellular automaton" that consists of populated and unpopulated cells that survive and die based off of four rules

## Rules
1. Each populated cell that has 0 or 1 neighbors dies in the next generation
1. Each populated cell that has 4 or more neighbors dies in the next generation
1. Each cell with 2 or 3 neighbors survives in the next generation
1. Each unpopulated cell with exactly 3 neighbors becomes populated in the next generation

## Usage
`
./life.py [# of generations] [colony width] [colony height] 
`
