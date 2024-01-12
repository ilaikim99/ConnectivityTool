from abc import ABC, abstractmethod
import csv
import os
from datetime import datetime

from connectivity_tester.models.test_instance import TestInstance
from connectivity_tester.models.test_result import TestResult


class ResultsStorage(ABC):

    @abstractmethod
    def add_test(self, test_instance: TestInstance) -> None:
        pass

    @abstractmethod
    def get_last_similar_test(self, test_instance: TestInstance) -> TestInstance:
        pass


class CsvResultsStorage(ResultsStorage):
    HEADER = ["url", "protocol", "is_success", "additional_info", "datetime"]

    def __init__(self, file_path):
        self.file_path = file_path
        self.create_csv_if_not_exists()

    def create_csv_if_not_exists(self) -> None:
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(self.HEADER)

    def add_test(self, test_instance: TestInstance) -> None:
        try:
            with open(self.file_path, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([test_instance.url, test_instance.protocol_type.value,
                                     test_instance.test_result.is_success, test_instance.test_result.additional_info,
                                     datetime.now()])
        except Exception as e:
            print(f"Failed adding test instance: {e}")

    def get_last_similar_test(self, test_instance: TestInstance) -> TestInstance:
        try:
            with open(self.file_path, 'r', newline='') as file:
                for row in reversed(list(csv.reader(file))):
                    if row[0] == test_instance.url and row[1] == test_instance.protocol_type.value:
                        return TestInstance(row[0], row[1], TestResult(row[2], eval(row[3])))
        except Exception as e:
            print(f"Failed fetching similar test instance: {e}")
