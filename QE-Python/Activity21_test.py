import pytest
@pytest.mark.a
def test_sum():
    n1=25
    n2=20
    assert n1+n2==45
@pytest.mark.b
def test_diff():
    n1=25
    n2=20
    assert n1+n2==45
@pytest.mark.a
def test_prod():
    n1,n2=21,2
    assert n1*n2==42
@pytest.mark.b
def test_quo():
    n1,n2=10,5
    assert n1/n2==4
    
