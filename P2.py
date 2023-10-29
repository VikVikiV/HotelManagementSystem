# *
# * Project Name: Hotel Management Application System for 'LANGHAM Hotels'
# * Author Name: Jimmy Connors
# * Date: 23/09/2022
# * Application Purpose:Develop software application for 'LANGHAM Hotels' to manage their day-to-day operations
# * like the allocation of rooms, deallocation of rooms, displaying the status of rooms, and other functionality.
# *

import os.path
from datetime import datetime
try:
    from RoomModule import Room
    from CustomerModule import Customer
    from RoomAllocationModule import RoomAllocation
except ImportError as ex:
    print(ex)
    print("Please check your modules")

# Custom Main Class - Program
# Variables declaration and initialisation
# Initialising array of class Room
listOfRooms = []
# Initialisng integer variable for number of room
noOfRoom = 0
# Create a list of room allocations
listOfRoomAllocations = []
# Initialising file path for both save allocations and back up file
filePath = ""
filePathBackUp = ""

# Main function
def main():
    global noOfRooms, filePath, filePathBackUp

    # Initialising and declaring path for location of the file
    folderPath = os.path.expanduser("~/Documents")
    # Create specific file for both save allocations and back up
    filePath = os.path.join(folderPath, "LHMS_764706455.txt")
    filePathBackUp = os.path.join(folderPath, "LHMS_764706455_Backup_Date_Time.txt")
    # Display main menu
    menu()

# Method for main menu
def menu():
    # Format exception, invalid operation exception
    try:
        # Initialise integer variable
        choice = - 1;
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
            print("3. Display Rooms Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocataion Details")
            print("6. Billing & De-Allocation")
            print("7. Save The Room Allocation to a File")
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
                Add_Room()
            elif choice == 2:
                # Deleting Rooms
                Delete_Room()
            elif choice == 3:
                # Displaying Room Details
                Display_Rooms_Details()
            elif choice == 4:
                # Allocating Rooms
                Allocate_Rooms()
            elif choice == 5:
                # Displaying Room Alocations Details
                Display_Room_Allocation_Details()
            elif choice == 6:
                # Billing & De-Allocation
                Billing_DeAllocation()
            elif choice == 7:
                # Save The Room Allocation to a File
                Save_Room_Allocation_to_File()
            elif choice == 8:
                # Show The Room Allocation from a File
                Show_Room_Allocation_to_File()
            elif choice == 9:
                # Backup
                Back_Up()
            else:
                print("Please choose (0-9)")

    except SyntaxError as e:
        print(f"Syntax error :{e}")
    except TypeError as e:
        print(f"Type error :{e}")
    except ValueError as e:
        print(f"Value error :{e}")

def Add_Room():
    global noOfRoom, listOfRooms
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
        if len(listOfRooms) > 0:
            y = len(listOfRooms)
        else:
            y = 0
        for x in range(noOfRoom):
            room = Room()
            listOfRooms.append(room)
            # Use for loop to ask user to input room details and save it
        for i in range(y, y + noOfRoom):
            obj_room = listOfRooms[i]
            # Ask user to enter room number
            print(f"Room Allocation {i + 1}: ")
            # Convert user input to integer and save it
            obj_room.RoomNo = int(input(f"Please enter room number {i + 1}: "))
            # Declare room allocation status to false(not allocated)
            obj_room.IsAllocated = False
            # Save the new room object to array of Room
            listOfRooms[i] = obj_room
            # If condition to check the same room number exist or not when there is more than 1 room added
            if (i > 0):
                # Use for loop to check the listOfRooms with the same room number
                for j in range(i):
                    # Use while loop to check the user input room number is equal to previous inputs
                    while listOfRooms[i].RoomNo == listOfRooms[j].RoomNo:
                        # Display message for the same room exist and ask to input new room number
                        print(f"Same room number already exist")
                        obj_room.RoomNo = int(input(f"Please enter a new room number {i + 1}: "))
                        # Declare room allocation status to false(not allocated)
                        obj_room.IsAllocated = False
                        # Save the new room object to array of Room
                        listOfRooms[i] = obj_room
    except ValueError as e:
        print(f" Value Error: {e} ")
        print("Invalid input, Please try again ")
        add_room()
def Delete_Room():
    global listOfRooms
    # If condition to check there is any rooms to display
    if listOfRooms:
        # Display 'display rooms' choice selected
        print("You have selected 'DELETE ROOMS' from menu")
        print("***********************************************************************************")
        room_Number = int(input("Please enter the room number that you want to delete"))
        try:
            for obj_room in listOfRooms:
                if obj_room.RoomNo == room_Number:
                    listOfRooms.remove(obj_room)
        except ValueError as e:
            print(f"Value Error : {e}")
            print("Invalid input, Please try again")

        print(f"Following rooms have been deleted")
    # If nothing to display, display following message
    else:
        print("No rooms to delete\nPlease add rooms first")
