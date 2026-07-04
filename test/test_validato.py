import pytest

from validator import _validate_types
from errors import InvalidAgeError


# -------------------------
# Valid age values
# -------------------------

@pytest.mark.parametrize(
    "value",
    [
        25,
        "25",
        " 25 ",
        None,
    ],
)
def test_validate_type_age_valid(value):
    data = {"age": value}

    _validate_types(data)


# -------------------------
# Invalid age values
# -------------------------

@pytest.mark.parametrize(
    "value",
    [
        "",
        "abc",
        "25 years",
    ],
)
def test_validate_type_age_invalid(value):
    data = {"age": value}

    with pytest.raises(InvalidAgeError):
        _validate_types(data)