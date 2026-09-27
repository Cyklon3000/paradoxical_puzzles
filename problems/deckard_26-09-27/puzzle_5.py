import sys, os

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, main_dir)

from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint = ConstraintWrapper("3 and 4 have the same parity")
constraint_02: Constraint = ConstraintWrapper("there are exactly three true constraints")
constraint_03: Constraint = ConstraintWrapper("1 and 5 have the different parity")
constraint_04: Constraint = ConstraintWrapper("there are 3-5 true statements")
constraint_05: Constraint = ConstraintWrapper("3 is false")

constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03, constraint_04, constraint_05]

constraint_01.constraint = ParityConstraint([constraint_03, constraint_04])
constraint_02.constraint = CountConstraint(constraints, 3, 3)
constraint_03.constraint = NOTConstraint(ParityConstraint([constraint_01, constraint_05]))
constraint_04.constraint = CountConstraint(constraints, 3, 5)
constraint_05.constraint = NOTConstraint(IsTrueConstraint([constraint_03]))

solve_with_constraints(constraints, False, True)