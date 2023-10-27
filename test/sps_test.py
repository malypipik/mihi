from restaurant import get_day_from_number

def test_get_day_from_number():
    result = get_day_from_number(1)
    assert result == "Monday"

# def test_test_get_day_from_invalid_number():
