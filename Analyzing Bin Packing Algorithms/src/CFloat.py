from __future__ import annotations

import math


class CFloat:
    val: float

    def __init__(self, value: float):
        self.val = value

    def __eq__(self, other: CFloat) -> bool:
        if other is None:
            return False
        # return abs(self.val - other.val) <= sys.float_info.epsilon
        return math.isclose(self.val, other.val)

    # def __lt__(self, other: CFloat) -> bool:
    #     if other is None:
    #         return False
    #     # return not(self == other) and self.val < other.val
    #     return not math.isclose(self.val, other.val) and self.val < other.val
    # ???
    def __lt__(self, other: CFloat):   # for <= operator
        if other is None:
            return False
        return self.val < other.val and not math.isclose(self.val, other.val)

    def __le__(self, other: CFloat):   # for < operator
        if other is None:
            return False
        return self.val <= other.val or math.isclose(self.val, other.val)

    def __gt__(self, other: CFloat):   # for > operator
        if other is None:
            return False
        return self.val > other.val and not math.isclose(self.val, other.val)

    def __ge__(self, other: CFloat) -> bool:  # for >= operator
        if other is None:
            return False
        return self.__gt__(self, other) or self.__eq__(self, other)

    def __sub__(self, other: CFloat):  # for subtraction, e.g. a-b
        return CFloat(self.val - other.val)

    def __rsub__(self, other: CFloat):  # for revert subtraction, e.g. b-a
        return CFloat(other.val - self.val)