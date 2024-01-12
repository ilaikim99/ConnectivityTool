from connectivity_tester.consts import LATENCY_KEY
from connectivity_tester.models.protocol_type import ProtocolType
from connectivity_tester.models.test_instance import TestInstance
from connectivity_tester.results_storage import ResultsStorage


class ResultsHandler:
    PROTOCOLS_LATENCY_CHECK = [ProtocolType.HTTP, ProtocolType.HTTPS]

    def __init__(self, results_storage: ResultsStorage, latency_threshold: float):
        self.results_storage: ResultsStorage = results_storage
        self.latency_threshold: float = latency_threshold

    def handle_new_instance(self, test_instance: TestInstance) -> None:
        print(test_instance)
        self.handle_latency_check(test_instance)
        self.results_storage.add_test(test_instance)

    def handle_latency_check(self, test_instance: TestInstance) -> None:
        if test_instance.protocol_type in self.PROTOCOLS_LATENCY_CHECK:
            self.validate_latency(test_instance)
            self.latency_check(test_instance)

    @staticmethod
    def validate_latency(test_instance: TestInstance) -> None:
        if test_instance.test_result.additional_info.get(LATENCY_KEY) is None:
            raise ValueError("Test Instance don't have LATENCY KEY")

    def latency_check(self, test_instance: TestInstance) -> None:
        last_similar_instance = self.results_storage.get_last_similar_test(test_instance)
        if last_similar_instance:
            last_latency = last_similar_instance.test_result.additional_info.get(LATENCY_KEY)
            current_latency = test_instance.test_result.additional_info.get(LATENCY_KEY)
            if abs(current_latency - last_latency) > self.latency_threshold:
                print(f"Alert: Latency differs from previous run in more than {self.latency_threshold} seconds!")
