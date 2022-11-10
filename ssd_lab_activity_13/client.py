import requests

def signup():
    name = input("Enter Name:")
    email = input("Enter Email:")
    pwd = input("Enter Password:")
    payload = {
        "name": name,
        "email": email,
        "password": pwd
    }

    resp = requests.post("http://127.0.0.1:5000/user/signup", json=payload).content.decode()

    print(resp)

def signin():
    email = input("Enter Email:")
    pwd = input("Enter Password:")

    payload = {
        "email": email,
        "password": pwd
    }

    resp = requests.post("http://127.0.0.1:5000/user/signin", json=payload).content.decode()

    print(resp)

def signout():
    # email = input("Enter Email:")
    # pwd = input("Enter Password:")

    # payload = {
    #     "email": email,
    #     "password": pwd
    # }

    resp = requests.post("http://127.0.0.1:5000/user/signout").content.decode()

    print(resp)

while True:
    ch = int(input("1.SignUP\n2.SignIn\n3.SignOut\n"))
    if(ch==1):
        signup()
    elif(ch==2):
        signin()
    elif(ch==3):
        signout()
    
    else:
        break