import sys, os

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, main_dir)

from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint = ConstraintWrapper("no three consecuetives have the same parity")
constraint_02: Constraint = ConstraintWrapper("2 or 3 of odd statements are true")
constraint_03: Constraint = ConstraintWrapper("exactly 2 true of 4, 5, 6 and 7")
constraint_04: Constraint = ConstraintWrapper("3 and 5 have same parity")
constraint_05: Constraint = ConstraintWrapper("4 and 6 have different parity")
constraint_06: Constraint = ConstraintWrapper("exactly 1 true of 3, 8 and 9")
constraint_07: Constraint = ConstraintWrapper("5 and 6 have different parity")
constraint_08: Constraint = ConstraintWrapper("1 and 9 have same parity")
constraint_09: Constraint = ConstraintWrapper("1 and 8 have same parity")
constraint_10: Constraint = ConstraintWrapper("4 or 5 true of 1-9")

constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03, constraint_04, constraint_05, constraint_06, constraint_07, constraint_08, constraint_09, constraint_10]
odd_constraints: List[Constraint] = [constraint_01, constraint_03, constraint_05, constraint_07, constraint_09]
three_consecutive_constraints: List[List[Constraint]] = [
    ParityConstraint([constraint_01, constraint_02, constraint_03]),
    ParityConstraint([constraint_02, constraint_03, constraint_04]),
    ParityConstraint([constraint_03, constraint_04, constraint_05]),
    ParityConstraint([constraint_04, constraint_05, constraint_06]),
    ParityConstraint([constraint_05, constraint_06, constraint_07]),
    ParityConstraint([constraint_06, constraint_07, constraint_08]),
    ParityConstraint([constraint_07, constraint_08, constraint_09]),
    ParityConstraint([constraint_08, constraint_09, constraint_10])
]

constraint_01.constraint = NOTConstraint(ORConstraint(three_consecutive_constraints))
constraint_02.constraint = CountConstraint(odd_constraints, 2, 3)
constraint_03.constraint = CountConstraint([constraint_04, constraint_05, constraint_06, constraint_07], 2, 2)
constraint_04.constraint = ParityConstraint([constraint_03, constraint_05])
constraint_05.constraint = NOTConstraint(ParityConstraint([constraint_04, constraint_06]))
constraint_06.constraint = CountConstraint([constraint_03, constraint_08, constraint_09], 1, 1)
constraint_07.constraint = NOTConstraint(ParityConstraint([constraint_05, constraint_06]))
constraint_08.constraint = ParityConstraint([constraint_01, constraint_09])
constraint_09.constraint = ParityConstraint([constraint_01, constraint_08])
constraint_10.constraint = CountConstraint(constraints[0:9], 4, 5)


solve_with_constraints(constraints, False, True)