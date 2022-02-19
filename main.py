# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_string = name1 + name2
lower_case_string = combine_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

print( f"There is {t} times of T")
print (f"There is {r} times of R")
print (f"There is {u} times of U")
print (f"There is {e} times of E")
print (f"Total = {t+r+u+e} times")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
print (f"There is {l} times of L")
print (f"There is {o} times of O")
print (f"There is {v} times of V")
print (f"There is {e} times of E")
print (f"Total = {l+o+v+e} times") 

Score = t+r+u+e+l+o+v+e

print (f"Total love score = {Score}")
if (Score < 10 ) or (Score > 90):
  print ("Your score is **x**, you go together like coke and mentos.")
elif (Score < 50) and (Score > 40):
  print ("Your score is **y**, you are alright together.")
else:
  print ("Your score is **z**.")
  





