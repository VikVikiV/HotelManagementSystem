# *
# * Project Name: Hotel Management Application System for 'LANGHAM Hotels'
# * Author Name: Victor Viki
# * Date: 31/10/2023
# * Application Purpose:Develop software application for 'LANGHAM Hotels' to manage their day-to-day operations
# * like the allocation of rooms, de allocation of rooms, displaying the status of rooms, and other functionality.
# *

import os.path
import datetime
# Importing Modules.
try:
    from RoomModule import Room
    from CustomerModule import Customer
    from RoomAllocationModule import RoomAllocation
    # Display ImportError message.
except ImportError as ex:
    print(ex)
    print("Please check your modules")

# Custom Main Class - Program
# Variables declaration and initialisation
# Initialising array of classroom
list_of_rooms = []
# Initialising integer variable for number of room
noOfRoom = 0
# Create a list of room allocations
listOfRoomAllocations = []
# Initialising file path for both save allocations and back up file
filePath = ""
filePathBackUp = ""


# Main function
def main():
    global noOfRoom, filePath, filePathBackUp

    # Initialising and declaring path for location of the file
    folder_path = os.path.expanduser("~/Documents")
    # Create specific file for both save allocations and back up
    filePath = os.path.join(folder_path, "LHMS_764706455.txt")
    filePathBackUp = os.path.join(folder_path, "LHMS_764706455_Backup_Date_Time.txt")
    # Display main menu
    menu()


# Method for main menu
def menu():
    # Format exception, invalid operation exception
    try:
        # Initialise integer variable
        choice = - 1
        # Do while loop for continuing with menu or not
        while choice != 0:
            # Display main menu
            print("***********************************************************************************")
            print("                 LANGHAM HOTEL MANAGEMENT SYSTEM                  ")
            print("                            MENU                                 ")
            print("***********************************************************************************")
            print("0. Exit")
            print("1. Add Room")
            print("2. Delete Room")
            print("3. Display Room Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocation Details")
            print("6. Billing & De-Allocation")
            print("7. Save the Room Allocation to a File")
            print("8. Show the Room Allocation from a File")
            # Add new option 9 for Backup
            print("9. Backup of the LHMS_764706455.txt file to LHMS_764706455_Backup_Date_Time.txt")
            print("***********************************************************************************")
            # Ask user to enter a number for menu choice
            choice = int(input("Enter Your Choice Number Here (0-9): "))
            if choice == 0:
                # Exit Application function called
                exit(0)
            elif choice == 1:
                # Adding Rooms
                add_room()
            elif choice == 2:
                # Deleting Rooms
                delete_room()
            elif choice == 3:
                # Displaying Room Details
                display_room_details()
            elif choice == 4:
                # Allocating Rooms
                allocate_rooms()
            elif choice == 5:
                # Displaying Room Allocations Details
                display_room_allocation_details()
            elif choice == 6:
                # Billing & De-Allocation
                billing_de_allocation()
            elif choice == 7:
                # Save The Room Allocation to a File
                save_room_allocation_to_file()
            elif choice == 8:
                # Show The Room Allocation from a File
                show_room_allocation_from_file()
            elif choice == 9:
                # Backup
                back_up()
            else:
                print("Please choose (0-9)")
        # Display SyntaxError message.
    except SyntaxError as e:
        print(f"Syntax error :{e}")
        # Display TypeError message.
    except TypeError as e:
        print(f"Type error :{e}")
        # Display ValueError message.
    except ValueError as e:
        print(f"Value error :{e}")


def add_room():
    global noOfRoom, list_of_rooms
    # Format exception
    try:
        # Display 'add rooms' choice selected
        print("You have selected 'ADD ROOMS' from menu")
        # Ask user how many rooms to add, and convert and save as integer variable
        noOfRoom = int(input("Please enter the total number of rooms in the Hotel: "))
        # Display how many rooms are there in total
        print(f"Hotel has {noOfRoom} rooms in total")
        print("***********************************************************************************")
        # Create new array with number of rooms to add
        if len(list_of_rooms) > 0:
            y = len(list_of_rooms)
        else:
            y = 0
        for x in range(noOfRoom):
            room = Room()
            list_of_rooms.append(room)
            # Use for loop to ask user to input room details and save it
        for i in range(y, y + noOfRoom):
            obj_room = list_of_rooms[i]
            # Ask user to enter room number
            print(f"Room Allocation {i + 1}: ")
            # Convert user input to integer and save it
            obj_room.RoomNo = int(input(f"Please enter room number {i + 1}: "))
            # Declare room allocation status to false(not allocated)
            obj_room.is_allocated = False
            # Save the new room object to array of Room
            list_of_rooms[i] = obj_room
            # If condition to check the same room number exist or not when there is more than 1 room added
            if i > 0:
                # Use for loop to check the listOfRooms with the same room number
                for j in range(i):
                    # Use while loop to check the user input room number is equal to previous inputs
                    while list_of_rooms[i].RoomNo == list_of_rooms[j].RoomNo:
                        # Display message for the same room exist and ask to input new room number
                        print(f"Same room number already exist")
                        obj_room.RoomNo = int(input(f"Please enter a new room number {i + 1}: "))
                        # Declare room allocation status to false(not allocated)
                        obj_room.is_allocated = False
                        # Save the new room object to array of Room
                        list_of_rooms[i] = obj_room
            # Display ValueError message.
    except ValueError as e:
        print(f" Value Error: {e} ")
        print("Invalid input, Please try again ")
        add_room()


