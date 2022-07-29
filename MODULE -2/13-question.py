# Write a Python program to count the occurrences of each word in a given sentence.

str = " this is phython! "

x=str.split(" ")
print(x)

for i in x:
      print(f"{i}= " , x.count(i))
