# list but len returns 1000

class SuperList(list):
    def __len__(self):
        return 1000


sl1 = SuperList()
print(len(sl1))
sl1.append(2)
print(sl1)
print(issubclass(SuperList, list))
