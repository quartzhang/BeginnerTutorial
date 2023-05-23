import copy

class Student():
    def __init__(self,id,name,ml_grade,python_grade,eng_grade):
        self.id = id
        self.name = name
        self.ml_grade=ml_grade
        self.python_grade=python_grade
        self.eng_grade = eng_grade



class StudentSystem():
    def __init__(self, l):
        self.list = l

    def add_stu_info(self, student:Student):
        if self.exist(student.id):
            print("the stu'info is already in the system")
            return
        self.list.append(student)


    def delete(self, id):
        if not self.exist(id):
            print("the stu'info is not in the system")
            return

        for i in self.list:
            if i.id == id:
                self.list.remove(i)

    def update(self,student):
        ## 对比下前后信息是否发生改变
        for i in self.list:
            if i.name == student.name:
                i.ml_grade = student.ml_grade
                i.python_grade = student.python_grade
                i.eng_grade = student.eng_grade

    def show_info(self, id):
        ## 判断是否有对应的信息
        if not self.exist(id):
            print(f"there is no student with {id}")
            return
        for i in self.list:
            if i.id == id:
                print(i.ml_grade,i.python_grade,i.eng_grade)

    def calculate(self, id):
        if not self.exist(id):
            print(f"there is no student with {id}")
            return
        for i in self.list:
            if i.id == id:
                mean = (int(i.ml_grade)+int(i.python_grade)+int(i.eng_grade))/3
                return mean

    def rank_ml(self):
        ## 从大到小排序
        tempList = copy.deepcopy(self.list)
        for i in range(len(tempList)):
            for j in range(i+1, len(tempList)):
                if int(tempList[i].ml_grade) < int(tempList[j].ml_grade):
                    tempList[i], tempList[j] = tempList[j], tempList[i]
        self.tostring(tempList)

    def rank_eng(self):
        ## 从大到小排序
        tempList = copy.deepcopy(self.list)
        for i in range(len(tempList)):
            for j in range(i+1, len(tempList)):
                if int(tempList[i].eng_grade) < int(tempList[j].eng_grade):
                    tempList[i], tempList[j] = tempList[j], tempList[i]
        self.tostring(tempList)

    def rank_py(self):
        ## 从大到小排序
        tempList = copy.deepcopy(self.list)
        for i in range(len(tempList)):
            for j in range(i+1, len(tempList)):
                if int(tempList[i].python_grade) < int(tempList[j].python_grade):
                    tempList[i], tempList[j] = tempList[j], tempList[i]
        self.tostring(tempList)



    def exist(self, id):
        for i in range(len(self.list)):
            if self.list[i].id == id:
                return True
        return False

    def tostring(self, temp):
        for i in range(len(temp)):
            print(f"id {temp[i].id} name {temp[i].name} grades:  {temp[i].ml_grade} , {temp[i].python_grade} , {temp[i].eng_grade} ")






a = []

sys = StudentSystem(a)
student1 = Student("001", "zhangrui", "100", "100", "100")
student2 = Student("002", "yuanchuanyu", "59", "59", "58")
student3 = Student("003", "zhangsan", "60", "60", "60")
student4 = Student("004", "lisi", "99", "98", "100")
student5 = Student("005", "wangerma", "32", "60", "76")
student6 = Student("006", "wangwu", "78", "62", "98")

sys.add_stu_info(student1)
sys.add_stu_info(student2)
sys.add_stu_info(student3)
sys.add_stu_info(student4)
sys.add_stu_info(student5)
sys.add_stu_info(student6)
# sys.tostring()
#
# sys.delete("001")
# sys.tostring()
#
# sys.show_info("001")
#
# sys.update(Student("002", "yuanchuanyu", "59", "59", "59"))
# sys.tostring()
#
# print(sys.calculate("002"))

sys.rank_ml()
print()
sys.rank_eng()
print()
sys.rank_py()







