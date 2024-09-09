# Test cases for sort_packages.py

# Run with: pytest
from sort_packages import sort

def test_standard_package():
    assert sort(10, 10, 10, 10) == "STANDARD"

def test_special_package_bulky():
    assert sort(200, 10, 10, 10) == "SPECIAL"

def test_special_package_heavy():
    assert sort(10, 10, 10, 30) == "SPECIAL"

def test_rejected_package():
    assert sort(200, 10, 10, 30) == "REJECTED"

def test_edge_case_volume_tolerance():
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_edge_case_dim_tolerance():
    assert sort(150, 10, 10, 10) == "SPECIAL"

def test_edge_case_mass_tolerance():
    assert sort(10, 10, 10, 20) == "SPECIAL"