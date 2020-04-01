import math


def is_inside_triangle(x1,y1,x2,y2,x3,y3,m,n):
    area = area_of_triangle(x1,y1,x2,y2,x3,y3)
    area_1 = area_of_triangle(m,n,x2,y2,x3,y3)
    area_2 = area_of_triangle(m, n, x1, y1, x3, y3)
    area_3 = area_of_triangle(m, n, x1, y1, x2, y2)
    if area == area_1+area_2+area_3:
        print('({},{}) is inside the Triangle'.format(m,n))
    else:
        print('({},{}) is outside the Triangle'.format(m,n))


def area_of_triangle(x1,y1,x2,y2,x3,y3):
    return abs(x1 * (y2-y3)+x2*(y1-y3)+x3*(y1-y2))/2.0


def is_inside_circle(r, x, y):
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


def take_circle_inputs():
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
    is_inside_circle(r, x, y)


def take_triangle_inputs():
    x1, y1 = map(int, input('Enter the Triangle\'s 1st Coordinates: ').split(' '))
    x2, y2 = map(int, input('Enter the Triangle\'s 2nd Coordinates: ').split(' '))
    x3, y3 = map(int, input('Enter the Triangle\'s 3rd Coordinates: ').split(' '))
    m,n = map(int, input('Enter the Coordinates of point to verify : ').split(' '))
    is_inside_triangle(x1, y1, x2, y2, x3, y3, m, n)

def menu():
    choice = int(input('''Program to check Co-ordinates inside/outside 2D Shapes\n1.Circle?\n2.Triangle\nEnter your choice: '''))
    r = 0
    if choice==1:
        take_circle_inputs()
    elif choice==2:
        take_triangle_inputs()
    else:
        print('Wrong Choice')
        exit(0)