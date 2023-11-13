#!/usr/bin/python3
'''
This class inherits from class Rectangle
'''

from models.rectangle import Rectangle
'''
Importing square from square
'''


class Square(Rectangle):
    '''
    inheritance square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Args:
            id of the class
            size - size of the square
            x - coordinate of square
            y - coordinate of square
        '''
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Getter for size

        Return:
            size of rectangle
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Setter for size

        Args:
            size width and height of rectangle

        Return:
            size of rectangle
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        Returns:
            printout of '[Square] (<id>) <x>/<y>'
        '''
        return('[Square] ({}) {}/{} - {}'.format(
                self.id,
                self.x,
                self.y,
                self.width))

    def update(self, *args, **kwargs):
        '''
        Args:
            args takes in non key word arguments
            kwargs takes in kew word items
        '''
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs is not None and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''
        Returns:
            returns the dictionary representation of a Rectangle
        '''
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
