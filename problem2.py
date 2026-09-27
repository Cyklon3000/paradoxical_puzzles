from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint = ConstraintWrapper("2 is true", None)
constraint_02: Constraint = ConstraintWrapper("3 is false", None)
constraint_03: Constraint = ConstraintWrapper("1, 2 and 3 have the same parity", None)

constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03]

constraint_01.constraint = IsTrueConstraint([constraint_02])
constraint_02.constraint = NOTConstraint(IsTrueConstraint([constraint_03]))
constraint_03.constraint = ParityConstraint([constraint_01, constraint_02, constraint_03])

print("Solutions: \n\t" + str(solve_with_constraints(constraints)))