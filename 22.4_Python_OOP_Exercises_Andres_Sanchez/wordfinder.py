import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        '''Opens files based on path, parses the file contents, indicates number of words that are read'''
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        '''Strips items of  leding and tralling spaces'''
        return [word.strip() for word in file]

    def random(self):
        '''Returns a random word from the file'''
        return random.choice(self.words)

# Wrote this function that works.  Had Trouble incorporating it into a class.

    # def read_random_line(file_name):
    #     file = open(file_name, 'r')
    #     lines = file.readlines()
    #     length = len(lines)
    #     rand_line = random.randint(0, length -1)
    #     print(lines[rand_line])
    #     file.close()

"--------------------------------------------"
    # Create child class that inherits methods from parent and has new functionality added

class SpecialWordFinder(WordFinder):
    '''Child class to add funcionality to omit comments and blank lines.  There are 4 words iin file

    >>> swf.random() in ["kale", 'parsnips', 'apple', 'mango']
    True

 >>> swf.random() in ["kale", 'parsnips', 'apple', 'mango']
    True
     >>> swf.random() in ["kale", 'parsnips', 'apple', 'mango']
    True
     >>> swf.random() in ["kale", 'parsnips', 'apple', 'mango']
    True
     >>> swf.random() in ["kale", 'parsnips', 'apple', 'mango']
    True

    >>> swf.random() in ['#', ' ', '#Veggies', '#Fruits', '#Fruits are good for you1']
    False (These are the elements that have been removed from file)

'''

    def parse(self, file):
         '''Parses items in file and skips lines that are blank or that have comments'''
         return [word.strip() for word in file if word.strip() and not word.startswith('#')]
        
               