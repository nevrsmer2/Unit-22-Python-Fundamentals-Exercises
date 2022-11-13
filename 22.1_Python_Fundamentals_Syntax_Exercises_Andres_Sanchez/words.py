
#  This for loop prints each word in the list on a separate line
words = ["hello", "hey", "goodbye", "yo", "yes"]

for word in words:
  print(word)



# Converts all words in the list to uppercase
words = ["hello", "hey", "goodbye", "yo", "yes"]

converted_list = [word.upper() for word in words]
for word in converted_list:
    print(word)



# Function to convert words in a list to uppercase

def print_upper_words(list):
  """This function accepts an list of strings and converts all the letters of each string into capital letters and prints each string on a separate line"""
  converted_list = [word.upper() for word in list]
  for word in converted_list:
    print(word)

  print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "kitties"])



def print_first_letter(list):
  """Prints every string in the list that starts with "e" or "E" on a separate line"""
  for word in list:
    if word[0] == "e" or word[0] == "E":
      print(word)

print_first_letter(["hello", "hey", "goodbye", "yo", "yes", "every", "Edward"])



def print_first_letter_2(list, char):
  """Prints every string in the list that starts with the letter that is the value of the argument char on a separate line"""
  lower_case = [word.lower() for word in list]
  lower_char = char.lower()

  for word in lower_case:
    if word[0] == lower_char:
      print(word)

print_first_letter_2(["hello", "hey", "goodbye", "yo", "yes", "Yep", "every", "Edward"], "Y")
    


