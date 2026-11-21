# Student Marks Calculator

name = input("Enter student name: ")

def get_mark(subject):
    while True:
        mark = int(input("Enter " + subject + " marks: "))
        if 0 <= mark <= 100:
            return mark
        else:
            print("Invalid marks! Enter 0 to 100.")

m1 = get_mark("Tamil")
m2 = get_mark("English")
m3 = get_mark("Maths")
m4 = get_mark("Science")
m5 = get_mark("Computer")

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
