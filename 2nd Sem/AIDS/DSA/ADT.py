class ListADT:
    def __init__(self):
        self.arr = []
    def insert(self, val):
        self.arr.append(val)
        print(f"{val} inserted")
    def delete(self, val):
        if val in self.arr:
            self.arr.remove(val)
            print(f"{val} deleted")
        else:
            print(f"{val} not found")
    def search(self, val):
        if val in self.arr:
            print(f"{val} found at position {self.arr.index(val)+1}")
        else:
            print(f"{val} not found")
    def modify(self, old, new):
        if old in self.arr:
            idx = self.arr.index(old)
            self.arr[idx] = new
            print(f"{old} modified to {new}")
        else:
            print(f"{old} not found")
    def display(self):
        print("List:", self.arr)
  
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