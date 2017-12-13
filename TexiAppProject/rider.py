"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """Initializes and presents the current status of the Rider in three different status

    Status WAITING is given for waiting rider
    Status CANCELLED is given to cancelled rider
    Status SATISFIED is given to satisfied rider
    """
    def __init__(self, status, origin, destination, ):
        """Initializes a status, origin, and the destination to a rider

         @type self: Rider
         @rtype: None
        """
        self.status = status
        self.origin_row, origin_column = origin_row_row, origin_column
        self.destination_row, destination_column = destination_row, destination_column

    def __str__(self):
        """Return a string representation.

        @rtype: str

        >>> r1 = Rider(WAITING, )
        >>> print(r1)
        "Current Rider Status: waiting"
        """
        return("Current Rider Status: {}, Rider Origin: {},{}, Rider Destination: {},{}").format(self.status,
                                                                                                 self.origin_row,
                                                                                                 self.origin_column,
                                                                                                 self.destination_row,
                                                                                                 self.destination_column)

    def __eq__(self, other):
        """Return True if self equals other, and False otherwise

        @rtype: bool

        >>> r1 = Rider(WAITING)
        >>> r2 = Rider(SATISFIED)
        >>> r3 = Rider(WAITING)
        >>> r1 == r2
        False
        >>> r1 == r3
        True
        """
        return (type(self) == type(other) and type(self.status, self.origin_row, self.origin_column, self.destination_row, self.destination_column)
                == type(other.status, other.origin_row, other.origin_column, other.destination_row, other.destination_column))







