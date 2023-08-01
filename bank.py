print('___________________________Welcome To SBI___________________________')
print()
print('* Please enter your details *')
print()
a=input('Enter your account number:')
u=input('Username:')
p=input('Password:')
r=input('Re-enter password:')
print()
if r==p:
    print('#--You have login successfully--#')
    balance = 50000
    print()
    s = input('To check your account balance enter your account number:')
    if s == a:
        print('Your account balance is', balance, 'Rs')
        x = int(input('Enter amount to withdraw:'))
        class sbi:
            def withdraw(self, balance):
                if x <= balance:
                    print('                      * Transaction completed successfully *', )
                    print('Your current balance is', balance - x,'Rs')
                    print()
                else:
                    print('Ooops...Insufficient balance...!')
        m = sbi()
        m.withdraw(50000)
    else:
        print()
        print('*** Please check your account number...!')
else:
    print('Please enter correct password...!')
