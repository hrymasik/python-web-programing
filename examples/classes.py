class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        self.id = Flight.counter 
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration
    def print_info(self):
          print(f"Flight origin: {self.origin}")
          print(f"Flight destination: {self.destination}")
          print(f"Flight duration: {self.duration}")
          print()
          print("Passengers")
          for passenger in self.passengers:
              print(f"{passenger.flight_id} {passenger.name}")
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

    def delay(self):
        self.duration += 10

def main():
    f1 = Flight(origin="New York", destination="Paris", duration=540)

  # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

  # Add passengers.
    f1.add_passenger(alice)

    f1.print_info()


    
if __name__ == "__main__":
    main()