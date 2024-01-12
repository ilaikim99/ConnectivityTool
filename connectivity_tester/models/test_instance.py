from connectivity_tester.models.protocol_type import ProtocolType
from connectivity_tester.models.test_result import TestResult


class TestInstance:
    def __init__(self, url: str, protocol_type: ProtocolType, test_result: TestResult = None):
        self.url: str = url
        self.protocol_type: ProtocolType = protocol_type
        self.test_result: TestResult = test_result

    def __repr__(self):
        return f"Url: {self.url}, Protocol: {self.protocol_type.value}, " \
               f"Success: {self.test_result.is_success}, Additional: {self.test_result.additional_info}"
