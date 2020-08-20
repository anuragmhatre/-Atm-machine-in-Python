print('....WELCOME IDBI BANK ATM....')
restart=('y')
chances= 3
balance = 1000

while chances>=0:
    pin=int(input('enter your pin = '))
    if pin==(1525):
        print('welcome \n')
        while restart not in ('no','N','NO','n'):
            print('enter 1 for balance:  \n')
            print('enter 2 for widhdrawl:  \n')
            print('enter 3 for deposit: \n')
            print('enter 4 for exit: \n')
            option = int(input('what would you choose:  '))
            if option==1:
                print('YOUR BLANCE IS $: ',balance,'\n')
                restart=input('enter  Y go back = ')
                if restart in ('no','N','NO','n'):
                    print('THANK YOU')
                    break
            elif option==2:
                option2=('y')
                widhdrawl=float(input('how much would you widhdrawl :   \n $100,$200,$500,$2000:  '))
                if widhdrawl in[100,200,500,2000]:
                    balance = balance - widhdrawl
                    print('\n your available bal--: $',balance)
                    restart= input('what would you like to do? ')
                    if restart in('no','N','NO','n'):
                        print('Thankyou')
                        break
                elif widhdrawl !=[100,200,500,2000]:
                        print('Invalid amount ,please retry \n')
                        restart=('y')
                elif widhdrawl == 1:
                    widhdrawl=float(input('please new amount: '))
            elif option==3:
                pay_in=float(input('how  much would you desposit: '))
                balance = balance + pay_in
                print('\n your balance now :$ ',balance)
                restart = input('would you like to go back?')
                if restart in ('no','N','NO','n'):
                    print('thankyou')
                    break

            elif option==4:
                print('take your card \n')
                print('thnakyou')
                break
            else:
                print('please enter correct pin. \n')
                restart=('y')
    elif pin !=('1525'):
        print('Incorrect password')
        chances= chances-1
        if chances == 0:
            print('\n contact bank please----')
            break




