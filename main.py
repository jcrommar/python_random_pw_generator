import random
import array

# Maximum length of password needed
# this can be changed to suit your password
MAX_LEN = 12

# declare the arrays of the character that we need in the password
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<&# 039;] 

# combine all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# randomly select one character from each character list
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

# combine the characters random
# at this stage. the password contains 4 chars only
# we want a 12 chars password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# we have characters from each set of chars
for x in range (MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	# convert temp password into array
	# prevent consistency where password is not the same
	temp_pass_list = array.array(&# 039;u&# 039;, temp_pass)
	random.shuffle(temp_pass_list)

# traverse the temporary password array and append the chars
password = ""
for x in temp_pass_list:
	password = password + x

# print out password
print(password)
