import re
def payment():
    print('\n**********PAYMENT PORTAL**********\n')
    print('\n**Enter card details**')
    while True:
        card_type=input('Enter card type(Credit/Debit):')
        if(card_type=='Debit' or card_type=='debit'):
            break
        elif(card_type=='Credit' or card_type=='credit'):
            break
        else:
            print('Wrong choice!!!')
            continue
    while True:
        card_num=input('Enter card number: ')
        card_num_valid=re.match('[0-9]{16}',card_num)
        if(card_num_valid==None):
            print('Format Invalid!')
            continue
        else:
            break
    while True:
        exp_date=input('Valid upto(mm/yy): ')
        exp_date_valid=re.match('(((0)[0-9])|((1)[0-2]))(\/)[19|20]\d{2}',exp_date)
        if(exp_date_valid==None):
            print('Format Invalid!')
            continue
        else:
            break
    while True:
        card_name=input('Enter card holder\'s name: ')
        card_name_valid=re.match('[a-z A-Z]{2,}',card_name)
        if(card_name_valid==None):
            print('Format Invalid!')
            continue
        else:
            break
    while True:
        card_cvv=input('Enter 3-digit CVV: ')
        card_cvv_valid=re.match('[0-9]{3}',card_cvv)
        if(card_cvv_valid==None):
            print('Format Invalid!')
            continue
        else:
            break