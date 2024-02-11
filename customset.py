class CustomSet:

    def __init__(self):
        self.items = []

    def add(self, item: str)-> set:
        if item not in self.items:
            self.items.append(item)

    def remove(self, item: str)-> set:
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError

    def as_list(self)-> list:
        return self.items.copy()

    def clear(self)-> list:
        self.items.clear()

def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list())
    
    my_set.remove("item 2")
    print(my_set.as_list())

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving foward")

    my_set.clear()
    print(my_set.as_list())

if __name__ == "__main__":
    main()
