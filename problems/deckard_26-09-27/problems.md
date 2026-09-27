# Problems posed by Deckard

**Source: [Paradoxical Puzzles](https://www.youtube.com/watch?v=Ycveax8jHbI)**
---

## [Puzzle 1](https://youtu.be/Ycveax8jHbI)
An paradoxical introductory puzzle with no solutions consisting of only two constraints.

| Constraints | Solution |
| --- | --- |
| The statement below is true. | - |
| The statement above is false. | - |

Implemented in [puzzle_1.py](puzzle_1.py)


## [Puzzle 2](https://youtu.be/Ycveax8jHbI?t=105)
Converting the problem into a puzzle with exactly one correct solution by changing the 2nd constraint.

| Constraints | Solution |
| --- | --- |
| The statement below is true. | F |
| There is exactly one true statement. | F |

Implemented in [puzzle_2.py](puzzle_2.py)


## [Puzzle 3](https://youtu.be/Ycveax8jHbI?t=175)
Expanding the puzzle to include a third statement.

| Constraints | Solution |
| --- | --- |
| 1. Statement 2 is true. | T |
| 2. Statement 3 is false. | T |
| 3. The 3 statements are either all true or all false. | F |

Implemented in [puzzle_3.py](puzzle_3.py)


## [Puzzle 4](https://youtu.be/Ycveax8jHbI?t=282)
Modification of Puzzle 3 that uses patterns spotted to aid in the solving of this new Puzzle.

| Constraints | Solution |
| --- | --- |
| 1. Statement 2 is false. | T |
| 2. Statement 3 is true. | F |
| 3. Statements 1 and 2 are either both true or both false. | F |

Implemented in [puzzle_4.py](puzzle_4.py)


## [Puzzle 5](https://youtu.be/Ycveax8jHbI?t=330)
5 constraint puzzle to illustrate a way of solving these puzzles without checking every possible solution.

| Constraints | Solution |
| --- | --- |
| 1. Statements 3 & 4 are either both tru eor both false. | T |
| 2. Exactly three of the statements are true. | F |
| 3. Statements 1 & 5 have differing parities. | F |
| 4. Over half of the statements are true. | F |
| 5. Statement 3 is false. | T |

Implemented in [puzzle_5.py](puzzle_5.py)


## [Puzzle 6](https://youtu.be/Ycveax8jHbI?t=580)
Another 5 constraint puzzle to handle cases where it is harder to pick out a starting point.

| Constraints | Solution |
| --- | --- |
| 1. Statements 3 & 4 are a different parity. | T |
| 2. Statements 1 & 5 are a different parity. | T |
| 3. Statements 1 & 2 are a same parity. | T |
| 4. Statements 3 & 5 are a same parity. | T |
| 5. Statements 2 & 4 are a different parity. | T |

Implemented in [puzzle_6.py](puzzle_6.py)


## [Puzzle 7](https://youtu.be/Ycveax8jHbI?t=729)
The final puzzle in the video consisting of 10 statements left as an exercise for the viewer.

| Constraints | Solution |
| --- | --- |
| 1.  There are no instances of three rules in a row being all true or all false.  | F |
| 2.  Of the odd numbered statements, either 2 or 3 of them are true.  | F |
| 3.  Exactly 2 of statements 4, 5, 6, and 7 are true.  | F |
| 4.  Statements 3 and 5 are either both true or both false.  | T |
| 5.  Statements 4 and 6 are not both true or both false.  | F |
| 6.  Between statements 3, 8, and 9, only one of them is true  | T |
| 7.  Statements 5 and 6 are not both true or both false.  | T |
| 8.  Statements 1 and 9 are either both true or false.  | T |
| 9.  Statements 1 and 8 are either both true or false.  | F |
| 10. There are ether 4 or 5 true statements in the above 9 statements.  | T |

Implemented in [puzzle_7.py](puzzle_7.py)