import time
import requests

from connectivity_tester.consts import HTTP_TIMEOUT, LATENCY_KEY
from connectivity_tester.models.test_result import TestResult
from connectivity_tester.protocols_testers.abstract_tester import ProtocolTester


class HttpTester(ProtocolTester):

    def test(self, url: str) -> TestResult:
        try:
            start_time = time.time()

            # Check connectivity
            response = requests.get(url, timeout=HTTP_TIMEOUT)
            response.raise_for_status()  # Check for HTTP errors

            # Measure latency
            end_time = time.time()
            latency = end_time - start_time

            return TestResult(True, {LATENCY_KEY: latency})
        except requests.RequestException as e:
            return TestResult(False)


if __name__ == "__main__":
    h=HttpTester()
    r = h.test("https://www.facebook.com")
    print(r.is_success)
    print(r.additional_info)
