# get 10 std id
# store in list
# check dublication
# remove dublication
# again display


def dublication(s_lst):
    for i in s_lst:
        if s_lst.count(i) > 1:
            return True
    return False

if __name__=="__main__":
    std_id = []

    for i in range(10):
        std_id.append(int(input("Enter Std ID : ")))

    result = dublication(std_id)
    if result:
        print("Dublication")
    else:
        print("No Dublication")
