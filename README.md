# Logic Puzzle Solver

A simple **brute-force** solver for solving little **self-referencial logic puzzles**.

--- 

## Instructions

Use by setting up the problem as a set of constraints referencing each other.

A logic puzzle like this
```
1. Statement 2 is true.
2. Statement 3 is false.
3. The 3 statements are either all true or all false.
```

can then be converted into a set of constraints like this:

```py
from constraints import *

# Declare all different contraint wrappers for later reference with their name/purpose
constraint_01: Constraint = ConstraintWrapper("2 is true")
constraint_02: Constraint = ConstraintWrapper("3 is false")
constraint_03: Constraint = ConstraintWrapper("1, 2, and 3 have the same parity")

# Save them for passing them to the solver later
constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03]

# Fill the wrappers with their resprective constraints
constraint_01.constraint = IsTrueConstraint([constraint_02])
constraint_02.constraint = NOTConstraint(IsTrueConstraint([constraint_03]))
constraint_03.constraint = ParityConstraint(constraints)
```

After that you can get a list of all valid solutions (`List[List[bool]]`) this way:<br>
You can also get debug information directly for every combination by passing `True` as the 2nd argument or print valid solutions by passing `True` as the 3rd argument as they come in.
```py
from solver import solve_with_constraints

solutions: List[List[bool]] = solve_with_constraints(constraints, False, True)
```

### The different Constraints
There exists a number of different constraints that can be used to model puzzles:
| Constraint | Function |
| --- | --- |
| `Constraint` | Abstract base constraint, not to be used. |
| `ConstraintWrapper` | A wrapper for another constraint, used to wrap constraints and not loose references while assigning the puzzle.  |
| `NOTConstraint` | A constraint is fulfilled if the constraint wrapped inside it is not fulfilled. |
| `ORConstraint` | A constraint is fulfilled if **any** constraint wrapped inside it is fulfilled. |
| `ANDConstraint` | A constraint is fulfilled if **all** constraint wrapped inside it is fulfilled. |
| `CountConstraint` | A constraint is fulfilled the amount of constraints that are assigned true lies within a given range. |
| `IsTrueConstraint` | A constraint is fulfilled if all constraints wrapped inside are assigned true. |
| `ParityConstraint` | A constraint is fulfilled if all constraints wrapped inside are assigned the same value. |

## AI Disclosure

AI (in the form of Githubs Autocomplete) was only used towards the end as I began translating the puzzles from deckards video into the `puzzle_n.py` files. The `.md` files, `solver.py` and `constraints.py` file were written without any AI usage. <br>
The `colors.py` was taken from https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007 <br>
The `.gitignore` file was AI generated.
