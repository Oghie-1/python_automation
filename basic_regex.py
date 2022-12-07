"""The check_web_address function checks if the text passed qualifies as a top-level web 
    address, meaning that it contains alphanumeric characters(which includes letters, 
    numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period 
    and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular 
    expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and 
    end-of-line characters, and character classes. """

import re


def check_web_address(text):
  pattern = r"^\S+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


''' The check_time function checks for the time format of a 12-hour clock, as follows: the hour is 
    between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, 
    then an optional space, and then AM or PM, in upper or lower case. 
    Fill in the regular expression to do that. How many of the concepts that you just learned 
    can you use here? '''


def check_time(text):
  pattern = r'[0-2]*:[00-59]'
  result = re.search(pattern, text)
  return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False

''' The contains_acronym function checks the text for the presence of 2 or more characters
  or digits surrounded by parentheses, with at least the first character in uppercase 
  (if it's a letter), returning True if the condition is met, or False otherwise. For example,
  "Instant messaging (IM) is a set of communication technologies used for text-based communication" 
  should return True since (IM) satisfies the match conditions." Fill in the regular expression in 
  this function: '''

''' We're working with a CSV file, which contains employee information. Each record has a name field,
   followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, 
   and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the
    regular expression, using groups, to use the transform_record function to do that. '''


def transform_record(record):
  new_record = re.sub(r",([\d-]+)", r",+1-\1", record)
  return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

'''The multi_vowel_words function returns all words with 3 or more consecutive vowels(a, e, i, o, u).
  Fill in the regular expression to do that. '''


def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3}\w*\b"
  result = re.findall(pattern, text)
  return result


print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words(
    "The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

''' The transform_comments function converts comments in a Python script into those usable 
  by a C compiler. This means looking for text that begins with a hash mark (#) and replacing 
  it with double slashes (//), which is the C single-line comment indicator. For the purpose of 
  this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command,
  and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks 
  (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#).
  Fill in the parameters of the substitution method to complete this function: '''


def transform_comments(line_of_code):
  result = re.sub(r'##*', r'//', line_of_code)
  return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

''' The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX 
  (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it 
  to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to 
  complete this function. '''


def convert_phone_number(phone):
  result = re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', phone)
  return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))


# (?<!\S) - a left-hand whitespace boundary
# (\d{3}) - Capturing group  # 1: three digits
# - - a hyphen.
