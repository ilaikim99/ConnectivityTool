from connectivity_tester.input_reader import InputReader, YamlInputReader
from connectivity_tester.models.input import Input
from connectivity_tester.models.protocol_type import ProtocolType
from connectivity_tester.models.test_result import TestResult
from connectivity_tester.protocols_testers.dns_tester import DnsTester
from connectivity_tester.protocols_testers.http_tester import HttpTester
from connectivity_tester.results_handler import ResultsHandler
from connectivity_tester.results_storage import ResultsStorage, CsvResultsStorage


class TestHandler:
    _http_tester = HttpTester()
    TYPE_TO_PROTOCOL_TESTER = {ProtocolType.DNS: DnsTester(),
                               ProtocolType.HTTP: _http_tester,
                               ProtocolType.HTTPS: _http_tester}

    def __init__(self, input_file, results_file):
        self.input_reader: InputReader = YamlInputReader(input_file)
        self.config_input: Input = self.input_reader.get_input()
        self.results_storage: ResultsStorage = CsvResultsStorage(results_file)
        self.results_handler: ResultsHandler = ResultsHandler(self.results_storage, self.config_input.latency_threshold)

    def run_test(self) -> None:
        for test_instance in self.config_input.test_instances:
            test_result: TestResult = self.TYPE_TO_PROTOCOL_TESTER.get(test_instance.protocol_type).test(test_instance.url)
            test_instance.test_result = test_result
            self.results_handler.handle_new_instance(test_instance)
