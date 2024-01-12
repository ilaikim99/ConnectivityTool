from typing import List

from connectivity_tester.models.test_instance import TestInstance


class Input:
    def __init__(self, test_instances: List[TestInstance], latency_threshold: float):
        self.test_instances: List[TestInstance] = test_instances
        self.latency_threshold: float = latency_threshold
