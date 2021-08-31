class Atm(object):

    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
        
    
    def check_balance(self):
        print("your balance is 10000")

    def withdrawl (self,amount):
        new_amount=50000-amount
        print("your withdrawl amount is "+str(amount)+"your remaining balance is "+str(new_amount))

def main():
        cardName=input("insert your card number")
        pinNumber=input("enter your pin")
        newUser=Atm(cardName,pin_number)
        print("choose your activity")
        print("1.balance enquiry 2.Withdrawl")
        activity=int(input("enter activity number"))
        if (activity==1):
            new_user.check_balance()
        elif(activity==2):
            amount=int(input("enter the amount:-"))
            new_user.withdrawl(amount)
        else:
            print("enter the valid number")


if __name__== "main":
    main()