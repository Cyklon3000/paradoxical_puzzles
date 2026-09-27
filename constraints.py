from abc import abstractmethod
from typing import Dict, List
class Constraint:
    is_true: bool
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def get_is_true(self, assignments) -> bool:
        return False


class ConstraintWrapper(Constraint):
    name: str
    constraint: Constraint
    
    def __init__(self, name):
        self.name = name
    
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        return self.constraint.get_is_true(assignments)


class NOTConstraint(Constraint):
    constraint: Constraint

    def __init__(self, constraint: Constraint):
        self.constraint = constraint
        
    
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        return not self.constraint.get_is_true(assignments)


class ORConstraint(Constraint):
    constraints: List[Constraint] = []
    
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints
        
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        for constraint in self.constraints:
            if constraint.get_is_true(assignments):
                return True
        return False


class ANDConstraint(Constraint):
    constraints: List[Constraint] = []
    
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints
        
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        for constraint in self.constraints:
            if not constraint.get_is_true(assignments):
                return False
        return True


class CountConstraint(Constraint):
    constraints: List[Constraint]
    min_true: int
    max_true: int
    
    def __init__(self, constraints: List[Constraint], min_true: int, max_true: int):
        self.constraints = constraints
        self.min_true = min_true
        self.max_true = max_true
    
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        true_count: int = 0
        for constraint in self.constraints:
            true_count += int(assignments[constraint])
        
        return self.min_true <= true_count <= self.max_true


class IsTrueConstraint(Constraint):
    constraints: List[Constraint]
    
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints
    
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
        for constraint in self.constraints:
            if not assignments[constraint]:
                return False
        return True


class ParityConstraint(Constraint):
    constraints: List[Constraint]
    
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints
    
    def get_is_true(self, assignments: Dict[Constraint, bool]) -> bool:
            is_all_false: bool = True
            is_all_true: bool = True
            for constraint in self.constraints:
                if assignments[constraint]:
                    is_all_false = False
                else:
                    is_all_true = False
            
            return is_all_true or is_all_false