 
command = ""
while True:
    command = input("Enter command: ")
    if command == 'start':
        print("Car started! ready to go...")
    elif command == 'stop':
        print("Car stopped!")
    elif command == 'quit':
        break
    elif command == 'help':
        print("start - to start the car.")
        print("stop - to stop the car. ")
        print("Quit - to exit. ")
    else:
        print("Sorry! I don't understand that.")

