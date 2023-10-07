import random
import string
from fpdf import FPDF
import MySQLdb

# Your User, Seat, Card, and Ticket classes here...
class User1:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free() and card.validate(seat.get_price()):
            seat.occupy()
            ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
            ticket.to_pdf()
            return "Purchase successful"
        else:
            return "Purchase failed"
class Seat:
    """Represents a cinema seat that can be taken from a User"""

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="rahul@1234",
            db="movie"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT price FROM Seat WHERE seat_id=%s", (self.seat_id,))
        price = cursor.fetchall()[0][0]
        connection.close()
        return price

    # The rest of the Seat class remains the same...

class Card:
    # Represents a bank card needed to finalize a seat purchase

    def __init__(self, type, number, cvc, holder):
        self.holder = holder
        self.cvc = cvc
        self.number = number
        self.type = type

    def validate(self, price):
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password="rahul@1234",
            db="movie"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT balance FROM Card WHERE number=%s AND cvc=%s", (self.number, self.cvc))
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                cursor.execute("UPDATE Card SET balance=%s WHERE number=%s AND cvc=%s", (balance - price, self.number, self.cvc))
                connection.commit()
                connection.close()
                return True

        connection.close()
        return False
class Ticket:

    #Represents a cinema Ticket purchased by a User

    def __init__(self,user,price,seat_number):
        self.user=user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number=seat_number

    def to_pdf(self):
        pdf=FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()

        pdf.set_font(family='Times',style="B",size=24)
        pdf.cell(w=0,h=80,txt="Your Digital Ticket",border=1,ln=1,align="C")

        pdf.set_font(family='Times',style="B",size=14)
        pdf.cell(w=100,h=25,txt="Name:",border=1)
        pdf.set_font(family='Times',style="",size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1,ln=1)
        pdf.cell(w=0, h=5, txt="", border=0,ln=1)

        pdf.set_font(family='Times', style="B", size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family='Times', style="", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family='Times', style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style="B", size=14)
        pdf.cell(w=100, h=25, txt="seat Number", border=1)
        pdf.set_font(family='Times', style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("sample.pdf",'F')


if __name__ == "__main__":
    name = input("Your full name:")
    seat_id = input("Preferred seat number:")
    card_type = input("Your card type:")
    card_number = input("Your card number:")
    card_cvc = input("Your card cvc:")
    card_holder = input("Card Holder name:")

    user = User1(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)
    result = user.buy(seat=seat, card=card)
    print(result)
