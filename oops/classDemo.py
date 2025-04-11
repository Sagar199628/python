

# class pen:
#     a = 10
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
#
#     def test (self):
#         print(self.id,self.name)
#
#     @staticmethod
#     def disp():
#         print("display calling...",a )
#
#     @classmethod
#     def demo(self):
#         print("running demo",self.a)
#
#
# p = pen(10,"sagar")
# p.test()
#
# p1 = pen(20,"mohan")
# p1.test()
#
# p2 = pen(30,"harsh")
# p2.test()

# pen.disp()
# pen.demo()



# class student:

#     def __init__(self,id,name,phone):
#         self.id = id
#         self.name = name
#         self.phone = phone

#     def test (self):
#         print(self.id,self.name,self.phone)

# s = student(12,"sagar",987654)
# s.test()

# s1 = student(13,"mohan", 9864526)
# s1.test()


# init function:
# class person:
#     def __init__ (self, name):
#         self.name = name

    # def __str__(self): #str mthd.
    #     return f"{self.name}"
# p1 = person("sagar")
# print(p1.name)
# print(p1)


# class Cars:
    # def __init__ (self, name,color):
        # self.name = name
        # self.color = color
    # def god (self):
    #     print(self.name,self.color)

# print(c.name)
# c1 = Cars("Red")
# print(c1.color)

# c = Cars("Toyota","Red")
# c.god()

# c = Cars("Toyota","Red")
# print(c.name,c.color)
# c1 = Cars("Kiya", "White")
# print(c1.name,c1.color)

# class Pen:
#     clg = "drstc"
#
#     # name="tops"
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print("display calling", self.id, self.name, self.clg)
#
#     def test(self):
#         print("test calling")
#
#     @classmethod
#     def show(self):
#         print("show calling", self.clg)
#
#     @staticmethod
#     def run():
#         print("run calling...")
#
#
# Pen.clg = "abc"
#
# p = Pen(10, "Akash")
# p.display()
#
# p1 = Pen(20, "Farukh")
# p1.display()
#
# p2 = Pen(30, "Rudra")
# p2.display()
#
# Pen.show()
# Pen.run()