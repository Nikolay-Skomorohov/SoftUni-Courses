class Human:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        elif not len(value) > 3:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        elif not len(value) > 3:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        else:
            self.__last_name = value


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number: str):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        if len(value) in range(5, 10) and value.isalnum():
            self.__faculty_number = value
        else:
            raise Exception("Invalid faculty number!")

    def __str__(self):
        return f"First Name: {self.first_name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Faculty number: {self.faculty_number}"


class Worker(Human):
    def __init__(self, first_name, last_name, weekly_salary: float, hours_per_day: float):
        Human.__init__(self, first_name, last_name)
        self.weekly_salary = weekly_salary
        self.hours_per_day = hours_per_day

    def pay_per_hour(self):
        return (self.weekly_salary / 5) / self.hours_per_day

    @property
    def weekly_salary(self):
        return self.__weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value):
        if not value > 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        else:
            self.__weekly_salary = value

    @property
    def hours_per_day(self):
        return self.__hours_per_day

    @hours_per_day.setter
    def hours_per_day(self, value):
        if 1 <= value <= 12:
            self.__hours_per_day = value
        else:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")

    def __str__(self):
        return f"First Name: {self.first_name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Week Salary: {self.weekly_salary:.2f}\n" \
               f"Hours per day: {self.hours_per_day:.2f}\n" \
               f"Salary per hour: {self.pay_per_hour():.2f}"


try:
    student_input = input().split()
    new_student = Student(student_input[0],
                          student_input[1],
                          student_input[2])
    worker_input = input().split()
    new_worker = Worker(worker_input[0],
                        worker_input[1],
                        float(worker_input[2]),
                        float(worker_input[3]))
    print(new_student)
    print()
    print(new_worker)
except Exception as text:
    print(text)
