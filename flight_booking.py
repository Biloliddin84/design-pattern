class FlightBooking:
    """Aviachiptalarni bron qilish va bekor qilish."""

    def book(self, user, destination):
        print(f"[Aviachipta] {user} uchun {destination} yo'nalishiga chipta bron qilindi.")
        return True

    def cancel(self, user, destination):
        print(f"[Aviachipta] {user}ning {destination} yo'nalishidagi chiptasi bekor qilindi.")
        return True
