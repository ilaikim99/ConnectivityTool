
class TestResult:
    def __init__(self, is_success: bool, additional_info: dict=None):
        self.is_success: bool = is_success
        self.additional_info: dict = additional_info
