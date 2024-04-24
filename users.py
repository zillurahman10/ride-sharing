from abc import ABC, abstractclassmethod
class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractclassmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location

    def display_profile(self):
        print(f'Rider: {self.name} and email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print('Amount less than zero')

    def update_location(self, current_location):
        self.current_location = current_location

    

    