marks_dict = {'smit': 50, 'mark': 45, 'python': 40, 'babu': 35, 'raju': 30}

n = input("enter your name : ")

if n in marks_dict:
    print(f"{n}'s marks : " , marks_dict[n])

else :
    print("student not found in list")
