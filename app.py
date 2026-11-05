product_list = []

def add_product (p):
    product_list.append(p)

def remove_product(p):
    product_list.remove(p)

def get_product(id):
    product = {}
    for p in product_list :
        if id == p.id :
            print(p)

    