from typing import List

class Constraint:
    name: str
    is_true: bool
    
    def __init__(self, name: str):
        self.name = name
    
    def get_is_true(self) -> bool:
        return self.is_true


class NOTConstraint(Constraint):
    constraint: Constraint

    def __init__(self, name: str, constraint: Constraint):
        super().__init__(name)
        self.constraint = constraint
        
    
    def get_is_true(self) -> bool:
        return not self.constraint.get_is_true()


class ORConstraint(Constraint):
    constraints: List[Constraint] = []
    
    def __init__(self, name: str, constraints: List[Constraint]):
        super().__init__(name)
        self.constraints = constraints
        
    def get_is_true(self) -> bool:
        for constraint in self.constraints:
            if constraint.get_is_true():
                return True
        return False


class ANDConstraint(Constraint):
    constraints: List[Constraint] = []
    
    def __init__(self, name: str, constraints: List[Constraint]):
        super().__init__(name)
        self.constraints = constraints
        
    def get_is_true(self) -> bool:
        for constraint in self.constraints:
            if not constraint.get_is_true():
                return False
        return True


class CountConstraint(Constraint):
    constraints: List[Constraint]
    min_true: int
    max_true: int
    
    def __init__(self, name: str, constraints: List[Constraint], min_true: int, max_true: int):
        super().__init__(name)
        self.constraints = constraints
        self.min_true = min_true
        self.max_true = max_true
    
    def get_is_true(self) -> bool:
        true_count: int = 0
        for constraint in self.constraints:
            true_count += int(constraint.is_true)
        
        return self.min_true <= true_count <= self.max_true


class ParityConstraint(CountConstraint):
    def __init__(self, name: str, constraints: List[Constraint]):
        super().__init__(name)
        self.constraints = constraints
    
    def get_is_true(self) -> bool:
            is_all_false: bool = True
            is_all_true: bool = True
            for constraint in self.constraints:
                if constraint.is_true:
                    is_all_false = False
                else:
                    is_all_true = False
            
            return is_all_true or is_all_false