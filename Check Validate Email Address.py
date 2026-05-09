email=input("Enter your email address:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and email.count("@") == 1:
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="@" or i=="." or i=="_":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email Address 5")
                else:
                    print("Right Email Address ")
            else:
                print("Wrong Email Address 4")
        else:
            print("Wrong Email Address 3")

    else:
        print("Wrong Email Address 2")
else:
    print("Wrong Email Address 1")