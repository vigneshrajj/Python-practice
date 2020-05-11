def swap_case(s):
    sa=[]
    for i in range(len(s)):
        if(s[i].isupper()==True):
            sa.append(s[i].lower())
        elif(s[i].islower()==True):
            sa.append(s[i].upper())
        else:
            sa.append(s[i])
    return ''.join(sa)
