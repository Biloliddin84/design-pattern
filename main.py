from travel_facade import TravelFacade


travel = TravelFacade()

travel.book_trip(
    user="Biloliddin",
    destination="Madina",
    hotel="FIRDA HOTEL",
    nights=5,
    amount=7_500_000,
)

travel.cancel_trip(
    user="Biloliddin",
    destination="Madina",
    hotel="FIRDA HOTEL",
    amount=7_500_000,
)
