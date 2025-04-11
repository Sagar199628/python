
# class A:
#     a = 20
#     b = 30
#     def show(self):
#         print("show",self.a)

# class B(A):

    # def run(self):
    #     print("run",self.b)

# a = A()
# a.show()

# b = B()
# b.run()
# b.show()


# class A:

#     _a = 20
#     def show(self):
#         print("Class A show mwthod calling",self._a)

# class B(A):
#     def disp(self):
#         print("class B disp method calling",self._a)
# class C(A):
#     pass

# b  = B()
# a = A()
# # b._a = 60
# # b.disp()
# print(dir(a))


# class Sample:

#     # def __init__(self,a,b):
#     #     self.a = a
#     #     self.b = b

#     def __init__(self,*a):
#         self.a = a[0]
#         self.b = a[1]


#     def desp(self):
#         print(self.a, self.b)

# class Demo(Sample):

#     def __init__(self, a, b,c):
#         super().__init__(10,20,30)
#     pass


# d = Demo(10,20,30)
# d.desp()


class P:

    def __init__(self):
        print("class p constructor calling")


class Q(P):

    def __init__(self):
        print("class Q constructor calling")
        super().__init__()


q = Q()