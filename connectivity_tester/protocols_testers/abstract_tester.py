from abc import ABC, abstractmethod

from connectivity_tester.models.test_result import TestResult


class ProtocolTester(ABC):

    @abstractmethod
    def test(self, url: str) -> TestResult:
        pass
