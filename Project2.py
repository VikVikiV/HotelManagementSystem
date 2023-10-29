def Billing_Deallocation():
    global listOfRooms
    if not listOfRooms:
        print("No rooms to Biil or Deallocate. Please add rooms first.")
    else:
        room_number = int(input("Please enter the room number for Billing or Deallocation: "))
        found_room = False
        for obj_room in listOfRooms:
            if obj_room.RoomNo == room_number:
                found_room = True
                choice = input("Select an option: (B)ill or (D)eallocate: ")
                if choice.upper() == "B":
                    obj_room.IsAllocated = False
                    print(f"Room {room_number} has been successfully billed.")
                elif choice.upper() == "D":
                    listOfRooms.remove(obj_room)
                    print(f"Room {room_number} has been successfully deallocated.")
                else:
                    print("Invalid input. Please Select either 'B' or 'D'. ")
                break;
        if not found_room:
            print("Invalid room number.")
            room_number()