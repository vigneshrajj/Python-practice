import re
def signup():
    print('**********SIGN UP**********\n')
    while True:
        count=0
        email=input('Enter email address: ')
        email_valid=re.match('[a-zA-Z]+@[a-zA-Z]+\.com',email)
        file=open('D:\~Projects\python github\projects\Food_maza\Cust_details.txt','rt')
        for line in file:
            if(email in line):
                count=count+1
        file.close()
        if(email_valid==None):
            print('Format Invalid!')
            continue
        elif(count>0):
            print('Email already exists!')
            continue
        pasw=input('Enter password (min 8 char.): ')
        pasw_valid=re.match('.{8,}',pasw)
        if(pasw_valid==None):
            print('Format Invalid!')
            continue
        file=open('D:\~Projects\python github\projects\Food_maza\Cust_details.txt','at')
        file.write(email+':'+pasw+'\n')
        file.close()
        break