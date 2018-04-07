"""School members"""


class SchoolMember:
    """Representing any human being in school.
    """
    def __init__(self, name, age):
        """Create instance of SchoolMember.

        :param name: name of a human being.
        :param name: str.
        :param age: age of a human being.
        :param age: int.
        :returns: instance of SchoolMember.
        :raises: AssertionError.
        """
        assert isinstance(name, str), "Name must be str"
        assert isinstance(age, int) and age > 0, "Age must be int"
        self._name = name.title()
        self._age = age
        print(f"(Создан {SchoolMember.__name__}: {self._name})")

    def show(self):
        """Shows data of a human being.

        :returns: None
        """
        print("Имя:{}; Возраст: {}".format(self._name, self._age))


class Teacher(SchoolMember):
    """Representing teacher in school.
    """
    def __init__(self, name, age, salary):
        """Create instance of Teacher.

        :param name: name of a teacher.
        :param name: str.
        :param age: age of a teacher.
        :param age: int.
        :param salary: salary of a teacher
        :returns: instance of Teacher.
        :raises: AssertionError.
        """
        super().__init__(name, age)
        assert isinstance(salary, int) and salary > 0, "Salary must be int"
        self._salary = salary
        print("(Создан {}: {})".format(Teacher.__name__, name))

    def show(self):
        """Shows data of a teacher.

        :returns: None
        """
        print("Имя: {}; Возраст: {}; Зарплата: {} ".format(self._name, self._age, self._salary))


class Student(SchoolMember):
    """Representing schoolboy profile.
    """
    def __init__(self, name, age, gpa):
        """Create instance of Teacher.

        :param name: name of a student.
        :param name: str.
        :param age: age of a student.
        :param age: int.
        :param gpa: grade point average of a student.
        :param gpa: int.
        :returns: instance of Student.
        :raises: AssertionError.
                """
        super().__init__(name, age)
        assert isinstance(gpa, (int, float)) and gpa > 0, "Gpa must be positive numeric"
        self._gpa = gpa
        print("(Создан {}: {})".format(Student.__name__, name))

    def show(self):
        """Shows data of a student.

        :returns: None
        """
        print("Имя: {}; Возраст: {}; Cредний бал: {} ".format(self._name, self._age, self._gpa))


if __name__ == '__main__':
    PERSONS = [Teacher("Mr. Goldenfold", 40, 3000), Student("Morty", 16, 3.9)]
    for person in PERSONS:
        person.show()
