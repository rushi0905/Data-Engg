
# num = int(input("Enter the number : "))
# def number_verify():
#     if num > 0:
#         print("+ve number")
#     else:
#         print("-ve number")
# number_verify()

# age=int(input("Enter the age : "))
# def vote_eligibilty(age):
#     if age > 18:
#         print("Valid age")
#     else:
#         print("not eligible")
# vote_eligibilty(age)
#read the 5 subjects marks of the student and print the total marks and grades as well

marks=(int(input("math : ")),
       int(input("english : ")),
       int(input("hindi : ")),
       int(input("marathi : ")),
       int(input("history : ")))
total = sum(marks)
avg = total/5
print("The total is :",total," & The avg is : ",avg)
#total = 60
def cal_marks_and_grade(marks,total):
    if avg > 75:
        print("student is in A grade")
    elif  60 <= avg <75:
        print("student is in B grade")
    elif 35<= avg <60:
        print("student is in C grade")
    else:
        print("student is fail")
cal_marks_and_grade(marks,total)

