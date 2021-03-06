class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "《%s》" % self.title

    def __call__(self):
        print("《%s》是%s写的" % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('Core Python', 'Wesley')   # 调用__init__
    print(core_py)    # 调用__str__
    core_py()     # 调用__call__
