# The Uberject project 
# version 0.01
# Created by Søren Pilgård
# Contact through github.com
# The project is aimed for python 2.X

# /*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <github.com/Pilen> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Søren Pilgård
# * ----------------------------------------------------------------------------
# */


class UberjectTypeError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return repr(self.msg)

class Uberject():
    __doc__ = 'Base class for the uberject project'
    __parents__ = []
    __type__ = 'Uberject'

class Ubermethod():
    __doc__ = 'Base function class'
    __parents__ = ['Uberject']
    __type__ = 'Uberfunction'
    def __init__(self,functionname, function, parmtypelist, returntype):
        self.functionname = functionname
        self.function = function
        self.parmtypelist = parmtypelist
        self.returntype = returntype
    def __call__(self, *args):
        for i in range(len(args)):
            if not isuberstance(arg[i],self.parmtypelist[i]):
                raise TypeError('Typeerror in %s: argument of type %s, should be of type %s' %
                                self.functionname, arg[i].__type__, self.parmtypelist[i])
        result = self.function(*args)
        if not isuberstance(result,self.returntype):
            raise TypeError('Typeerror in %s: returns %s, should be %s' %
                            self.functionname, result.__type__, self.returntype)
        return result



u = Uberject()

def extend(obj,functionname, function, parmtypelist, returntype):
    f = Uberfunction(functionname, function, parmtypelist, returntype)
    obj.functionname = f

def isuberstance(a, b):
    if a
def uberclass(name, listofparents, listoffunctions):
    o = Uberject()
    o.__parents__.append(o.__type__)
    o.__type__ = name
    o.


def uberclass(c):
    
