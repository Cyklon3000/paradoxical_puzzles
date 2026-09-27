import sys, os

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, main_dir)

from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint = ConstraintWrapper("3 and 4 have different parity")
constraint_02: Constraint = ConstraintWrapper("1 and 5 have different parity")
constraint_03: Constraint = ConstraintWrapper("1 and 2 have the same parity")
constraint_04: Constraint = ConstraintWrapper("3 and 5 have the same parity")
constraint_05: Constraint = ConstraintWrapper("2 and 4 have different parity")

constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03, constraint_04, constraint_05]

constraint_01.constraint = NOTConstraint(ParityConstraint([constraint_03, constraint_04]))
constraint_02.constraint = NOTConstraint(ParityConstraint([constraint_01, constraint_05]))
constraint_03.constraint = ParityConstraint([constraint_01, constraint_02])
constraint_04.constraint = ParityConstraint([constraint_03, constraint_05])
constraint_05.constraint = NOTConstraint(ParityConstraint([constraint_02, constraint_04]))

solve_with_constraints(constraints, False, True)