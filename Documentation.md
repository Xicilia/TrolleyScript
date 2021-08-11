
###/////////// **DESCRIPTION** ///////////////

this was my first experience in making "languages"
also i know it isn't a language in the usual sense,i just having fun

###//////////// **SYNTAX** ////////////

basic syntax is simillar to python syntax, because it translates to python for run the code

easiest way to run some code in TrolleyScript is imagine python code and replace keywords

some of this words can be removed or replaced right in TrolleyScript code because this version doesn't have her own lexer

here is all of this (sample is: TrolleyScript keyword - Python keyword):

**епт - end of line keyword, similar to ; in c++ or java**, was created just for fun and as a tribute

мутка - def
запомни - =
базарить - print
если - if
нахуй - : (in function declare or if statement)
это - ==
иначе - else
поясни - input()
отдыхай - pass
по_понятиям - True
не_по_понятиям - False
похуй - end of statement

###///////////// **A LITTLE BIT MORE ABOUT LANGUAGE NUANCES AND OTHER THINGS** ///////////////


The source file must be **ANSI encoded .txt file** (I only tested with UTF-8 and ANSI), UTF-8 doesn't work and I see no reason to fix it if it's just a preview version.

**space for every construction!!!** in case that this version have no lexer (and in case of really simple parser) you need to put a space in every other construction

example in TrolleyScript: 
  базарить('you will not see this text') - error 
  базарить ('you will see this text') - will work because have space between keyword and argument section 
  etc.
  
 __a little more about 'похуй' keyword__ in python you dont need to declare an end of any statement...but! TrolleyScript isn't python!
 in every statement that needs to be tabulated you need to put 'похуй' keyword to declare an end of statement
 
 example in TrolleyScript:
  
  мутка myFunc() нахуй
    базарить ('hello world!')
  похуй
  
  similar to
  
  def myFunc():
    print('hello world!')
   
   in python.

also TrolleyScript does not support spaces in Strings and you need to use _ or deal with it

after you read this you will become a professional TrolleyBus driver!





