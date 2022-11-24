def read_file_list(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(f"- {line}")


# What I had.  Printed correctly but did not access file
    def read_file_list(filename):
        file =  open(filename, 'r')
        list_items = (file.readlines())
        for element in list_items:
            print('-',element)



    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!