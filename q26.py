#classstaffreg
class TeacherReg:
    def __init__(self,name,age,domain):
        self.name=name
        self.age=age
        self.domain=domain
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Domain:",self.domain)

staff1=TeacherReg("Jenifer",27,"CSE")
staff2=TeacherReg("Anitha",29,"IT")
staff1.display()
staff2.display()