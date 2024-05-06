#Szálloda és annak szobái 
class Hotel:
    def __init__(self, hotelName, hotelLocation):
        self.hotelName=hotelName
        self.hotelLocation=hotelLocation 


highClass = Hotel(hotelName="High LifeSytle Resort,", hotelLocation="Monaco")
vintageCastle=Hotel(hotelName="Uphill Vintage Hotel", hotelLocation="Norvégia")
        
class Room:
    def __init__(self, price, roomNum):
        self.price=price
        self.roomNum=roomNum


class OneBedRoom(Room):
    def __init__(self, roomNum):
        super().__init__(8000, roomNum)

class TwoBedRoom(Room):
    def __init__(self,roomNum ):        
        super().__init__(15000, roomNum)