def Display_Rooms_Details():
    global listOfRooms
    # If condition to check there is any rooms to display
    if listOfRooms:
        # Display 'display rooms' choice selected
        print("You have selected 'DISPLAY ROOMS' from menu")
        print("***********************************************************************************")
        print(f"Following rooms have been added")
        # Use foreach loop to display details of each room
        for obj_room in listOfRooms:
            print(f"Room Number :  {obj_room.RoomNo}")
        # If nothing to display, display following message
    else:
        print("No rooms to display\nPlease add rooms first")

# Method to allocate rooms to customer
def Allocate_Rooms():
    global noOfRoom, listOfRooms, listOfRoomAllocations

    # Format exception, Invalid operation exception
    try:

        # Display 'allocate rooms' choice selected
        print("You have selected 'ALLOCATE ROOMS' from menu")
        # Ask user to input how many rooms to allocate
        # Declare integer variable, convert user input to integer and save it
        allocate_room = int(input("How many rooms would you like to allocate?: "))
        # Use while loop to check user input is correct
        while allocate_room > len(listOfRooms):

            # Display input is incorrect message and give another chance
            print(f"You cannot allocate more rooms than total number of rooms in the Hotel\n" +
                  f"Please enter number between 1-{len(listOfRooms)}: ")
            allocate_room = int(input("How many rooms would you like to allocate?: "))

        # Display how many room will be allocated
        print(f"You are allocating {allocate_room} room(s)")
        # Use for loop to each room and customer details for allocation
        i = 0
        for i in range(allocate_room):

            print("***********************************************************************************")
            # Create new object called roomAllocation for class RoomAllocation
            roomAllocation = RoomAllocation()
            # Create new object called customer for class Customer
            customer = Customer()
            # Display allocation number
            print(f"Room Allocation {i + 1}:")
            # Ask user to input room number to search
            # Declare integer variable, convert user input to integer and save it
            searchRoom = int(input("Please search Room Number to allocate: "))
            # Use for loop to search matching room from list of rooms that has been added
            j = 0
            for j in range(len(listOfRooms)):

                # If condition to find matching room number
                # If room number matches, display found message
                if searchRoom == listOfRooms[j].RoomNo:

                    # Display matching room found message
                    print("Found matching room number to allocate")
                    # If condition to check for room is already allocated or not
                    # If room is not allocated, display allocation message
                    if listOfRooms[j].IsAllocated == False:

                        # Display room searched is empty
                        print(f"Room {listOfRooms[j].RoomNo} is empty ")
                        # Ask user to enter customer number
                        # Convert user input to integer and save it
                        customer.CustomerNo = int(input("Please enter Customer Number to allocate: "))
                        # Ask user to enter customer name
                        customer.CustomerName = input("Please enter Customer Name to allocate: ")
                        # Change room allocation status to allocated
                        listOfRooms[j].IsAllocated = True
                        # Display allocation done message
                        print("Allocation has been done")
                        # Save room number for allocation and customer details into the object
                        roomAllocation.AllocatedRoomNo = searchRoom
                        roomAllocation.AllocatedCustomer = customer
                        # Add object to the list
                        listOfRoomAllocations.append(roomAllocation)
                        break;

                    # If room is already allocated, display message: room is occupied
                    else:

                        print(f"Room {listOfRooms[j].RoomNo} is already occupied\n" +
                              f"Please enter another room to allocate")
                        # Give user another chance
                        i -= 1
                        break;

                # For no match found
                else:

                    # If no matching room number found, display message
                    while j == len(listOfRooms) - 1:

                        print("Could not find matching room number to allocate\n" +
                              "Please enter correct room number or add room first")
                        # Give user another chance
                        i -= 1
                        break;
            i += 1
    except ValueError:
        # Display value exception message
        print(" Ivalid Input. Please try again. ")
        # Call the function again to give user another chance
        Allocate_Rooms()

    except IOError:
        # Display invalid operation exception message
        print(" Ivalid Input. Please try again. ")
        # Call the function again to give user another chance
        Allocate_Rooms()

# Method to display room allocations details
def Display_Room_Allocation_Details():
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


