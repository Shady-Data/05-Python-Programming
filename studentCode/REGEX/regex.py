# Regular Expressions or RegEx

import re

text_to_match = '''lol lololol
Daniel 1234 abcd 
this.thing@email.com
    \tthis_other-thing@email.com
210-444-4444
512*888*8888

800-444-4444
900-123-4567
cat mat hat bat

Mr. Anderson
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# print(r'\tTab')

# compile() will allow us to seperate our pattern matches into a variable
# that makes it easier to reuse our variable

# pattern = re.compile(r'1234')


# match()
# determines if the regex matches at the beginning of the string
# returns None if its not at beginning, same as ^ anchor

# match = pattern.match(text_to_match)
# print(match)

# search() lets us search the entire string
# pattern = re.compile(r'1234')
# searched_item = pattern.search(text_to_match)
# print(searched_item)

# finditer()
# pattern = re.compile(r'abcd')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# ************* META CHARACTERS *************

# . - Any character except newline '\n'
# pattern = re.compile(r'.')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \ - Escape character to grab special characters
# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \d - matches any digit from 0-9
# pattern = re.compile(r'\d')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \D - matches any non-digit
# capitals essentially negate
# pattern = re.compile(r'\D')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \w - matches any word character (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\w')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \W - matches any non-word character
# pattern = re.compile(r'\W')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \s - matches any whitespace character (tab, space, newline)
# pattern = re.compile(r'\s')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \S - matches any non-whitespace character
# pattern = re.compile(r'\S')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# ************* ANCHORS *************
# Anchors don't match chars, they match invisible positions before or after chars

# \b - matches word boundaries
# anything prefixed with start of a newline, start of a string, spaces, tabs
# pattern = re.compile(r'\blol')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# \B - matches non-word boundaries
# pattern = re.compile(r'\Blol')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# ^ - finds matches at the beginning of a string
# pattern = re.compile(r'^lol')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# $ - finds matches at the end of a string
# pattern = re.compile(r'com$')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# pattern = re.compile(r'\d\d\d')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# [] - Character set, used to search for a single character from a group of characters

# pattern = re.compile(r'[89]00[-*]\d\d\d[-*]\d\d\d\d')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# Find a range of values using[-]

# pattern = re.compile(r'[a-d]')
# pattern = re.compile(r'[a-dA-D]')
# pattern = re.compile(r'[1-7]')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# [^] - carrot in a set negates what you're looking for
# pattern = re.compile(r'[^1-7]')
# pattern = re.compile(r'[^a-zA-Z]')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# match cat, mat, hat but not bat
# pattern = re.compile(r'[^b]at')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# {n, m} - finds the preceding character/set at least n times, but not more than m times (m is optional '{n}' = exactly n times)
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'(\d{3}.){3}')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# ? - finds the preceding character/set 0 or 1 times
# pattern = re.compile(r'Mr\.')
# pattern = re.compile(r'Mr\.?')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# + - finds the preceding character/set 1 or more times
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# * - finds the preceding character/set 0 or more times
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# () - groups allow us to match several different patterns
# Here we can match an 'M' then an 'r' or 's' or 'rs'
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_match)

# for match in matches:
#     print(match)

# find emails
emails = '''
TestUser@gmail.com
test.user@school.edu
test-123-user@this-place.net
bademail@.com
'''

# Matches TestUser@gmail.com
# pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# match the other two emails
# pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# match the third email
# pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# match emails
# pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]+')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# GROUPS
urls = '''
http://testsite.com
https://www.google.com
https://youtube.com
https://www.nasa.gov
'''
# pattern = re.compile(r'http')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)

# pattern = re.compile(r'https?://(www\.)?')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)

# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)

# we can group all of these to grab groups
# group 0 being all groups, then group 1 being the first group...etc
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0, 1, 2, 3))

# substitute out groups 2 and 3 for our rurls everytime it finds a match
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# findall() - returns matches as a list of strings
# If there are no groups it returns a list of strings
# If there is one group it returns tahe group as a list of strings
# If there are more than one group, it returns a list of tuples

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?(\s[A-Z]\w*)')
# matches = pattern.findall(text_to_match)

# for match in matches:
#     print(match)

# pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]+')
# matches = pattern.findall(emails)

# for match in matches:
#     print(match)

# flags
string = "I cAan TyPeE GoOd"
# pattern = re.compile(r'[aAOo]')
# pattern = re.compile(r'[ao]', re.IGNORECASE)
pattern = re.compile(r'[ao]', re.I)
matches = pattern.findall(string)

for match in matches:
    print(match)