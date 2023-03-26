### Loops
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


### Code challenge: Average Height using for loops
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # turning the student heights into integers
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total = 0 # creating a variable so the heights can be added to it
for height in student_heights:
    total += height
average = total / len(student_heights)
print(average) 