def Billing_DeAllocation(): # Format exception, invalid operation exception
    try:
        # Display 'deallocate rooms' choice selected
        print("You have selected 'DEALLOCATE ROOMS' from menu")
        # Ask user how many rooms to deallocate
        print("How many rooms would you like to deallocate?: ")
        # Declare integer variable, convert user input to integer and save it
        int(DeAllRoom) > listOfRoomAllocations.count()
        # Use while loop to check user input is correct (needs to be less than number of rooms allocated)
        while (deAllRoom > listOfRoomAllocations.Count()):
            # Display input is incorrect message and give user another chance
            print(f"You cannot deallocate more rooms than you have allocated\n" +
                        f"Please enter number between 1-{listOfRoomAllocations.Count}: ")
            deAllRoom = int(input())

            # Display how many rooms will be deallocated
            print((f"You are deallocating {deAllRoom} room(s)"))
            # Use for loop for deallocating each room
            for i in range(deAllRoom):
                # Display each deallocation
                print("***********************************************************************************")
                print(f"Room Deallocation {i + 1}:")
                # Ask user to enter room number to deallocate
                print("Please search Room Number to deallocate: ")
                # Convert user input to integer and save it
                searchRoom = int(input())
                # Use for loop to search matching room from list of rooms
                for i in range(noOfRoom):
                    # If condition to find matching room number
                    # If room number matches, display found message
                    if searchRoom == listOfRooms[j].RoomNo:
                        # Display matching room found message
                        print("Found matching room number to deallocate")
                        # If condition to check for room is already allocated or not
                        # If room is allocated, display deallocation message
                        if listOfRooms[j].IsAllocated == True:
                            # Display room searched is occupied
                            print("Room {listOfRooms[j].RoomNo} is occupied")
                            # Change room allocation status to deallocated
                            listOfRooms[j].IsAllocated == False
                            # Display deallocation done message
                            print(f"Room {searchRoom} has been deallocated")
                            # Find the room number to deallocate from the list and remove
                            RoomAllocation = listOfRoomAllocations.find(x in x.AllocatedRoomNo == searchRoom)
                            listOfRoomAllocations.remove(RoomAllocation)
                            break;

                            # If room is not allocated, display room not allocated message, and give user another chance
                        else:
                            print((f"Room {listOfRooms[j].RoomNo} is empty" +
                                    f"\nPlease find another room to deallocate"))
                            # Give user another chance
                            i -= 1
                            break;
                    # For no match found
                    else:
                        # If no matching room number found, display message, and give user another chance
                        while (j == noOfRoom - 1):
                            print(("Could not find matching room number to deallocate\n" +
                                    "Please enter correct room number or add room first"))
                            # Give user another chance
                            i -= 1
                            break;

    except SyntaxError as ex:
        # Display format exception message
        print(ex)
        print("Please try again")
        # Call the function again to give user another chance
        Billing_DeAllocation()
    except IOError as ex:
        # Display invalid operation exception message
        print(ex)
        print("Please try again")
        # Call the function again to give user another chance
        Billing_DeAllocation()

# Method to save the room allocations to file
def Save_Room_Allocation_to_File():
    global filePath

    # Unauthorized access exception
    try:

        # Display 'save the room allocations to a file' choice selected
        print("You have selected 'SAVE THE ROOM ALLOCATIONS TO A FILE' from menu")
        print("***********************************************************************************")
        # Initialise FileStream class with specified path, creation mode, and write permission
        with open(filePath, "w")as file:
            # Save current date and time
            now = datetime.now()
            # Foreach loop to write all the details for room allocations and customer, and adds to file
            for obj_room.Allocated in listOfRoomAllocations:

                add_to_file = f"***********************************************************************************" \
                              f"Allocated Room Number :  {obj_room.AllocatedRoomNo}\n" \
                              f"Customer Number :  {obj_room.AllocatedCustomer.CustomerNo}\n" \
                              f"Customer Name :  {obj_room.AllocatedCustomer.CustomerName}\n" \
                              f"Current date and time is {now}"
                    # Writes specified string to the file
                file.write(add_to_file + "\n")

            # Closing the file
            file.close()
            # Display file saved message
            print("File saved as 'lhms_764703866.txt' under Documents folder")

    except IOError as ex:
        print(ex)
        print("Please try again")
    except FileNotFoundError as ex:
        print(ex)
        print("Please try again")

# Method to show room allocations from file
def Show_Room_Allocation_to_File():
    global filePath
    try:
        print("You have selected 'SHOW THE ROOM ALLOCATIONS TO A FILE' from menu")
        print("***********************************************************************************")
        with open(filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())

    except IOError as ex:
        print(ex)
        print("Please try again")
    except FileNotFoundError as ex:
        print(ex)
        print("Please try again")
    except EOFError as ex:
        print(ex)
        print("Please try again")

def Back_Up():
    global filePath, filePathBackUp
    try:
        print("You have selected 'BACKUP' from menu")
        print("***********************************************************************************")
        while os.path.exists(filePathBackUp):
            print("'lhms_backup.txt' file already exist\nExisting file will be deleted")
            os.remove(filePathBackUp)

        os.rename(filePath, filePathBackUp)
        print("Now your file 'lhms.txt' is saved as 'lhms_backup.txt'\n" +
                        "under Documents folder and orignial file will be deleted")
    except FileNotFoundError as ex:
        print(ex)
        print("Please try again")

if __name__ == '__main__':
    main()
