# Simple Parking Management System
# Mini Project (Beginner level)

def show_menu():
    print("\n=== Parking Management System ===")
    print("1. Park a Vehicle")
    print("2. Unpark a Vehicle")
    print("3. Show Parking Status")
    print("4. Exit")
    print("=================================")

def park_vehicle(parking_slots, vehicle_number):
    for slot in parking_slots:
        if parking_slots[slot] is None:
            parking_slots[slot] = vehicle_number
            print(f"Vehicle {vehicle_number} parked in Slot {slot}.")
            return
    print("No empty slots available!")

def unpark_vehicle(parking_slots, vehicle_number):
    for slot in parking_slots:
        if parking_slots[slot] == vehicle_number:
            parking_slots[slot] = None
            print(f"Vehicle {vehicle_number} removed from Slot {slot}.")
            return
    print(f"Vehicle {vehicle_number} not found in parking.")

def display_status(parking_slots):
    print("\n--- Parking Lot Status ---")
    for slot in parking_slots:
        if parking_slots[slot] is None:
            print(f"Slot {slot}: Empty")
        else:
            print(f"Slot {slot}: Occupied by {parking_slots[slot]}")
    print("--------------------------")

def main():
    total_slots = int(input("Enter total number of parking slots: "))

    # Dictionary to store slot status (slot number → vehicle number or None)
    parking_slots = {}
    for i in range(1, total_slots + 1):
        parking_slots[i] = None

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_num = input("Enter vehicle number to park: ")
            park_vehicle(parking_slots, vehicle_num)
        elif choice == '2':
            vehicle_num = input("Enter vehicle number to unpark: ")
            unpark_vehicle(parking_slots, vehicle_num)
        elif choice == '3':
            display_status(parking_slots)
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()
