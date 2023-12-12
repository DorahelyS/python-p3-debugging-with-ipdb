#We'll cover ipdb, a type of REPL, and discuss how to install and use it to debug a program.

'''
You've already been introduced to REPLs through using the Python Shell. REPL stands for Read, Evaluate, Print, Loop.
It is an interactive programming environment that takes a user's input, evaluates it and returns the result to the 
user.

Python installs with its own REPL, which is the Python shell that you've already been using. Every time you type 
python into your terminal, you're entering into a REPL.

ipdb is another Python REPL with some added functionality. It is built on top of pdb, a REPL in Python's standard 
library, and provides helpful features such as tab completion, syntax highlighting, and better tracebacks. 
When you enter ipdb, you are entering a brand new interactive environment. For any code you want to play with in 
the Python shell, you have to copy and paste or write your code in the Python shell itself. ipdb, on the other hand,
 is like a REPL that you can inject into your program.

ipdb is far more flexible than the Python shell. Once you install the ipdb library (via this lesson's Pipfile), 
you can use ipdb.set_trace() anywhere in your code.

ipdb.set_trace() gives you similar functionality to using debugger in a JavaScript application, in that it 
lets you set a breakpoint in your code that will pause the execution of your program at a certain point so you can 
inspect the variables, functions, and other context available at a specific place in your code.

So when you place the line ipdb.set_trace() in your code, that line will get interpreted at runtime (as your 
program is executed). When the interpreter hits that line, your program will actually freeze and your terminal
will turn into a REPL that exists right in the middle of your program, wherever you added the ipdb.set_trace() line.

At the top of the file, import ipdb is a statement that loads the ipdb library in this file when our application 
runs, very similar to import statements in JavaScript.

After importing ipdb, which you must do to use ipdb


In addition to exploring code inside ipdb, you can also manipulate variables and try code out. This is where ipdb 
really becomes helpful for debugging. If you have a function that isn't doing what it's supposed to do, instead of
 making changes in your text editor and running the tests over and over until you get it working, you can put a 
 binding in your code and try things out. Once you've figured out how to fix the problem, you then update the code 
 in your text editor accordingly.
'''

