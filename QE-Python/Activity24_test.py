import pytest
import pandas as pd

def get_csv():
    data=pd.read_csv("C:\\Users\\VNikhil\\Desktop\\Python prog\\tests\\test_case.csv")
    return list(data.itertuples(index=False, name=None))

@pytest.mark.parametrize("earned,spent,expected",get_csv())
def test_param(earned,spent,expected):
    assert earned - spent==expected
    
    
