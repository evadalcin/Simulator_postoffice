import random
import time

queue = []
client_counter = 0

def client_generator():
    #client_age = (map(int,(input("Enter a range separate by a space for the range of client ages: ").split(" "))))
    #client_age = random.randint(next(client_age), next(client_age))
    client_age = random.randint(16, 99)
    if client_age < 35:
        service_time = random.randint(1, 3)
    elif 35 <= client_age < 65:
        service_time = random.randint(10, 15)
    else:
        service_time = random.randint(20, 30)
    return [client_age, service_time]

def add_clients(num_clients):
    global client_counter
    for _ in range(num_clients):
        client = client_generator()
        client_counter += 1
        queue.append((client_counter, client))
        print(f"Client {client_counter} with age {client[0]} added to the queue. Service time: {client[1]} minutes.")
        time.sleep(2)
    print("----------")

def remove_client():
    if queue:
        removed_client = queue.pop(0)
        print(f"Client {removed_client[0]} with age {removed_client[1][0]} removed from the queue.")
    else:
        print("No clients in the queue to remove.")

def display_queue():
    if queue:
        print("Current queue:")
        for client in queue:
            print(f"Client {client[0]}: Age {client[1][0]}, Service time {client[1][1]} minutes")
    else:
        print("The queue is empty.")

def last_client_wait():
    if queue:
        last_client = queue[-1]
        wait_time = sum(client[1][1] for client in queue[:-1])
        print(f"The last client in the queue is Client {last_client[0]} with age {last_client[1][0]}, and will wait for {wait_time} minutes.")

def simulator():
    # n = int(input("Enter the number of clients to simulate: "))
    # for i in range(n):
            add_clients(3)
            while queue:
                current_client = queue[0]
                print(f"Processing Client {current_client[0]} with age {current_client[1][0]}, service time: {current_client[1][1]} minutes.")
                time.sleep(2)

                remove_client()

            print("All clients processed. End of simulation.")




while True:
    print("Welcome to the postal office, choose an option:")
    print("1 - Add clients to the queue")
    print("2 - Remove a client from the queue")
    print("3 - Display the queue")
    print("4 - Next client's wait time")
    print("5 - Exit")
    print("6 - Begin simulation")

    user_input = input("Choose an option: ")

    if user_input == "1":
        add_clients(15)
    elif user_input == "2":
        remove_client()
    elif user_input == "3":
        display_queue()
    elif user_input == "4":
        last_client_wait()
    elif user_input == "5":
        print("Exiting...")
    elif user_input == "6":
        simulator()
    else:
        print("Invalid option")

