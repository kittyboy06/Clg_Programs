class ListADT:
    def __init__(self):
        self.lst = []
    def insert(self, val):
        self.lst.append(val)
        print(f"{val} inserted")
    def delete(self, val):
        if val in self.lst:
            self.lst.remove(val)
            print(f"{val} deleted")
        else:
            print(f"{val} not found")
    def search(self, val):
        if val in self.lst:
            print(f"{val} found at position {self.lst.index(val)+1}")
        else:
            print(f"{val} not found")
    def modify(self, old, new):
        if old in self.lst:
            idx = self.lst.index(old)
            self.lst[idx] = new
            print(f"{old} modified to {new}")
        else:
            print(f"{old} not found")
    def display(self):
        print("List:", self.lst)
        
lst = ListADT()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.display()
lst.search(20)
lst.modify(20, 25)
lst.display()
lst.delete(10)
lst.display()