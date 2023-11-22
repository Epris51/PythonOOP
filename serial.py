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

    def __init__(self, start):
        """Initialize the serial generator with a start number."""
        self.start = start
        self.current = start

    def generate(self):
        """Generate the next serial number."""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Reset the serial number to its original start value."""
        self.current = self.start


