# Auditory exercise 4 - Informed search


## Example - Puzzle

A puzzle 3x3 is given, that has fields with numbers from 1 to 8 and an empty field. The empty field is marked with ‘\*’.

![](./../images/puzzle1.png)

The problem question is how to go from an initial puzzle ordering to a goal puzzle ordering, as in:

![](./../images/puzzle2.png)

Actions: the actions possible are moving the empty field:
- **Up**
- **Down**
- **Left**
- **Right**

When defining the actions, it's important to make sure they're possible in the given puzzle. 

We define the state as a string with 9 characters (8 numbers and ‘\*’).
The string is stores the fields starting from the first to the third row, left to right. 
Example: initial puzzle state is “\*32415678”, the goal state is “\*12345678”.


##### Heuristic

1. Number of fields in the wrong spot

2. Manhattan distance to the goal state

To define distance, we need to define a coordinate system
The beginning of the coordinate system is set in the lower left puzzle corner
We define a dictionary for every puzzle field coordinates 
We define a function that computes Manhattan distance for the puzzle. 
This function at input takes two integers, which are the two fields with the numbers that we need to compute distance for

![](./../images/puzzle3.png)


## Problem 1 - Explorer

Implement in Python a state representation about the problem for which, one of the possible initial states is like in the figure below

![](./../images/explorer1.png)

The little man needs to be brought to his home. The man can move on any adjacent field, horizontally or vertically. 
The obstacles 1 and 2 are moving vertically. Each of the obstacles is moving one field in the adequate direction with each movement of the little man.

Obstacle 1 moves downwards initially and Obstacle 2 upwards. Figure 2 gives an example movement of the man and the obstacles. 

![](./../images/explorer1.png) ![](./../images/explorer2.png)


When the obstacle reaches the end of the board, it switches direction and continues to move. 
If an obstacle and the man are on the same field, the man will be destroyed.

For all test examples, the look and size of the board are the same as in the figures. All test cases have the same initial position and movement direction for the obstacles. Each test case has a different starting position of the man and different position of the house. 

The initial code reads the input arguments for each test case. 

The movements need to be defined as follows:
- **Right** - move the man one position right
- **Left** - move the man one position left
- **Up** - move the man one position up
- **Down** - move the man one position down

Your code should have one function call that will print the man movement sequence. The movement sequence is the sequence of moves that will allow the man to reach the position of the house. 

Use informed search. Use manhattan distance as a heuristic function.
