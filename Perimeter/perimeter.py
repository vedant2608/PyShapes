class perimeter:
    try:
        def parallelogram(self, _base, _height):
            '''
            parallelogram(....)
            parallelogram(self,_base,_height)
             -> This returns the perimeter.py of parallelogram
             -> accepts the two arguments:value of base and value of height
            '''
            return 2 * (_base + _height)

        def triangle(self, _a=1, _b=1, _c=1, n=0):
            '''
            triangle(....)
            triangle(self,_a,_b,_c)
             -> This returns the perimeter.py of parallelogram
             -> accepts the three arguments:values of three sides
            '''
            return _a + _b + _c

        def rectangle(self, _length, _width):
            '''
            rectangle(....)
            rectangle(self,_length,_width)
             -> This returns the perimeter.py of rectangle
             -> accepts the two arguments:values of length and width
            '''
            return 2 * (_length + _width)

        def square(self, _side):
            '''
            square(....)
            square(self,_side)
             -> This returns the perimeter.py of square
             -> accepts an argument: value of side
            '''
            return 4 * _side

        def trapezoid(self, _a, _b, _c, _d):
            '''
            trapezoid(....)
            trapezoid(self,_a,_b,_c,_d):
             -> This returns the perimeter.py of trapezoid
             -> accepts the four arguments:values of its four sides
            '''
            return _a + _b + _c

        def kite(self, _a, _b):
            '''
            kite(....)
            kite(self,_a,_b):
             -> This returns the perimeter.py of kite
             -> accepts the two arguments:values of four sides
            '''
            return 2 * (_a + _b)

        def rhombus(self, _a):
            '''
            rhombus(....)
            rhombus(self,_a):
             -> This returns the perimeter.py of rhombus
             -> accepts an argument:value of a side
            '''
            return 4 * _a

        def hexagon(self, _a):
            '''
            hexagon(....)
            hexagon(self,_a):
             -> This returns the perimeter.py of hexagon
             -> accepts an argument:value of a side
            '''
            return 6 * _a

        def polygon(self, _n, _l):
            '''
            polygon(....)
            rectangle(self,_n,_l):
             -> This returns the perimeter.py of polygon
             -> accepts the two arguments:number of sides and length of a side
            '''
            return _n * _l
    except Exception as e:
        print(e)

