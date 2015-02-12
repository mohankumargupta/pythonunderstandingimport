#PYTHON JARGON
'''
modules, packages
int, float, str, bool
list, tuple, dict
'''


# IMPORTS .... WTF
'''
import someLibraryThing
from something import boo
from something import boo1,boo2,boo3
from something import *
import Rpi.camera as camera
''' 


#---FUNCTIONS (no return value)-------------------------------
'''
def division(numerator, denominator=1):
    print(numerator/denominator)


division(10,2)
division(10)
division(denominator=2, numerator=10)    
'''

#----FUNCTIONS-(return value)-----------------------------
'''
def division(numerator, denominator=1):
    return(numerator/denominator)
'''

'''
answer = division(10,2)
print(answer)
answer = division(10)
print(answer)
answer = division(denominator=2, numerator=10) 
print(answer)
'''

#-----BUILT-IN FUNCTIONS ---------------------------------


# ---type---

'''
type(4)
type(4.5)
type("hello")
type([1,2,3])
type((1,2,3))
type(False)
'''


print(type(4))
print(type(4.5))
print(type("hello"))
print(type([1,2,3]))
print(type((1,2,3)))
print(type(True))
print(type({'mohan':'mohangupta@live.com', 'santa':'santa@northpole.com'}))
print(type({'apple', 'banana', 'orange'}))

'''
def division(numerator, denominator=1):
    return(numerator/denominator)

print(type(division))
'''



#---dir---

#help(dir)
#print(dir("hello world"))
#print("hello world".upper())

#---dir()---

#print(abcd)
#help(print)
#print(dir(__builtins__))
'''
a = 5
def division(numerator, denominator=1):
    return(numerator/denominator)
print(dir())     
'''

#-IMPORT (function definition and invocation)------------------------------
'''
import sendtweet
#print(dir())
#print(dir(sendtweet))
#print(__name__)
#print(sendtweet.__name__)
'''
#-------------------------------------------------------------

#-----------------------IMPORT (fail)-------------------------------------
'''
import sendtweet
sendTwitterUpdateStatus("English is a stolen language")
'''
#-------------------------------------------------------------



#-----------------------IMPORT (works)------------------------------
'''
import sendtweet
sendtweet.sendTwitterUpdateStatus("English is a stolen language")
'''
#-------------------------------------------------------------

#--CALL FUNCTION DIRECTLY WITHOUT MODULE NAME-------------------------------
'''
from sendtweet import sendTwitterUpdateStatus
sendTwitterUpdateStatus("English is a plagiarised language")
'''

#---WHAT ABOUT tweetsent VARIABLE------------------------------------
'''
print("Before import:")
print(dir())
from sendtweet import someJunkText
print("After import:")
print(dir())
print(someJunkText)
print(dir(sendtweet))
'''

#-----BUILT-IN MODULES -----------------------------------

#import sys
#dir(sys)
#print(sys.path)
#print(sys.modules)
#print(sys.builtin_module_names)



#--------------Technical details-------------------
#from python documentation
#https://docs.python.org/3/archives/python-3.4.2-docs-pdf-a4.zip

'''
7.11 The import statement
import_stmt ::= “import” module [”as” name] ( ”,” module [”as” name] )*
| “from” relative_module “import” identifier [”as” name]
( ”,” identifier [”as” name] )*
| “from” relative_module “import” “(” identifier [”as” name]
( ”,” identifier [”as” name] )* [”,”] ”)”
| “from” module “import” “*”
module ::= (identifier ”.”)* identifier
relative_module ::= ”.”* module | ”.”+
name ::= identifier

Examples:
import foo # foo imported and bound locally
import foo.bar.baz # foo.bar.baz imported, foo bound locally
import foo.bar.baz as fbb # foo.bar.baz imported and bound as fbb
from foo.bar import baz # foo.bar.baz imported and bound as baz
from foo import attr # foo imported and foo.attr bound as attr

The basic import statement (no from clause) is executed in two steps:
1. find a module, loading and initializing it if necessary
2. define a name or names in the local namespace for the scope where the import statement occurs.

When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for
each clause, just as though the clauses had been separated out into individiual import statements.

If the requested module is retrieved successfully, it will be made available in the local namespace in one of three
ways:
• If the module name is followed by as, then the name following as is bound directly to the imported module.
• If no other name is specified, and the module being imported is a top level module, the module’s name is
bound in the local namespace as a reference to the imported module
• If the module being imported is not a top level module, then the name of the top level package that contains
the module is bound in the local namespace as a reference to the top level package. The imported module
must be accessed using its full qualified name rather than directly

The from form uses a slightly more complex process:
1. find the module specified in the from clause, loading and initializing it if necessary;
2. for each of the identifiers specified in the import clauses:
(a) check if the imported module has an attribute by that name
(b) if not, attempt to import a submodule with that name and then check the imported module again for
that attribute
(c) if the attribute is not found, ImportError is raised.
(d) otherwise, a reference to that value is stored in the local namespace, using the name in the as clause
if it is present, otherwise using the attribute name

If the list of identifiers is replaced by a star (’*’), all public names defined in the module are bound in the local
namespace for the scope where the import statement occurs.
The public names defined by a module are determined by checking the module’s namespace for a variable named
__all__; if defined, it must be a sequence of strings which are names defined or imported by that module. The
names given in __all__ are all considered public and are required to exist. If __all__ is not defined, the
set of public names includes all names found in the module’s namespace which do not begin with an underscore
character (’_’). __all__ should contain the entire public API. It is intended to avoid accidentally exporting
items that are not part of the API (such as library modules which were imported and used within the module).
The wild card form of import—from module import *—is only allowed at the module level. Attempting
to use it in class or function definitions will raise a SyntaxError.
When specifying what module to import you do not have to specify the absolute name of the module. When a
module or package is contained within another package it is possible to make a relative import within the same top
package without having to mention the package name. By using leading dots in the specified module or package
after from you can specify how high to traverse up the current package hierarchy without specifying exact names.
One leading dot means the current package where the module making the import exists. Two dots means up one
package level. Three dots is up two levels, etc. So if you execute from . import mod from a module
in the pkg package then you will end up importing pkg.mod. If you execute from ..subpkg2 import
mod from within pkg.subpkg1 you will import pkg.subpkg2.mod. The specification for relative imports
is contained within PEP 328.
importlib.import_module() is provided to support applications that determine dynamically the modules to be loaded.

'''

