#OOP Concept

#check the number using 79927398713 it will give the output


class CreditCard(object):
    def __init__(self, card_no):
        self.card_no = card_no

    @classmethod
    def set_card(self, card_to_check):
        return self(card_to_check)
    
    @property
    def company(self):
        comp = None
        if str(self.card_no).startswith("4"):
            comp = "Visa Card"

        elif str(self.card_no).startswith(('50','67','58','63')):
            comp = "Maestro Card"

        elif str(self.card_no).startswith('5'):
            comp = "Master Card"

        elif str(self.card_no).startswith('37'):
            comp = "American Express Card"

        elif str(self.card_no).startswith('62'):
            comp = "UniounPay Card"

        elif str(self.card_no).startswith('7'):
            comp = "Gasoline Card"

        return 'Company:'  +comp  
    

    def first_check(self):
        if 13 <= len(self.card_no) <= 19:
            message = "First Check: Valid Interns of Length"
        else:
            message = "First Check: check credit card number once again, it must be of 13 or 16 digit long"

        return message
    
#validate the card
    def validate(self):
        #double every second digit from right to left
        sum_ = 0
        crd_no = self.card_no[::-1] #this operation basically reverse

        for i in range(len(crd_no)):
            if i % 2 ==  1:
                double_it = int(crd_no[i]) * 2
                if len(str(double_it)) == 2:
                    sum_ += sum([eval(i) for i in str(double_it)])
                else:
                    sum_ += double_it

        if sum_ % 10 == 0:
            response = "Valid Card"

        else:
            response = "Invalid Card"

        return response


    @property
    def checksum(self):
        return "#checksum: #" + self.card_no[-1]

card_number = input("Enter your credit card number: ")
card = CreditCard.set_card(card_number)
print(card.company)

print('Card:' , card.card_no)
print(card.first_check())
print(card.checksum)
print(card.validate())