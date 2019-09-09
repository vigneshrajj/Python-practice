def signin():
    while True:
        print('\n**********SIGN IN**********\n')
        email=input('Enter email : ')
        pasw=input('Enter password: ')
        file=open('D:\~Projects\python github\projects\Food_maza\Cust_details.txt','rt')
        emaill={}
        for line in file:
            emaill[line.split(':')[0]]=line.split(':')[1].strip('\n')
        if(email not in emaill.keys()):
            print('Invalid email!')
            continue
        elif(emaill[email]!=pasw):
            print('Invalid password!')
            continue
        else:
            break
        file.close()