def delete_room():
    global list_of_rooms
    # If condition to check there is any rooms to display
    if list_of_rooms:
        # Display 'delete rooms' choice selected
        print("You have selected 'DELETE ROOMS' from menu")
        print("***********************************************************************************")
        room_number = int(input("Please enter the room number that you want to delete"))
        try:
            for obj_room in list_of_rooms:
                if obj_room.RoomNo == room_number:
                    list_of_rooms.remove(obj_room)
                # Display ValueError message.
        except ValueError as e:
            print(f"Value Error : {e}")
            print("Invalid input, Please try again")

        print(f"Following rooms have been deleted")
    # If nothing to display, display following message
    else:
        print("No rooms to delete\nPlease add rooms first")


def display_room_details():
    global list_of_rooms
    # If condition to check there is any rooms to display
    if list_of_rooms:
        # Display 'display rooms' choice selected
        print("You have selected 'DISPLAY ROOMS' from menu")
        print("***********************************************************************************")
        print(f"Following rooms have been added")
        # Use foreach loop to display details of each room
        for obj_room in list_of_rooms:
            print(f"Room Number :  {obj_room.RoomNo}")
        # If nothing to display, display following message
    else:
        print("No rooms to display\nPlease add rooms first")


# Method to allocate rooms to customer
def allocate_rooms():
    global noOfRoom, list_of_rooms, listOfRoomAllocations
    # Format exception, Invalid operation exception
    try:
        # Display 'allocate rooms' choice selected
        print("You have selected 'ALLOCATE ROOMS' from menu")
        # Ask user to input how many rooms to allocate
        allocate_room = int(input("How many rooms would you like to allocate?: "))
        # Use while loop to check user input is correct
        while allocate_room > len(list_of_rooms):
            # Display input is incorrect message and give another chance
            print(f"You cannot allocate more rooms than total number of rooms in the Hotel\n" f"Please enter number "
                  f"between 1-{len(list_of_rooms)}: ")
            allocate_room = int(input("How many rooms would you like to allocate?: "))

        # Display how many room will be allocated
        print(f"You are allocating {allocate_room} room(s)")
        # Use for loop to each room and customer details for allocation
        i = 0
        while i < allocate_room:

            print("***********************************************************************************")
            # Create new object called roomAllocation for class RoomAllocation
            room_allocation = RoomAllocation()
            # Create new object called customer for class Customer
            customer = Customer()
            # Display allocation number
            print(f"Room Allocation {i + 1}:")
            # Ask user to input room number to search
            # Declare integer variable, convert user input to integer and save it
            search_room = int(input("Please search Room Number to allocate: "))
            # Use for loop to search matching room from list of rooms that has been added
            for j in range(len(list_of_rooms)):

                # If condition to find matching room number
                # If room number matches, display found message
                if search_room == list_of_rooms[j].RoomNo:

                    # Display matching room found message
                    print("Found matching room number to allocate")
                    # If condition to check for room is already allocated or not
                    # If room is not allocated, display allocation message
                    if not list_of_rooms[j].is_allocated:

                        # Display room searched is empty
                        print(f"Room {list_of_rooms[j].RoomNo} is empty ")
                        # Ask user to enter customer number
                        # Convert user input to integer and save it
                        customer.CustomerNo = int(input("Please enter Customer Number to allocate: "))
                        # Ask user to enter customer name
                        customer.CustomerName = input("Please enter Customer Name to allocate: ")
                        # Change room allocation status to allocated
                        list_of_rooms[j].is_allocated = True
                        # Display allocation done message
                        print("Allocation has been done")
                        # Save room number for allocation and customer details into the object
                        room_allocation.AllocatedRoomNo = search_room
                        room_allocation.AllocatedCustomer = customer
                        # Add object to the list
                        listOfRoomAllocations.append(room_allocation)
                        i += 1
                        break

                    # If room is already allocated, display message: room is occupied
                    else:

                        print(f"Room {list_of_rooms[j].RoomNo} is already occupied\n"   f"Please enter another room"
                              f" to allocate")
                        # Give user another chance
                        i -= 1
                        break

                # For no match found
                else:

                    # If no matching room number found, display message
                    while j == len(list_of_rooms) - 1:
                        print("Could not find matching room number to allocate\n" "Please enter correct room number"
                              " or add room first")
                        # Give user another chance
                        i -= 1
                        break
        i += 1
        # Display ValueError message.
    except ValueError:
        print(" Invalid Input. Please try again. ")


