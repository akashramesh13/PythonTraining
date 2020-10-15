import pytest


@pytest.mark.parametrize("val", ["Akash", "Ramesh", "SAnthosh"])
# void
def test_contains_a(val) -> None:
    assert "a" or "A" in val
