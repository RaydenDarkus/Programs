from tabulate import tabulate
import collections
 
password = input("Enter the password : ")
length = len(password)
no_of_characters = length
no_of_upper = len([letter for letter in password if letter.isupper()])
no_of_lower = len([letter for letter in password if letter.islower()])
no_of_digits = len([letter for letter in password if letter.isdigit()])
no_of_symbols = len([letter for letter in password if (
   (letter.isdigit() == False) and (letter.isalpha() == False))])
min_req = 0
if length > 8:
   min_req += 1
if no_of_upper > 0:
   min_req += 1
if no_of_lower > 0:
   min_req += 1
if no_of_digits > 0:
   min_req += 1
if no_of_characters > 0:
   min_req += 1
 
entropy = 0
 
bonus_table = [["Bonus", "Entropy", "Count", "Bonus Value"],
              ["No: of Characters",
                  "+(n*4)", no_of_characters, no_of_characters*4],
              ["Uppercase letters", "+((len-n)*2)",
               no_of_upper, ((length-no_of_upper)*2)],
              ["Lowercase letters", "+((len-n)*2)",
               no_of_lower, ((length-no_of_lower)*2)],
              ["Numbers", "+(n*4)", no_of_digits, no_of_digits*4],
              ["Symbols", "+(n*6)", no_of_symbols, no_of_symbols*6],
              ["Minimum Requirements", "+(n*2)", min_req, min_req*2]]
 
entropy_bonus = int(bonus_table[1][3])+int(bonus_table[2][3])+int(
   bonus_table[3][3])+int(bonus_table[4][3])+int(bonus_table[5][3])+int(bonus_table[6][3])
 
print(tabulate(bonus_table, headers="firstrow", tablefmt="fancy_grid"))
 
only_alpha = 0
only_number = 0
 
if(password.isalpha()):
   only_alpha = 1
if(password.isdigit()):
   only_number = 1
 
frequencies = collections.Counter(password)
repeated = {}
for key, value in frequencies.items():
   if value > 1:
       repeated[key] = value
 
digit_repeated = 0
symbol_repeated = 0
upper_repeated = 0
lower_repeated = 0
char_repeated = 0
 
for i in repeated:
   char_repeated += repeated[i]
   if i.isdigit():
       digit_repeated += repeated[i]
   elif i.islower():
       lower_repeated += repeated[i]
   elif i.isupper():
       upper_repeated += repeated[i]
   else:
       symbol_repeated += repeated[i]
 
deduction_table = [["Deduction", "Entropy", "Count", "Deduction Value"],
                  ["Numbers Only", "-n", only_number, only_number],
                  ["Characters Only", "-n", only_alpha, only_alpha],
                  ["Number Repeated", "-(n*2)",
                   digit_repeated, digit_repeated*2],
                  ["Character Repeated",
                      "-(n/2)", char_repeated, char_repeated/2],
                  ["Upper Repeated", "-(n*2)",
                   upper_repeated, upper_repeated*2],
                  ["Lower Repeated", "-(n*2)",
                   lower_repeated, lower_repeated*2],
                  ["Symbol Repeated", "-(n*3)", symbol_repeated, symbol_repeated*3]]
 
entropy_deduction = int(deduction_table[1][3])+int(deduction_table[2][3])+int(deduction_table[3][3])+int(
   deduction_table[4][3])+int(deduction_table[5][3])+int(deduction_table[6][3])+int(deduction_table[7][3])
 
print(tabulate(deduction_table, headers="firstrow", tablefmt="fancy_grid"))
 
print("Strength of Password : ",entropy_bonus - entropy_deduction)
