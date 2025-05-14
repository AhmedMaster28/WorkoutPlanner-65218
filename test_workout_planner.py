import pytest
from assign import calculate_bmi, suggest_plan

@pytest.mark.parametrize("w,h,expected", [
    (60, 170, pytest.approx(20.76, rel=1e-2)),  # normal range
    (50, 160, pytest.approx(19.53, rel=1e-2)),  # underweight → still compute
])
def test_calculate_bmi_valid(w, h, expected):
    assert calculate_bmi(w, h) == expected

def test_calculate_bmi_zero_height():
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(70, 0)

@pytest.mark.parametrize("bmi,expected", [
    (17.0, (30, "High-protein diet with healthy fats")),
    (22.0, (45, "Balanced diet: carbs, proteins, fats")),
    (27.5, (60, "Low-carb diet with moderate protein")),
    (32.0, (75, "Calorie-deficit diet, focus on veggies")),
])
def test_suggest_plan(bmi, expected):
    assert suggest_plan(bmi) == expected
