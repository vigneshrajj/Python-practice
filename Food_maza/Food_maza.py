import os
os.chdir(r"D:\~Projects\python github\projects\Food_maza")
import Sign_Up,Sign_In,Food_order,Payment
print('WELCOME TO FOOD MAZA!!\n')
Sign_Up.signup()
Sign_In.signin()
Food_order.order()
Payment.payment()
print('Your order will be delivered soon!!!')