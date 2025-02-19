class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")

person_instance = Person()
student_instance = Student()

person_instance.introduce()
student_instance.introduce()