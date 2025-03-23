class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

# Example usage
my_class = MyClass()
data1 = "Hello, World!"
data2 = [1, 2, 3]

my_class.add_data(data1)
my_class.add_data(data2)

print("Data:", my_class.get_data())
