class Payment:
    """To'lovni amalga oshirish va qaytarish."""

    def pay(self, user, amount):
        print(f"[To'lov] {user}dan {amount:,} so'm yechildi.")
        return True

    def refund(self, user, amount):
        print(f"[To'lov] {user}ga {amount:,} so'm qaytarildi.")
        return True
