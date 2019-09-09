def order():
    print('\n**********FOOD ORDER**********\n')
    print('\nPlease select a dish from the menu: \n***MENU***\n\n')
    file=open('D:\~Projects\python github\projects\Food_maza\dishes.txt','rt')
    file1=open('D:\~Projects\python github\projects\Food_maza\dishes(no-price).txt','rt')
    for line in file:
        print(line)
    food_dict={}
    for line in file1:
        lines=line.split(':')
        food_dict[lines[0]]=lines[1]
    food_num=input('Enter dish numbers(spaced): ')
    food_num=food_num.split(' ')
    food_list=[]
    file.close()
    file1.close()
    for i in food_num:
        food_list.append(food_dict[i].strip('\n'))
    food_price={}
    order_price={}
    total=0
    file=open('D:\~Projects\python github\projects\Food_maza\dishes(dictionary).txt','rt')
    for line in file:
        food_price[line.split(':')[0]]=line.split(':')[1].strip('\n')
    for i in food_list:
        order_price[i]=int(food_price[i])
        total+=order_price[i]
    print('Your total price: '+'\u20B9'+str(total))