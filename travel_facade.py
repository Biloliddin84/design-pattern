from flight_booking import FlightBooking
from hotel_booking import HotelBooking
from payment import Payment


class TravelFacade:
    """Uchala xizmatni boshqaradi. Mijoz faqat shu klass bilan ishlaydi."""

    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.payment = Payment()

    def book_trip(self, user, destination, hotel, nights, amount):
        print(f"\n=== {user} uchun sayohat bron qilinmoqda ===")

        if not self.flight.book(user, destination):
            print("Aviachipta bron qilinmadi. Jarayon to'xtatildi.")
            return False

        if not self.hotel.book(user, hotel, nights):
            print("Mehmonxona bron qilinmadi. Aviachipta bekor qilinadi.")
            self.flight.cancel(user, destination)
            return False

        if not self.payment.pay(user, amount):
            print("To'lov amalga oshmadi. Bronlar bekor qilinadi.")
            self.hotel.cancel(user, hotel)
            self.flight.cancel(user, destination)
            return False

        print("Sayohat muvaffaqiyatli bron qilindi!")
        return True

    def cancel_trip(self, user, destination, hotel, amount):
        print(f"\n=== {user}ning sayohati bekor qilinmoqda ===")
        self.flight.cancel(user, destination)
        self.hotel.cancel(user, hotel)
        self.payment.refund(user, amount)
        print("Sayohat bekor qilindi, to'lov qaytarildi.")
