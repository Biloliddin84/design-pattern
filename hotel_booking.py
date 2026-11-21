class HotelBooking:
    """Mehmonxonadan xona bron qilish va bekor qilish."""

    def book(self, user, hotel, nights):
        print(f"[Mehmonxona] {user} uchun '{hotel}' mehmonxonasida {nights} kecha xona bron qilindi.")
        return True

    def cancel(self, user, hotel):
        print(f"[Mehmonxona] {user}ning '{hotel}' mehmonxonasidagi broni bekor qilindi.")
        return True
