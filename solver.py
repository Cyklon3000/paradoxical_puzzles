from typing import List, Dict
from constraints import Constraint
from colors import Colors

def solve_with_constraints(constraints: List[Constraint], print_debug: bool = False, print_valid: bool = False) -> List[List[bool]]:
    solutions: List[List[bool]] = [] 
    solution: List[bool] = [False] * len(constraints)
    while True:
        is_valid = True
        assignments: Dict[Constraint, bool] = dict(zip(constraints, solution))
        constraint: Constraint
        is_assigned_true: bool
        output: str = ""
        for constraint, is_assigned_true in zip(constraints, solution):
            if constraint.get_is_true(assignments) == is_assigned_true:
                output += f"{Colors.GREEN}\tConstraint: {constraint.name}, Assigned: {is_assigned_true}, Evaluated: {constraint.get_is_true(assignments)}{Colors.END}\n"
            else:
                output += f"{Colors.RED}\tConstraint: {constraint.name}, Assigned: {is_assigned_true}, Evaluated: {constraint.get_is_true(assignments)}{Colors.END}\n"
                is_valid = False
                break
        
        if print_debug:
            print(f"{Colors.YELLOW}Solution: {solution}{Colors.END}")
            print(output)
        
        if is_valid:
            solutions.append(solution.copy())
            if print_valid:
                print(f"{Colors.BLUE}Valid solution found: {solution}{Colors.END}")
                print(output)
            
        if not _count_up(solution):
            break

    return solutions


def _count_up(arr: List[bool]) -> bool:
    i = 0
    while arr[i]:
        arr[i] = False
        i += 1
        if i >= len(arr):
            return False
    arr[i] = True
    return True