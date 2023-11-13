#!/usr/bin/python3
'''
This is an inheritance class rectangles
'''


from models.base import Base
'''
importing class Base(superclass)
'''


class Rectangle(Base):
    '''
    inheritance class rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        class constructor for Rectangle

        Args:
            witdth: length of a rectangle
            height: length of a rectangle
            y input
            x input

        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0

        Returns:
            id or id of __nb_objects
        '''
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        '''
        Getter for width

        Return:
            width of rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for width

        Args:
            width of rectangle

        Return:
            width of rectangle
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        '''
        Getter for height

        Return:
            height of rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for height

        Args:
            height of rectangle

        Return:
            height of rectangle
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        '''
        Getter for x

        Return:
            x coordinate = value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for x

        Args:
            x coordinate

        Return:
            x coordinate = value
        '''
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        '''
        Getter for y

        Return:
            y coordinate
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for y

        Return:
            y coordinate = value
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        '''
        Return:
            The area of height and width
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Return:
            prints the Rectangle instance with the character #
        '''
        [print() for i in range(self.y)]
        for j in range(self.height):
            [print(' ', end="") for k in range(self.x)]
            [print('#', end="") for m in range(self.width)]
            print('')

    def __str__(self):
        '''
        Returns:
            printout of '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        '''
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
        ))

    def update(self, *args, **kwargs):
        '''
        Args:
            args takes in non key word arguments
            kwargs takes in kew word items
        '''
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == 'width':
                    self.width = val
                elif key == 'height':
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        '''
        Returns:
             returns the dictionary representation of a Rectangle
        '''
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
