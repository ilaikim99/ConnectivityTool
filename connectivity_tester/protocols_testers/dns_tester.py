import socket

from connectivity_tester.models.test_result import TestResult
from connectivity_tester.protocols_testers.abstract_tester import ProtocolTester


class DnsTester(ProtocolTester):

    def test(self, url: str) -> TestResult:
        try:
            _ip_address = socket.gethostbyname(url)
            return TestResult(True)
        except socket.gaierror as e:
            return TestResult(False)
