
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
'''

'''
print(type(4));
print(type(4.5));
print(type("hello"));
print(type([1,2,3]));
print(type((1,2,3)));
'''

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