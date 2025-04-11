class A:
    def disp(self):
        print("Running class A disp")

class B(A):
    def disp(self):
        print("running class B disp")

b = B()
b.disp()