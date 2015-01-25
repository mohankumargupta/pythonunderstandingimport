
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


answer = division(10,2)
print(answer)
answer = division(10)
print(answer)
answer = division(denominator=2, numerator=10) 
print(answer)
'''

#-----BUILT-IN FUNCTIONS ---------------------------------

#type
'''
type(4);
type(4.5);
type("hello");
type([1,2,3]);
type((1,2,3));
'''

print(type(4));
print(type(4.5));
print(type("hello"));
print(type([1,2,3]));
print(type((1,2,3)));

#dir

#dir()
#dir(4.5)
#help((4.0).is_integer)
#type("hello world")
#dir("hello world")
#"hello world".upper()
#type(print)



#-IMPORT (function definition and invocation)------------------------------
'''
import sendtweet
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
from sendtweet import sendtweet
sendTwitterUpdateStatus("English is a plagiarised language")
'''

#---WHAT ABOUT tweetsent VARIABLE------------------------------------
'''
from sendtweet import tweetsent
print(dir())
print(tweetsent)
print(sendtweet)
'''

#-----BUILT-IN MODULES -----------------------------------

#import sys
#dir(sys)
#print(sys.path)
#print(sys.modules)
#print(sys.builtin_module_names)