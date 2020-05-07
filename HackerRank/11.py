if __name__ == '__main__':
    N = int(input())
op_li=[]
for i in range(N):
    command = input()
    commands=command.split()
    if("insert" in command.lower()):
        op_li.insert(int(commands[1]),int(commands[2]))
    elif("print" in command.lower()):
        print(op_li)
    elif("remove" in command.lower()):
        for j in range(len(op_li)):
            if(op_li[j]==int(commands[1])):
                op_li.pop(j)
                break
    elif("append" in command.lower()):
        op_li.append(int(commands[1]))
    elif("sort" in command.lower()):
        op_li.sort()
    elif("pop" in command.lower()):
        op_li.pop()
    elif("reverse" in command.lower()):
        op_li=op_li[::-1]
