from collections import deque

class DeQ(deque):
    def __init__(self,exp):
        self.exp = str(exp)

    def __is_empty__(self):
        if len(a) == 0:
            return True
        else:
            return False

    def add_first(self,e):
        a.append(e)

    def add_last(self,e):
        a.appendleft(e)

    def del_first(self):
        if  not a.__is_empty__():
            a.pop()

    def del_Last(self):
        if  not a.__is_empty__():
            a.popleft()
    

    def last(self):
        if  not a.__is_empty__():
            x=a.del_Last()
            a.append(x)
            return x

    def _palindrome(self):
        for i in self.exp:
            a.add_first(i)
        str = ""
        for i in self.exp:
            str+=a.pop()
        if str == self.exp:
            print("Palindrome")
        else:
            print("Not a Palindrome")

b=input("Enter String:")
a=DeQ(b)
a._palindrome()