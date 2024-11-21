# Postal Office Queue Simulation README

## Overview

This program simulates the process of managing a client queue at a postal office. The simulation includes functionality for adding clients to a queue, removing clients, displaying the queue, and calculating the wait time for the last client. 
The program provides an interactive interface where the user can select various actions to simulate postal office operations.

## Features

1. **Add Clients**: Randomly generate clients with ages between 16 and 99. The service time for each client varies depending on their age group:
    - Clients aged 16-34: Service time between 1 and 3 minutes.
    - Clients aged 35-64: Service time between 10 and 15 minutes.
    - Clients aged 65-99: Service time between 20 and 30 minutes.
   
2. **Remove Clients**: Clients can be removed from the queue after being served.

3. **Display Queue**: The current client queue can be displayed, showing each client's ID, age, and service time.

4. **Last Client's Wait Time**: The program calculates and displays the wait time for the last client in the queue based on the service times of the clients ahead of them.

5. **Simulation**: Simulate adding and processing multiple clients in a queue.Clients are added to the queue in batches, and the queue is processed by removing one client at a time, with service times being printed.

## Setup

1. Ensure you have Python installed (Python 3.x recommended).
2. Save the script as a `.py` file on your local machine.
3. Run the script in your terminal or command prompt.

## Usage Instructions

1. **Start the Program**: Upon running the program, the following menu options will appear:

    ```
    Welcome to the postal office, choose an option:
    1 - Add clients to the queue
    2 - Remove a client from the queue
    3 - Display the queue
    4 - Next client's wait time
    5 - Exit
    6 - Begin simulation
    ```

2. **Option 1 - Add Clients**: This option adds clients to the queue. You can add 15 clients at a time. Each client is generated with a random age and service time based on their age group.

3. **Option 2 - Remove a Client**: Removes the client at the front of the queue, simulating the completion of their service.

4. **Option 3 - Display the Queue**: Displays the current clients in the queue, showing their ID, age, and service time.

5. **Option 4 - Next Client's Wait Time**: Calculates and displays the estimated wait time for the last client in the queue based on the sum of service times of the clients ahead of them.

6. **Option 5 - Exit**: Exits the program.

7. **Option 6 - Begin Simulation**: Runs the simulation where clients are added and processed in a sequence. The system processes each client in the queue and prints details about each client as they are served.

## Code Breakdown

- **client_generator()**: Randomly generates a client’s age and service time based on the age.
- **add_clients(num_clients)**: Adds `num_clients` (default 15) to the queue with randomly generated attributes.
- **remove_client()**: Removes the client at the front of the queue.
- **display_queue()**: Displays all the clients currently in the queue, showing their ID, age, and service time.
- **last_client_wait()**: Calculates and displays the wait time for the last client in the queue based on the sum of service times of clients ahead of them.
- **simulator()**: Runs a simulation where 3 clients are added to the queue, and the queue is processed until empty.

## Example of Usage

### Example Interaction:

```
Welcome to the postal office, choose an option:
1 - Add clients to the queue
2 - Remove a client from the queue
3 - Display the queue
4 - Next client's wait time
5 - Exit
6 - Begin simulation
Choose an option: 1

Client 1 with age 25 added to the queue. Service time: 2 minutes.
Client 2 with age 40 added to the queue. Service time: 14 minutes.
Client 3 with age 67 added to the queue. Service time: 27 minutes.
----------
Choose an option: 3

Current queue:
Client 1: Age 25, Service time 2 minutes
Client 2: Age 40, Service time 14 minutes
Client 3: Age 67, Service time 27 minutes
```

### Example Simulation:

```
Welcome to the postal office, choose an option:
1 - Add clients to the queue
2 - Remove a client from the queue
3 - Display the queue
4 - Next client's wait time
5 - Exit
6 - Begin simulation
Choose an option: 6

Client 1 with age 28 added to the queue. Service time: 2 minutes.
Client 2 with age 55 added to the queue. Service time: 14 minutes.
Client 3 with age 72 added to the queue. Service time: 24 minutes.
----------
Processing Client 1 with age 28, service time: 2 minutes.
Client 1 with age 28 removed from the queue.
Processing Client 2 with age 55, service time: 14 minutes.
Client 2 with age 55 removed from the queue.
Processing Client 3 with age 72, service time: 24 minutes.
Client 3 with age 72 removed from the queue.

All clients processed. End of simulation.
```

## Dependencies

- The script uses Python’s built-in `random` and `time` modules for random number generation and pausing between actions.

## Modifications & Customization

- **Add Clients**: Modify the `add_clients` function to change the number of clients added at a time or adjust client age and service time ranges.
- **Simulation Behavior**: Adjust the simulation speed by changing the `time.sleep()` duration in the `simulator()` and other related functions.
