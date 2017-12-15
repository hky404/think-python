"""
* Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

* Write a function that draws a similar grid with four rows and four columns.

"""


def print_grid():
    """grid with four rows and four columns
    """

    def print_vertical():
        print('|         |         |         |         |')
        print('|         |         |         |         |')
        print('|         |         |         |         |')
        print('|         |         |         |         |')

    def print_horizontal():
        print('+ - - - - + - - - - + - - - - + - - - - +')

    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()

print_grid()
