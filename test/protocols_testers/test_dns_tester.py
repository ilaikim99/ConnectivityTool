import pytest

from connectivity_tester.protocols_testers.dns_tester import DnsTester


@pytest.fixture
def dns_tester():
    return DnsTester()


def test_valid_url(dns_tester):
    test_result = dns_tester.test("example.com")
    assert test_result.is_success is True


def test_invalid_url(dns_tester):
    test_result = dns_tester.test("nonexistenturl123")
    assert test_result.is_success is False
