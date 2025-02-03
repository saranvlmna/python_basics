count= input("input a number: ")

def test(count):
    if count == 0 or count =="0":
        print("nothing")
    elif count == 1 and count == "1":
        print("*")
    elif count ==2 and not count == "12":
        print("**")
    elif count == 3:
        print("***")
    else:
        print("more than 3")

test(int(count))