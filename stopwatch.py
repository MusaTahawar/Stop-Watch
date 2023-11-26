import time

def stopwatch():
    start_time = 0
    elapsed_time = 0
    running = False

    while True:
        user_input = input("Enter 'start' to begin, 'stop' to end, or 'quit' to exit: ").lower()

        if user_input == 'start' and not running:
            start_time = time.time() - elapsed_time
            running = True
            print("Stopwatch started!")

        elif user_input == 'stop' and running:
            elapsed_time = time.time() - start_time
            running = False
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            
        elif user_input == 'quit':
            print("Exiting the stopwatch...")
            break

        else:
            print("Invalid input. Please enter 'start', 'stop', or 'quit'.")

stopwatch()
