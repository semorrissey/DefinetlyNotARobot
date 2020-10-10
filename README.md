# DefinetlyNotARobot
### Group Members
Christopher Guerrette, Oliver Thode, Sean Morrissey

## Instructions
Please run the **Agent.py** file before the Referee is running in a given game.

**Note:**
Our files must be in the same directory as the **referee.py** file.

## Program Info

### Utility Function

Our utility function checks for winning conditions, five pieces in a row, and assigns a maximum or minimum value accordingly.

### Evaluation Function

Our Evaluation function performs checks on the board state for the following placements of pieces:
1. Fours
1. Straight Fours
1. Threes
1. Broken Threes

Each of these states and our winning condition are assigned a value in the order of importance for both the agent and its opponent. This order depends on which state will lead to winning the game.


### Heuristics & Strategies

Our program begins in the middle of the board no matter what. Our Heuristic measures how close a possible move is to five in a row.

We use forward pruning to determine the best possible move to take based on each possible move's value assigned by our heuristic evaluation function. We prune possible spaces that are more than one away from placed pieces.

We implemented a depth limit for the Minimax Algorithm so that we do not exceed the time limit.

We intended to tune our heuristics for our tournament-ready version and implement an opening book or set of starting strategies.

## Results

### Tests

We first ran tests of our program against itself with varying depth limits for the opponent and player versions. We were able to debug with this, finding an ideal depth limit for our program of 3 and optimizing our algorithm so it chooses the best choice faster. It took a bit for us to optimize as when we first began testing, our program was not very smart and took too long to make decisions. Fine-tuning to forward pruning with a heap queue helped dramatically improved the timing, intelligence, and efficiency of our program. We also did unit testing on our evaluation function's ability to find different placements or game states.

### Strengths & Weaknesses
Our strengths include:
- It is efficient at searching the minimax tree for possible moves
- It is good when it moves first
- It is able to pick its own wins

Our weaknesses include:
- Not blocking enemy wins


### Discussion
The heuristics that we chose allow our program to search much faster by choosing only relevant moves, ones that are likely to affect the outcome of the game. Our evaluation function is a good choice because it takes into account what configurations of the board lead to winning threats.