# Method to display room allocations details
def display_room_allocation_details():
    global listOfRoomAllocations
    # If condition to check there is any allocated rooms to display
    if listOfRoomAllocations:
        # Display 'display room allocation details' choice selected
        print("You have selected 'DISPLAY ROOM ALLOCATION DETAILS' from menu")
        # For loop to display details of allocated rooms and customers
        for obj_room in listOfRoomAllocations:
            print("***********************************************************************************")
            print(f"Allocated Room Number :  {obj_room.AllocatedRoomNo}")
            print(f"Customer Number :  {obj_room.AllocatedCustomer.CustomerNo}")
            print(f"Customer Name :  {obj_room.AllocatedCustomer.CustomerName}")

        # If nothing to display, display following message
    else:
        print("No allocated rooms to display\nPlease allocate rooms first")


def billing_de_allocation():
    global listOfRoomAllocations

    try:

        # Display 'deallocate rooms' choice selected
        print("You have selected 'DEALLOCATE ROOMS' from menu")
        # Ask user how many rooms to deallocate
        room_no = int(input("Please enter Room Number for billing and de-allocation: "))

        for obj_room_no in listOfRoomAllocations:
            # If the room number matches the allocated room number.
            if obj_room_no.AllocatedRoomNo == room_no:
                # Asking user amount of days stayed.
                days_stayed = int(input("Please enter the total amount of days stayed: "))
                # Hotel rate per day.
                rate = 150
                # Room charge calculation.
                room_charge = days_stayed * rate
                # Display Billing of room.
                print("Room has been Billed for a total of $", room_charge)
                listOfRoomAllocations.remove(obj_room_no)
                # Display Successful room de-allocation
                print(f"Room has been successfully de-allocated {room_no}")
                break
            else:
                print("Invalid input. There is no Allocated Room")
        # Display SyntaxError message.
    except SyntaxError as a:
        # Display format exception message
        print(a)
        print("Please try again")
        # Call the function again to give user another chance
        billing_de_allocation()
        # Display IOError message.
    except IOError as b:
        # Display invalid operation exception message
        print(b)
        print("Please try again")
        # Call the function again to give user another chance
        billing_de_allocation()
        # Display TypeError message.
    except TypeError as c:
        # Display invalid operation exception message
        print(c)
        print("Please try again")
        # Call the function again to give user another chance
        billing_de_allocation()


# Method to save the room allocations to file
def save_room_allocation_to_file():
    global filePath
    # Unauthorized access exception
    try:
        # Display 'save the room allocations to a file' choice selected
        print("You have selected 'SAVE THE ROOM ALLOCATIONS TO A FILE' from menu")
        print("***********************************************************************************")
        # Initialise FileStream class with specified path, creation mode, and write permission
        with open(filePath, "w") as file:
            # Save current date and time
            now = str(datetime.datetime.now())
            # Foreach loop to write all the details for room allocations and customer, and adds to file
            for obj_roomAllocated in listOfRoomAllocations:
                add_to_file = f"***********************************************************************************\n" \
                              f"Allocated Room Number :  {obj_roomAllocated.AllocatedRoomNo}\n" \
                              f"Customer Number :  {obj_roomAllocated.AllocatedCustomer.CustomerNo}\n" \
                              f"Customer Name :  {obj_roomAllocated.AllocatedCustomer.CustomerName}\n" \
                              f"Current Date and Time is {now}"
                # Writes specified string to the file
                file.write(add_to_file + "\n")

            # Closing the file
            file.close()
            # Display file saved message
            print("File saved as 'LHMS_764706455.txt' under Documents folder")
        # Display NameError message.
    except NameError as d:
        print(d)
        print("Please try again")
        # Display IOError message.
    except IOError as e:
        print(e)
        print("Please try again")


# Method to show room allocations from file
def show_room_allocation_from_file():
    global filePath
    # File not found exception, unauthorized access exception.
    try:
        # Display 'show the room allocations from a file' choice selected.
        print("You have selected 'SHOW THE ROOM ALLOCATIONS FROM A FILE' from menu")
        print("***********************************************************************************")
        with open(filePath, "r") as file:
            # Declare new object for reading file
            lines = file.readlines()
            for line in lines:
                print(line.strip())
        # Display IOError message.
    except IOError as f:
        print(f)
        print("Please try again")
        # Display EOFError message.
    except EOFError as g:
        print(g)
        print("Please try again")


def back_up():
    global filePath, filePathBackUp
    try:
        print("You have selected 'BACKUP' from menu")
        print("***********************************************************************************")
        while os.path.exists(filePathBackUp):
            print("'LHMS_backup.txt' file already exist\nExisting file will be deleted")
            os.remove(filePathBackUp)

        os.rename(filePath, filePathBackUp)
        print("Now your file 'LHMS.txt' is saved as 'LHMS_backup.txt'\n" "under Documents folder and original file will"
              " be deleted")
        # Display FileNotFoundError message.
    except FileNotFoundError as h:
        print(h)
        print("Please try again")


if __name__ == '__main__':
    main()
