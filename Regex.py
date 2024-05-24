print('Twinkle twinkle little star, \n\t how I wonder what you are, \n\t\t Up above the world so high, \n\tLike a diamond in the sky. \n Twinkle twinkle little star, \n\t\t how I wonder what you are')

# write a programme to show current date and time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#first and last name backwards

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#file name
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

#first and last letters
color_list = ["Red","Green","White" ,"Black"]
print("%s %s"%(color_list[0], color_list[-1])) # %s's get rid of the ''

#exam dates
exam_st_date = (11, 12, 2014)
print('The examination will start from : %i, %i, %i'%exam_st_date)

#integer
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#cALENDARS
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#strings
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#Some Regex examples
import re  # This is like calling your detective friend for help

text = "The cat chased the mouse. A caterpillar crawled on a leaf."

pattern = r'cat\w*'  # This pattern means: find 'cat' followed by any letters (\w*) 

matches = re.findall(pattern, text)  # Your detective finds all the matches

print(matches)  # The detective shows you the words: ['cat', 'chased', 'caterpillar']



#Email extraction
import re

# The regex pattern to match a valid email address
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# The email to be checked
email = "example@email.com"

# Using re.match() to check if the email matches the pattern
if re.match(pattern, email):
    print("Valid email!")
else:
    print("Invalid email.")



#Phone number Extraction
import re

# The regex pattern to match a U.S. phone number
pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

# The text containing the phone number
text = "My phone number is 123-456-7890."

# Using re.findall() to find all matches of the pattern in the text
matches = re.findall(pattern, text)
print(matches)  


#Replacing words
import re

# The text to be modified
text = "This is a bad example, not a good one."

# The regex pattern to match the word "bad"
pattern = r'\bbad\b'

# The replacement word
replacement = "good"

# Using re.sub() to replace all occurrences of the pattern with the replacement
new_text = re.sub(pattern, replacement, text)
print(new_text) 


#Whitespace removal
import re

# The text with extra spaces and tabs
text = "   This    has  extra   spaces    and tabs.   "

# The regex pattern to match one or more whitespace characters
pattern = r'\s+'

# The replacement string with a single space
replacement = ' '

# Using re.sub() to replace all occurrences of the pattern with the replacement
cleaned_text = re.sub(pattern, replacement, text.strip())
print(cleaned_text)  


#URL extractin
import re

# The text with extra spaces and tabs
text = "   This    has  extra   spaces    and tabs.   "

# The regex pattern to match one or more whitespace characters
pattern = r'\s+'

# The replacement string with a single space
replacement = ' '

# Using re.sub() to replace all occurrences of the pattern with the replacement
cleaned_text = re.sub(pattern, replacement, text.str())
print(cleaned_text) 