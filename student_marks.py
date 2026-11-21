
# Student Marks Calculator

name = input("Enter student name: ")

m1 = int(input("Enter Tamil marks: "))
m2 = int(input("Enter English marks: "))
m3 = int(input("Enter Maths marks: "))
m4 = int(input("Enter Science marks: "))
m5 = int(input("Enter Computer marks: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
