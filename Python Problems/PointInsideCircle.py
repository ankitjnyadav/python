import math


def verify_point_inside(r,x,y):
    r2 = r**2
    x2 = x**2
    y2 = y**2
    if x2+y2 == r2:
        print('Point is on the Cicle')
    elif x2+y2 < r2:
        print('Point is inside the Cicle')
    elif x2+y2 > r2:
        print('Point is outside the Cicle')
def find_radius(m,n,x,y):
    r2 = (x-m)**2 + (n-y)**2
    return math.sqrt(r2)

def take_inputs():
    choice = int(input('''You have\n1. Radius of Circle?\n2.Coordinates of Cicle's center?\nEnter your choice (1 or 2) : '''))
    r = 0
    if choice==1:
        r= int(input('Enter the radius of circle: '))
        x, y = map(int, input('Enter the Coordinates: ').split(' '))
    elif choice==2:
        m,n = map(int, input('Enter Cicle\'s centers coordinates: ').split(' '))
        x, y = map(int, input('Enter the Coordinates: ').split(' '))
        r = find_radius(m,n,x,y)
    else:
        print('Wrong Choice')
        exit(0)
    verify_point_inside(r, x, y)