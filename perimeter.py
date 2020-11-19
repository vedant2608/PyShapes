try:
    def parallelogram(_base, _height):
        '''
        parallelogram(....)
        parallelogram(_base,_height)
            -> This returns the perimeter of parallelogram
            -> accepts the two arguments:value of base and value of height
        '''
        return 2 * (_base + _height)

    def triangle(_a=1, _b=1, _c=1, n=0):
        '''
        triangle(....)
        triangle(_a,_b,_c)
            -> This returns the perimeter of parallelogram
            -> accepts the three arguments:values of three sides
        '''
        return _a + _b + _c

    def rectangle(_length, _width):
        '''
        rectangle(....)
        rectangle(_length,_width)
            -> This returns the perimeter of rectangle
            -> accepts the two arguments:values of length and width
        '''
        return 2 * (_length + _width)

    def square(_side):
        '''
        square(....)
        square(_side)
            -> This returns the perimeter of square
            -> accepts an argument: value of side
        '''
        return 4 * _side

    def trapezoid(_a, _b, _c, _d):
        '''
        trapezoid(....)
        trapezoid(_a,_b,_c,_d):
            -> This returns the perimeter of trapezoid
            -> accepts the four arguments:values of its four sides
        '''
        return _a + _b + _c

    def kite(_a, _b):
        '''
        kite(....)
        kite(_a,_b):
            -> This returns the perimeter of kite
            -> accepts the two arguments:values of four sides
        '''
        return 2 * (_a + _b)

    def rhombus(_a):
        '''
        rhombus(....)
        rhombus(_a):
            -> This returns the perimeter of rhombus
            -> accepts an argument:value of a side
        '''
        return 4 * _a

    def hexagon(_a):
        '''
        hexagon(....)
        hexagon(_a):
            -> This returns the perimeter of hexagon
            -> accepts an argument:value of a side
        '''
        return 6 * _a

    def regularPolygon(_n, _l):
        '''
        polygon(....)
        rectangle(_n,_l):
            -> This returns the perimeter of polygon
            -> accepts the two arguments:number of sides and length of a side
        '''
        return _n * _l
    def irregularPolygon(args=4, **keyargs):
        if(len(keyargs)<4):
            raise Exception("Polygon atleast have 4 sides")
        a = keyargs.values()
        return sum(a)
except Exception as e:
    print(e)
