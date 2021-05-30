
from cs50 import get_string
#gets input from user
texto = get_string("Text:  ")
text = texto.lower()
sent = 0
words= 1
letter = 0
#interates over whole text and checks if ith character of string is a letter, space, or ponctuation.
for i in range(0, len(text)):

    if str.isalpha(text[i]):
        letter += 1

    if str.isspace(text[i]):
        words += 1

    if (text[i] == "." or text[i] == "!" or text[i] == "?"):
        sent += 1


#get values for formula.
L = float(letter / words * 100)
S = float(sent / words * 100)
grade1 = 0.0588 * L - 0.296 * S - 15.8
grade = round(grade1)
#checks if grade value lower then 1 or bigger then 16.
if grade > 15:
    print("Grade 16+")

elif grade < 1:
    print("Before Grade 1")

else:
    print(f"Grade {grade}")