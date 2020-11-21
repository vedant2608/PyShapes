class perimeter:
    try:
        def circle(self,_radius):
            '''
            circle(....)
            circle(self,  _radius)
             -> This returns the perimeter.py of circle  (circumference)
             -> accepts one argument: value of radius
            '''
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
            return _a + _b + _c + _d

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

        def reg_polygon(self,_n,_l):
            '''
            reg_polygon(....)
            reg_polygon(self, _n, _l):
             -> This returns the perimeter.py of regular polygon (polygon with equal sides)
             -> accepts no. of sides _n and length _l
            '''
            return _n*_l
        def irreg_polygon(self,*args):
            '''
            irreg_polygon(....)
            irreg_polygon(self,*args);
             -> This returns the perimeter.py of irregular polygon (polygon with unequal sides)
             -> accepts lengths of  sides.  minimum 4 sides can be accepted
            '''
            _c=0
            for each in args:
                _c+=1
            if _c<4:
                print("Function polygon() takes minimum 4 arguments")
                exit()
            else:
                _n = _c
                for i  in args:
                    _n = _n * i
            return _n
    except Exception as e:
        print(e)


