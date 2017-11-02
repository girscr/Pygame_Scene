import math


def distance (x1, y1, x2, y2):
    '''calculates the distance between the
    two points given'''

    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist

def in_circle(center_x, center_y, radius, other_x, other_y):
    '''determines whether a given point lies 
    within the circle'''

    #get the distance between the center and given point
    new_dist = distance(center_x, center_y, other_x, other_y)

    #compare the distance with the radius
    if new_dist > radius:
        print ('The given point is outside the circle')
    elif new_dist == radius:
        print ('The given point is on the circle')
    else:
        print('The given point is inside the circle')
