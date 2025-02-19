def fcfs_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])

    n = len(processes)

    ct = [0] * n  # Completion time
    tat = [0] * n  # Turnaround time
    wt = [0] * n  # Waiting time

    # First process
    ct[0] = processes[0][1] + processes[0][2]  # Completion time = Arrival time + Burst time

    for i in range(1, n):
        ct[i] = max(ct[i - 1], processes[i][1]) + processes[i][2]

    for i in range(n):
        tat[i] = ct[i] - processes[i][1]  # Turnaround time = Completion time - Arrival time
        wt[i] = tat[i] - processes[i][2]  # Waiting time = Turnaround time - Burst time

    print("Process\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i][0]}\t{tat[i]}\t{wt[i]}")


# List of processes (Process ID, Arrival Time, Burst Time)
process_list = [
    ('P1', 2, 5),
    ('P2', 6, 3),
    ('P3', 4, 4)
]

# Run the scheduling function
fcfs_scheduling(process_list)

