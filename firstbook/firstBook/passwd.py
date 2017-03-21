#coding:utf-8

password_list=['*#*#','12345']

def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('enter a new password:')
        password_list.append(new_password)
        print ('Your password is change now!')
        account_login()
    else:
        print ('Enter error,input again')
        account_login()
account_login()	

