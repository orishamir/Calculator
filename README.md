# Calculator

## Parser.py
This is a stand-alone file that you can use.   
   
However, if you want OOP that resembles the true structure of a tree,   
you would want **ParserWithTree.py**, **CalculationTree.py** and additionally **Visualizer.py**

### Node.py
That is the file that contains the OOP stuff.   
Node is defined there.

### ParserOOP.py
Its the same as Parser.py, but instead of calculating in-place, it creates Nodes.   
The Node class has `evaluate()` method that calculates it's value.

### Visualizer.py
Used to visualize the expression tree. (Turtle)


## parserJS.js
There is the same thing but in JavaScript.