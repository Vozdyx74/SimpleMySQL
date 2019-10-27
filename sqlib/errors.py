class SimpleMySQLError(Exception):
    """ Base exception class for SimpleMySQL """

    pass


class AffinityNotFoundError(SimpleMySQLError):
    """ Exception that's thrown when a non-existing MySQL affinity is given. """

    def __init__(self):
        message = 'Given affinity not found. Use the ones from "variables.py"!'
        super(AffinityNotFoundError, self).__init__(message)


class DefaultValueError(SimpleMySQLError):
    """ Exception that's thrown when the default value of a column does not match the affinity. """

    def __init__(self):
        message = 'Default value does not match the affinity of the column.'
        super(DefaultValueError, self).__init__(message)


class DatabaseError(SimpleMySQLError):
    """ Exception that's thrown when an operation is in conflict with the MySQL database. """

    def __init__(self, message):
        super(DatabaseError, self).__init__(message)
