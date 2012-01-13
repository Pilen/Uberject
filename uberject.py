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
active = True

types = {
    'bool'       : bool,
    'buffer'     : buffer,
    'bytearray'  : bytearray,
    'complex'    : complex,
    'dict'       : dict,
    'enumerate'  : enumerate,
    'file'       : file,
    'float'      : float,
    'frozenset'  : frozenset,
    'int'        : int,
    'list'       : list,
    'long'       : long,
    'memoryview' : memoryview,
    'object'     : object,
    'property'   : property,
    'reversed'   : reversed,
    'set'        : set,
    'slice'      : slice,
    'tuple'      : tuple,
    'unicode'    : unicode,
    'str'        : str,

    'Uberject'   : Uberject,
    'Ubermethod' : Ubermethod
    }

def define(ty):
    types.update(ty.__name__,ty)
def undefine(ty):
    if types.has_key(ty.__name__):
        types.pop(ty.__name__)
    else raise UberjectUnknownTypeError(ty)
def lookup(ty):
    if types.has_key(ty.__name__):
        return types[ty.__name__]
    else raise UberjectUnknownTypeError(ty)

class UberjectTypeError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return repr(self.msg)

class UberjectUnknownTypeError(Exception):
    def __str__(self,type):
        return 'Type %s is unknown to to the Uberject typesystem.\nPlease create it using uberclass() or define().' ty.__name__

class Uberject():
    __doc__ = 'Base class for the uberject project'
    __parents__ = []
    __type__ = 'Uberject'

class Ubermethod(Uberject):
    __doc__ = 'Base method class'
    __parents__ = ['Uberject']
    __type__ = 'Ubermethod'
    def __init__(self,function):
        self.function = function
        self.retype = function.retype
        self.patype = function.patype
    def __call__(self, *args):
        for i in range(len(args)):
            if not isuberstance(arg[i],self.parmtypelist[i]):
                raise UberjectTypeError('Typeerror in %s: argument of type %s, should be of type %s' %
                                self.functionname, arg[i].__type__, self.parmtypelist[i])
        result = self.function(*args)
        if not isuberstance(result,self.returntype):
            raise UberjectTypeError('Typeerror in %s: returns %s, should be %s' %
                            self.functionname, result.__type__, self.returntype)
        return result

u = Uberject()

def isuberstance(a, b):
    if a

def uberclass(c):
    if active:
        if type(c).__name__ == 'classobj':
            ### Turn methods into ubermethods
            for item in dir(c):
                #if type(getattr(c,item)).__name__ == 'instancemethod':
                #    setattr(c,item,Ubermethod(getattr(c,item)))
                if callable(getattr(c,item)):
                    setattr(c,item,Ubermethod(getattr(c,item)))

def uberfunction(f):
    if active:
        if callable(f):
            Ubermethod(f)
