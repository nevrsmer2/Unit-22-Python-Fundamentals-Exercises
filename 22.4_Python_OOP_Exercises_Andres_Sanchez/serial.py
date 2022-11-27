"""Python serial number generator."""

class SerialGenerator:
    
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        '''Creates a new serial number generator that starts from the value of start'''
        self.start = self.next = start

    def __rpr__(self):
        '''To show representation'''
        return f"SerialGenerator start = {self.start} next = {self.next}"

    def generate(self):
        ''''Return next number in sequence of serial humbers'''
        self.next += 1
        return self.next -1

    def reset(self):
        '''Reset number to original value of  start argument'''
        self.next = self.start