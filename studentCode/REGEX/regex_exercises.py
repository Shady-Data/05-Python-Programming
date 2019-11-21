import re

"""
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
"""

# strings = '''
# bat
# bit
# but
# hat
# hit
# hut
# mit
# mat
# nut
# '''
# pattern = re.compile(r'[bh][aiu]t')
# matches = pattern.findall(strings)
# for match in matches:
#     print(match)

"""​
2. Match any pair of words separated by a single space, that is,
first and last names.
"""

# names = '''
# Bat Batterson
# Bit Byte
# But No
# Hat Hatter
# Hit Runner
# Hut Hitchcock
# Mit Mat
# '''
# pattern = re.compile(r'\w+\s\w+')
# matches = pattern.findall(names)
# for match in matches:
#     print(match)

"""
3. Match any word and single letter separated by a comma and
single space, as in last name, first initial.
"""

# names = '''
# Batterson, B
# Byte, B
# No, B
# Hatter, H
# Runner, H
# Hitchcock, H
# Mit Mat
# '''
# pattern = re.compile(r'\w+,\s\w+')
# matches = pattern.findall(names)
# for match in matches:
#     print(match)

"""
4. Match the set of all valid Python identifiers.
​"""

"""
5. Match a street address according to your local format (keep
your regex general enough to match any number of street
words, including the type designation). For example, American
street addresses use the format: 1180 Bordeaux Drive. Make
your regex flexible enough to support multi-word street
names such as: 3120 De la Cruz Boulevard.
​"""

# streets = '''
# 2048 Batterson blvd
# 64 Bit Dr
# 1920 No lane
# 1440 Hatter loop
# 1660 N Runner circle
# 5140 SE Hitchcock St
# 1200 MitMat Dr
# 1180 Bordeaux Drive
# 3120 De la Cruz Boulevard
# '''
# pattern = re.compile(r'(\d+)\s([NSWE]{1,2})?(\s?(\b\w+))+')
# matches = pattern.finditer(streets)
# for match in matches:
#     print(match.group(0))

"""
6. Match simple Web domain names that begin with “www.”
and end with a “.com” suffix; for example, www.yahoo.com.
Extra Credit: If your regex also supports other high-level
domain names, such as .edu, .net, etc. (for example,
www.foothill.edu).
​"""

# urls = '''
# www.yahoo.com
# www.foothill.edu
# www.google.com
# youtube.com
# yahoo.com
# '''

# pattern = re.compile(r'(w{3}\.)(\w+)\.(com|net|edu|org|mil|gov|)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(0))

"""
7. Match the set of all valid e-mail addresses (start with a loose
regex, and then try to tighten it as much as you can, yet
maintain correct functionality). Try to break what we did in class 
and improve it.
​"""

"""
8. Match the set of all valid Web site addresses (URLs) (start
with a loose regex, and then try to tighten it as much as you
can, yet maintain correct functionality).Try to break what we did in 
class and improve it.
"""

"""​
9. type(). The type() built-in function returns a type object,
which is displayed as the following Pythonic-looking string:
​
    # >>> type(0)
    # <type 'int'>
    # >>> type(.34)
    # <type 'float'>
    # >>> type(dir)
<type 'builtin_function_or_method'>
​
Create a regex that would extract the actual type name from
the string. Your function should take a string like this <type
'int'> and return int. (Ditto for all other types, such as
‘float’, ‘builtin_function_or_method’, etc.) Note: You
are implementing the value that is stored in the __name__
attribute for classes and some built-in types.
​"""

"""
10. Processing Dates. In Section 1.2, we gave you the regex pattern
that matched the single or double-digit string representations of
the months January to September (0?[1-9]). Create the regex
that represents the remaining three months in the standard
calendar.
"""