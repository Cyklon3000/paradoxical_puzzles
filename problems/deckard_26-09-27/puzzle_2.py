import sys, os

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, main_dir)

from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint = ConstraintWrapper("2 is true")
constraint_02: Constraint = ConstraintWrapper("there is exactly one true constraint")

constraints: List[Constraint] = [constraint_01, constraint_02]

constraint_01.constraint = IsTrueConstraint([constraint_02])
constraint_02.constraint = CountConstraint(constraints, 1, 1)

solve_with_constraints(constraints, True)