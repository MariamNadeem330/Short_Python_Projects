
command = ""
started = False
while True:
    command = input("Enter command(write help if u want to see the options and then follow the instructions):\n")
    if command == 'start':
        if started:
            print("Car has already started.")
        else:
            started = True
            print("Car started! ready to go...")
    elif command == 'stop':
        if not started:
            print("Car has already stopped.")
        else:
            started = False
            print("Car stopped!")
    elif command == 'quit':
        break
    elif command == 'help':
        print("start - to start the car.")
        print("stop - to stop the car. ")
        print("Quit - to exit. ")
    else:
        print("Sorry! I don't understand that.")

