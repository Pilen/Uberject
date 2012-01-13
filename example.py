### A simple python thing to test out uberject

class Calculator():
    def add(self,x,y):
        '''int int -> int'''
        return x+y
    def mul(self,x,y):
        mul.retype= int
        mul.patype= (int,int)
        return x*y
uberclass(Calculator)

class Stackcalculator():
    def __init__(self):
        '''None -> None'''
        self.stack = []
    def push(self,number):
        '''int -> None'''
        self.stack.push(number)
    def add(self):
        '''None -> int'''
        x = self.stack.pop()
        y = self.stack.pop()
        return x+y
uberclass(Stackcalculator)


class RealStackCalculator(Stackcalculator):
    '''Stackcalculator'''
    def push(self,number):
        '''float -> None'''
        self.stack.push(number)
    def add(self):
        '''None -> float'''
        x = self.stack.pop()
        y = self.stack.pop()
        return x+y
uberclass(Stackcalculator)
