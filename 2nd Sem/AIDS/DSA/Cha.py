list_adt = []
def insert(value):
    list_adt.append(value)
    print(f"{value} inserted")
def delete(value):
    if value in list_adt:
        list_adt.remove(value)
        print(f"{value} deleted")
    else:
        print(f"{value} not found")
def search(value):
    if value in list_adt:
        print(f"{value} found at position {list_adt.index(value)+1}")
    else:
        print(f"{value} not found")
def modify(old_value, new_value):
    if old_value in list_adt:
        idx = list_adt.index(old_value)
        list_adt[idx] = new_value
        print(f"{old_value} modified to {new_value}")
    else:
        print(f"{old_value} not found")
def display():
    print("List:", list_adt)
insert(10)
insert(20)