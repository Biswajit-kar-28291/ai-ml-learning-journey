n=int(input("Enter total number of student:"))
Student={}
for _ in range(n):
    name=input('Enter Your Name:')
    t_mark=int(input('Enter Your Total Mark:'))
    o_mark=int(input('Enter Your Obtain Mark:'))
    if o_mark==0:
        percentage=0
    else:
        percentage=(o_mark/t_mark)*100

    if percentage>=40:
        print("pass.")
    else:
        print("fail")
    Student={
        "name":name,
        "percentage":percentage,
    }
total=0
for i in Student:
    total+=Student["percentage"]
print(f"avarage mark is {(total/len(Student))}")