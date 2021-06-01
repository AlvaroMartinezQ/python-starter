class Person():

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'Person name: {self.name}'

# Define an employee class which inherits from Person class defined above
class Employee(Person):

    def __init__(self, name, idemp) -> None:
        super().__init__(name)
        self.idemp = idemp

    def __str__(self) -> str:
        return f'Employee id: {self.idemp} | Employee name: {self.name}'


if __name__ == "__main__":
    e = Employee("alvaro", 1)
    # If employee class didn't have a __str__ method it would print Person's __str__ method
    print(e.__str__())