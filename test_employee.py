import pytest
from employeedetails import get_ED
def test_get_ED():
    #sample data
    name="Sahana"
    emp_id="Bca202"
    dep="BCA"
    salary=60000
    #Expected result
    expected_output =(
        "Employee Name:Sahana,\n"
        "Employee ID:Bca202,\n"
        "Department:BCA,\n"
        "Salary:60000.00"
    )
    #Assertion
    assert get_ED(name, emp_id, dep, salary)==expected_output