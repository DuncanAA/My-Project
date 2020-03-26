class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.gender == new_gender
        else:
            print('請輸入MorF')
    def borrow_resources(self):
        pass
    def check_auth(self):
        pass

class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resources(self):
        print('student borrow')
class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print('Professor borrow')

student1=Student('M','工管系','M11111111')
student2=Student('F','工管系','M33333333')
professor1=Professor('F','數媒系','S11111111')
professor2=Professor('M','數媒系','S33333333')
ls=[student1,student2,professor1,professor2]

for item in ls:
    item.borrow_resources()