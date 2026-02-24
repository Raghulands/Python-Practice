#credcheck
username="pycharm"
password="deadbody"

ipuser=input()
ippassword=input()

def validate():
    if(username==ipuser and password==ippassword):
        return True
    else:
        return False

print(validate())