class Manage_public_parking:
    def __init__(self):
        self.parking_spots = {}

        # Create parking spots for IDs 1 to 10 and mark them as available
        for parking_id in range(1, 11):
            spot_id = str(parking_id)
            self.parking_spots[spot_id] = {"info": f"Spot {spot_id}", "occupied": False}

        self.available_spots = list(self.parking_spots.keys())  # Initially, all spots are available

    def create_parking_spots(self, spot_id, spot_info):
        if spot_id not in self.parking_spots:
            self.parking_spots[spot_id] = {"info": spot_info, "occupied": False}
            print("Parking spot added successfully!")
        else:
            print("Parking spot already exists!")
        self.save_to_file()

    def read_parking_spots(self):
        print("Parking Spots:")
        for spot_id, spot_info in self.parking_spots.items():
            status = "Available" if not spot_info["occupied"] else "Occupied"
            print(f"Spot ID: {spot_id}, Info: {spot_info['info']}, Status: {status}")

    def update_parking_spot(self, spot_id, spot_info):
        if spot_id in self.parking_spots:
            self.parking_spots[spot_id]["info"] = spot_info
            print("Parking spot updated successfully!")
        else:
            print("Parking spot does not exist!")
        self.save_to_file()

    def delete_parking_spot(self, spot_id):
        if spot_id in self.parking_spots:
            del self.parking_spots[spot_id]
            print("Parking spot deleted successfully!")
        else:
            print("Parking spot does not exist!")
        self.save_to_file()

    def save_to_file(self):
        with open("parking_records.txt", "w") as file:
            for spot_id, spot_info in self.parking_spots.items():
                file.write(f"Spot ID: {spot_id}, Info: {spot_info['info']}, Occupied: {spot_info['occupied']}\n")

    def available_parking_spots(self):
        if self.available_spots:
            print("Available Parking Spots:", ", ".join(self.available_spots))
            return self.available_spots
        else:
            print("No available parking spots.")
            return []

    def update_available_spots(self):
        self.available_spots = [spot_id for spot_id, spot_info in self.parking_spots.items() if not spot_info["occupied"]]


class Track_parking_usage:
    def __init__(self):
        self.usage_history = {}

    def track_entry(self, spot_id, time,parking_manager):
        if spot_id in parking_manager.available_spots:
            self.usage_history[spot_id] = {"entry_time": time}
            print("Entry recorded successfully!")
            parking_manager.parking_spots[spot_id]["occupied"] = True
            parking_manager.update_available_spots()
            parking_manager.available_parking_spots()
            self.save_to_file()
        else:
            print("Spot is already occupied or does not exist.")

    def track_exit(self, spot_id, time, parking_manager):
        if spot_id in self.usage_history:
            self.usage_history[spot_id]["exit_time"] = time
            print("Exit recorded successfully!")
            parking_manager.parking_spots[spot_id]["occupied"] = False
            parking_manager.update_available_spots()
            parking_manager.available_parking_spots()
            self.save_to_file()
        else:
            print("No entry found for the given spot ID!")

    def display_usage_history(self):
        print("Parking Usage History:")
        for spot_id, usage_info in self.usage_history.items():
            print(f"Spot ID: {spot_id}, Entry Time: {usage_info['entry_time']}, Exit Time: {usage_info.get('exit_time', 'N/A')}")

    def save_to_file(self):
        with open("parking_records.txt", "a") as file:
            for spot_id, usage_info in self.usage_history.items():
                file.write(f"Spot ID: {spot_id}, Entry Time: {usage_info['entry_time']}, Exit Time: {usage_info.get('exit_time', 'N/A')}\n")


def main():
    parking_manager = Manage_public_parking()
    usage_tracker = Track_parking_usage()

    while True:
        print("\n--- Menu ---")
        print("1. Create Parking Spot")
        print("2. Read Parking Spots")
        print("3. Update Parking Spot")
        print("4. Delete Parking Spot")
        print("5. Record Entry")
        print("6. Record Exit")
        print("7. Display Usage History")
        print("8. Display Available Parking Spots")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            spot_id = input("Enter spot ID: ")
            spot_info = input("Enter spot information: ")
            parking_manager.create_parking_spots(spot_id, spot_info)
        elif choice == '2':
            parking_manager.read_parking_spots()
        elif choice == '3':
            spot_id = input("Enter spot ID to update: ")
            spot_info = input("Enter updated spot information: ")
            parking_manager.update_parking_spot(spot_id, spot_info)
        elif choice == '4':
            spot_id = input("Enter spot ID to delete: ")
            parking_manager.delete_parking_spot(spot_id)
        elif choice == '5':
            parking_manager.available_parking_spots()
            spot_id = input("Enter spot ID: ")
            if spot_id in parking_manager.available_spots:
                time = float(input("Enter Entry time: "))
                usage_tracker.track_entry(spot_id,time,parking_manager)
            else:
                print("Invalid spot ID or spot is already occupied.")
        elif choice == '6':
            spot_id = input("Enter spot ID: ")
            if spot_id in parking_manager.parking_spots:
                time = float(input("Enter exit time: "))
                usage_tracker.track_exit(spot_id, time, parking_manager)
            else:
                print("Invalid spot ID.")
        elif choice == '7':
            usage_tracker.display_usage_history()
        elif choice == '8':
            parking_manager.available_parking_spots()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
