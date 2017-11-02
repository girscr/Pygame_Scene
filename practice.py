import math

def discriminate(a, b, c):
    """returns the discriminate of a quadratic function
        with coefficients a, b, c, of the form 
    
        a*x^2 + b*x +c = 0
    """
    disc = b**2 - 4*a*c

    return (disc)

def quad_roots(co_1, co_2, co_3):
    """returns the real roots of a quadratic function
        with coefficients co_1, co_2, co_3, of the form 

            co_1*x^2 + co_2*x + co_3 = 0
    """

    #getting the discriminate
    the_discrim = discriminate(co_1, co_2, co_3)

    #finding the roots
    root1 = (-co_2 + math.sqrt(the_discrim)) / (2 * co_1)
    root2 = (-co_2 - math.sqrt(the_discrim)) / (2 * co_1)

    return root1, root2

def get_roots():
    """displays the real roots of a quadratic function 
    using coefficients from user input"""

    #quad_co, lin_co, constant = float(input('Enter the coefficients of your quadratic: '))
    quad_co, lin_co, constant = 1, 2, 1

    #get the discrimnate for the input values
    discrim = discriminate(quad_co, lin_co, constant)

    if discrim < 0:
        print ('There are no real solutions')
    else:
        ans1, ans2 = quad_roots(quad_co, lin_co, constant)
        if discrim == 0:
            print ('There is one real solution: x = %.3f'%ans1)
        else:
            print('There are two real solutions:\n x = %.3f, x = %.3f' % (ans1, ans2))


get_roots()
