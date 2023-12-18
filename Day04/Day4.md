
* Randomisation
* Error Handling

### Project

1. Who will pay the bill
2. Heades or tails
3. Tresure mape
4. List
5. Random 
6. Final_project (Rock paper scissors Game)

Syntax Error
Syntax errors happen when our code
does not make any sense to the computer.
This can happen because we've misspelt
something or there's too many brackets or
a missing comma.

Name Error

This happens when there is a variable
with a name that the computer
does not recognise. It's usually because
we've misspelt the name of a variable
we created earlier.

Note: variable names are case sensitive!

Zero Division Error
This happens when we try to divide by zero,
This is something that is mathematically
impossible so Python will also complain.

Adding an Item to a List
If we just want to add a single item to a
list, we need to use the .append() method.


List Index
To get hold of a particular item from a
list we can use its index number.
This number can also be negative, if we
want to start counting from the end of the
list

Adding Lists Together
We can extend a list with another list by
using the extend keyword, or the + symbol.

List Slicing
Using the list index and the colon symbol
we can slice up a list to get only the
portion you want.
Start is included, but end is not.

Randomisation
The random functions come from the
random module which needs to be
imported.
In this case, the start and end are both
included
start <= randint <= end

Importing
Some modules are pre-installed with python
e.g. random/datetime
Other modules need to be installed from
pypi.org

Importing from modules
We can import a specific thing from a
module. e.g. a function/class/constant
We do this with the from keyword.
It can save you from having to type the same

from random import randint
n = randint(1, 5)