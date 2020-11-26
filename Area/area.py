import math
try:
    def circle(_radius):
        '''
        circle(....)
        circle(_radius)
            -> This returns the area of circle
            -> accepts one argument: value of radius
        '''
        return (3.14* _radius* _radius)


    def parallelogram(_base, _height):
            '''
            parallelogram(....)
            parallelogram(_base,_height)
                -> This returns the area of parallelogram
                -> accepts the two arguments:value of base and value of height
            '''
            return (_base * _height)


    def triangle(type, *keyargs):
        '''
        triangle(....)
        triangle(type, *keyargs)
            Area of triangles
            -> type 1: returns area of equilateral triangle 
            Parameters: (type, side)
            -> type 2: returns area of isosceles triangle
            Parameters: (type, base, height)
            -> type 3: returns area of scalene triangle
            Parameters: (type, base, height)
        '''
        if type == 1:
            for i in keyargs:
                return(0.43301 * i)        
        elif type == 2 or type == 3:
            temp = 1
            for i in keyargs:
                temp = temp * i
            return (0.5 * temp)
            
    def rectangle(_length, _width):
            '''
            rectangle(....)
            rectangle(_length,_width)
                -> This returns the area of rectangle
                -> accepts the two arguments:values of length and width
            '''
            return (_length * _width)

    def square(_side):
            '''
            square(....)
            square(_side)
                -> This returns the area of square
                -> accepts an argument: value of side
            '''
            return _side *  _side

    def trapezoid(_a, _b, _h):
            '''
            trapezoid(....)
            trapezoid(_a,_b,_h):
                -> This returns the area of trapezoid
                -> accepts three arguments:values of its two sides and height
            '''
            return ((_a + _b)/2) * _h

    def kite(_a, _b):
            '''
            kite(....)
            kite(_a,_b):
                -> This returns the area of kite
                -> accepts the two arguments:values of two diagonals
            '''
            return (_a * _b)/2

    def rhombus(_a, _b):
            '''
            rhombus(....)
            rhombus(_a):
                -> This returns the area of rhombus
                -> accepts an argument:values of two diagonals
            '''
            return (_a * _b)/2

    def polygon(_n,_r,_l):
        '''
        polygon(....)
        polygon(_n,_r_l):
        -> This returns the area of regular polygon
        -> accepts three arguments:number of sides, length of circumradius, length of a side
        '''
        a = _r*(math.cos(3.14/_n))
        p = _n*_l
        return (1/2 * a * p)


except Exception as e:
    print(e)

