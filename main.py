"""
Maths Challenge Runner

    * * * 
      * * x
---------
  * * * *
* * * * 0
---------
* * * * *

All * digits must be one of only 2, 3, 5 or 7

For the multiplication we use the variables


   a b c
     d e 
--------

"""

def main():
    """
    Go through all combinations of a, b, c, d and e until we get an answer
    """
    for a in (2, 3, 5, 7):
        for b in (2, 3, 5, 7):
            for c in (2, 3, 5, 7):
                for d in (2, 3, 5, 7):
                    for e in (2, 3, 5, 7):
                        if check(a, b, c, d, e):
                            show(a, b, c, d, e)

def check(a, b, c, d, e):
    """
    work out if all numbers are 2, 3, 5 or 7
    """
    first_row = (a * 100 + b * 10 + c) * e
    if not all_good(first_row):
        return False
    second_row = (a * 100 + b * 10 + c) * d * 10
    if not all_good(second_row // 10):
        return False
    third_row = first_row + second_row
    return all_good(third_row)

def all_good(number):
    """
    Check all digits are either 2, 3, 5 or 7
    """
    return all(char in '2357' for char in str(number))

def show(a, b, c, d, e):
    first_row = (a * 100 + b * 10 + c) * e
    second_row = (a * 100 + b * 10 + c) * d * 10
    third_row = first_row + second_row
    print("""\

   %s %s %s
     %s %s x
-----------
%s
%s
-----------
%s
""" % (a, b, c, d, e, first_row, second_row, third_row))

if __name__ == '__main__':
    main()
                


