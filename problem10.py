from constraints import *
from solver import solve_with_constraints

constraint_01: Constraint
constraint_02: Constraint
constraint_03: Constraint
constraint_04: Constraint
constraint_05: Constraint
constraint_06: Constraint
constraint_07: Constraint
constraint_08: Constraint
constraint_09: Constraint
constraint_10: Constraint

constraints: List[Constraint] = [constraint_01, constraint_02, constraint_03, constraint_04, constraint_05, constraint_06, constraint_07, constraint_08, constraint_09, constraint_10]
odd_constraints: List[Constraint] = [constraint_01, constraint_03, constraint_05, constraint_07, constraint_09]
three_consecutive_constraints: List[List[Constraint]] = [
    ParityConstraint("", [constraint_01, constraint_02, constraint_03]),
    ParityConstraint("", [constraint_02, constraint_03, constraint_04]),
    ParityConstraint("", [constraint_03, constraint_04, constraint_05]),
    ParityConstraint("", [constraint_04, constraint_05, constraint_06]),
    ParityConstraint("", [constraint_05, constraint_06, constraint_07]),
    ParityConstraint("", [constraint_06, constraint_07, constraint_08]),
    ParityConstraint("", [constraint_07, constraint_08, constraint_09]),
    ParityConstraint("", [constraint_08, constraint_09, constraint_10])
]

constraint_01: Constraint = NOTConstraint("no three consecuetives have the same parity", ORConstraint("",))
constraint_02: Constraint = CountConstraint("odd statements 2 or 3 are true", odd_constraints, 2, 3)
constraint_03: Constraint = CountConstraint("exactly 2 true of 4, 5, 6 and 7", [constraint_04, constraint_05, constraint_06, constraint_07], 2, 2)
constraint_04: Constraint = ParityConstraint("3 and 5 have same parity", [constraint_02, constraint_03])
constraint_05: Constraint = NOTConstraint("4 and 6 have different parity", ParityConstraint("", [constraint_02, constraint_03]))
constraint_06: Constraint = CountConstraint("exactly 1 true of 3, 8 and 9", [constraint_03, constraint_08, constraint_09], 1, 1)
constraint_07: Constraint = NOTConstraint("5 and 6 have different parity", ParityConstraint("", [constraint_05, constraint_06]))
constraint_08: Constraint = ParityConstraint("1 and 9 have same parity", [constraint_01, constraint_09])
constraint_09: Constraint = ParityConstraint("1 and 8 have same parity", [constraint_01, constraint_09])
constraint_10: Constraint = CountConstraint("4 or 5 true of 1-9", constraints[0::-2], 4, 5)