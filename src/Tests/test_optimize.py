from Optimize import optimize
from Tests.settings import API_INPUT


class TestOptimize:
    def test_optimize(self) -> None:
        optimize(API_INPUT)
