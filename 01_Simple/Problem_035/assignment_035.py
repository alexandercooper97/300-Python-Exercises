'''
Write A Python Program To Get 10 Name Of The Students From The User In A List,
Display That Students Name In Reverse Order with 
removing  last and first Student name
'''

def get_names_students():
    std_name = []

    for i in range(10):
        std_name.append(input("Enter name of the Student : "))
    return std_name

#print("These are student stored in the list "+str(std_name))
def show_proper_form(std_name):
    print("Student Name in proper form")
    for j in std_name:
        print(j)

def show_desc_form(std_name):
    std_name.reverse()

    print("Student Name in DESC form")
    for d in std_name:
        print(d)

def show_desc_form_v2(sdt_name):
    std_name.pop()
    std_name.pop(0)
    print("Student Name in DESC form")
    print("removing  last and first Student name")

    for d in std_name:
        print(d)



if __name__=="__main__":
    std_name = get_names_students()
    print("\n")
    show_proper_form(std_name)
    print("\n")
    show_desc_form(std_name)
    print("\n")
    show_desc_form_v2(std_name)