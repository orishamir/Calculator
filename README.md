# Calculator
This is a kind of recursive calculator with trig, diff, (definite) integrating, sigma, log and stuff. (inside CalculatorExtended.py)

## SearchFuncs.py
Implements logic of how to search for operators.   
For example in the expression "12*5+3" we'd like our calculator to   
use basic order of operations, so SearchFuncs should return the right   
operator (addition, subtraction, multiplication, ...) to start with and calculate.

## Parser.py 
Is like ExtendedCalculator but without the extended functions... it just  
has +-*/ and ^ just to understand the concept.   
I'd recommend looking at **earchFuncs.py* as basically every file uses it to calculate...


## ParserOOP.py and Node.py
Is a basic calculator, but really implements the OOP-aspect of the calculator.    
Since a mathematical expression can be perfectly represented as a binary tree.
