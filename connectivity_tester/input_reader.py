from typing import List

import yaml
from abc import ABC, abstractmethod

from connectivity_tester.consts import LATENCY_KEY, DEFAULT_LATENCY
from connectivity_tester.models.input import Input
from connectivity_tester.models.protocol_type import ProtocolType
from connectivity_tester.models.test_instance import TestInstance


class InputReader(ABC):

    @abstractmethod
    def get_input(self) -> Input:
        pass


class YamlInputReader(InputReader):

    def __init__(self, file_path: str):
        self.yaml_data: dict = None

        try:
            with open(file_path, 'r') as file:
                self.yaml_data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Failed reading yaml file. \n {e}")
            raise SystemExit(1)

    def get_input(self) -> Input:
        try:
            latency: float = self.yaml_data.get(LATENCY_KEY, DEFAULT_LATENCY)
            test_instances: List[TestInstance] = self.generate_test_instances()
            return Input(test_instances, latency)
        except KeyError as e:
            print(f"Error parsing yaml content. \n {e}")
            raise SystemExit(1)

    def generate_test_instances(self) -> List[TestInstance]:
        test_instances = []
        for protocol_type in ProtocolType:
            test_instances.extend(self.get_instances_for_protocol(protocol_type))
        return test_instances

    def get_instances_for_protocol(self, protocol_type: ProtocolType) -> List[TestInstance]:
        urls: List[str] = self.yaml_data.get(protocol_type.value, [])
        return [TestInstance(url, protocol_type) for url in urls]
