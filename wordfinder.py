import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    This class reads a file containing a list of words, stores them, and provides methods to access them.

    Args:
        filepath (str): The path to the file containing words.

    Attributes:
        words (list): A list of words read from the file.

    Usage:
     >>> wf = WordFinder(r"C:\\Users\\epris\\OneDrive\\Desktop\\python OOP\\words.txt")
    >>> len(wf.words) == 235886 
    True

    >>> wf.random() in wf.words
    True
    """

    def __init__(self, filepath):
        """Initialize the WordFinder with words from the specified file.

        Args:
            filepath (str): The path to the file containing words.
        """
        self.words = self.read_file(filepath)
        print(f"{len(self.words)} words read")

    def read_file(self, filepath):
        """Read the file and return a list of words.

        Args:
            filepath (str): The path to the file containing words.

        Returns:
            list: A list of words read from the file.
        """
        with open(filepath) as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the list of words.

        Returns:
            str: A random word from the list.
        """
        return random.choice(self.words)

if __name__ == "__main__":
    # When the script is executed, run the doctests
    import doctest
    doctest.testmod()
