class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row = row
        self.column = column


    def __str__(self):
        """Return a string representation.

        @rtype: str

        >>> loc = Location(4, 5)
        >>> print(loc)
        Row: 4, Column: 5
        """
        return ("Row: {}, Column: {}").format(self.row, self.column)


    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool

        >>> loc1 = Location(2, 5)
        >>> loc2 = Location(3, 5)
        >>> loc3 = Location(2, 5)
        >>> loc1 == loc2
        False
        >>> loc1 == loc3
        True
        """
        return (type(self) == type(other) and (self.row, self.column) == (other.row, other.column))



def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int

    >>> m1 = Location(2, 3)
    >>> m2 = Location(3, 5)
    >>> manhattan_distance(m1, m2)
    13
    """
    return(origin.row + origin.column + destination.row + destination.column)

def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    """
    location_str =
    return Location()



