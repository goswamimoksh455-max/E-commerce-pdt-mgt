import pytest

product_list = [{"name":"Ghee","price":1000},{"name":"Butter milk","price":19}]

def add_product (p):
    product_list.append(p)

def remove_product(p):
    product_list.remove(p)

def get_product(name):
    product = {"name":"abc"}
    # for p in product_list :
        
    return product

def get_all():
    return product_list

def include_tax(price):
    return price + 10

@pytest.fixture
def give_name():
    n = "Ghee"
    return n

@pytest.mark.get
def test_get_pdt():
    pdt = get_all()
    if len(pdt) > 0:
        assert True

@pytest.mark.get_that_pdt
def test_get_that(give_name):
    pdt = get_product(give_name)
    if pdt != {}:
        assert True
    else:
        assert False

        
