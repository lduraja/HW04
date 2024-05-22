import pytest

from assignment_4_1 import encode_message


@pytest.mark.parametrize(
    ("code", "message", "expected_encoded_message"),
    [
        ("ALGORITMUS", "HELLO", "MRWWZ"),
        ("algoritmus", "hello", "MRWWZ"),
        ("algoritmus", "MRWWZ", "XDKKQ"),
        ("ALGORITHM", "HELLO", "HRQQV"),
        ("ALGORITHM", "scissors", "ZGMZZVYZ"),
        ("PYTHON", "ALGORITHM", "PWQADSFRX"),
        ("ALGORITMUS", "HOKUSPOKUS", "MZVHEBZVHE"),
        ("GOAT", "GrindOptimizeAutomateThrive", "WJYETFHLYDYSUGMLFDGLULXJYNU"),
    ]
)
def test_encrypt_message(code, message, expected_encoded_message):
    assert encode_message(code, message) == expected_encoded_message
