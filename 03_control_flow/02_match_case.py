command = "start"

match command:
    case "start":
        print("Starting the process...")
    case "stop":
        print("Stopping the process...")
    case "pause":
        print("Pausing the process...")
    case _:
        print("Unknown command.")