This is our 1st group project of Operating System, in which we have made Intelligent CPU Scheduler Simulator
In this project, we have develop a simulator for CPU scheduling algorithms (FCFS, SJF, Round Robin, Priority Scheduling) with real-time visualizations. The simulator should allow users to input processes with arrival times, burst times, and priorities and visualize Gantt charts and performance metrics like average waiting time and turnaround time.
1. Introduction
The Intelligent CPU Scheduler Simulator is designed to simulate different CPU scheduling algorithms (FCFS, SJF, Round Robin, and Priority Scheduling) with real-time visualizations. The simulator takes process details as input (arrival time, burst time, priority) and generates a Gantt chart while calculating essential performance metrics such as waiting time, turnaround time, and response time.

2. Step-by-Step Working of the Simulator
Step 1: User Input Handling
The user enters process details such as:

Process ID

Arrival Time (when the process arrives in the ready queue)

Burst Time (total execution time required)

Priority (only for priority scheduling)

Time Quantum (only for Round Robin scheduling)

The input is validated to ensure correct values (e.g., arrival times are non-negative, burst times are positive).

Step 2: Choosing the Scheduling Algorithm
The user selects one of the following CPU scheduling algorithms:

First Come First Serve (FCFS)

Processes are executed in the order they arrive.

Non-preemptive (once a process starts, it cannot be interrupted).

Shortest Job First (SJF)

The process with the shortest burst time is executed first.

Can be preemptive (SRTF) or non-preemptive.

Round Robin (RR)

Each process is assigned a fixed time quantum.

If a process does not finish within the quantum, it is moved to the back of the queue.

Preemptive (processes are interrupted after each quantum).

Priority Scheduling

The process with the highest priority (lowest number) is executed first.

Can be preemptive or non-preemptive.

Step 3: Process Scheduling and Execution
Based on the chosen algorithm, the processes are arranged in a queue for execution.

The CPU executes processes in order, updating the system clock and calculating turnaround times, waiting times, and response times.

In case of preemptive scheduling (SRTF, Priority, or Round Robin), the scheduler constantly checks for new processes or time quantum expirations.

Step 4: Gantt Chart Generation
A Gantt chart is dynamically created, showing when each process starts and ends.

This provides a visual representation of process execution.

Example Gantt Chart for Round Robin (Quantum = 4):

markdown
Copy
Edit
| P1 | P2 | P3 | P1 | P2 | P3 |
---------------------------------
0    4    8    12   16   20   24
Each process gets CPU time based on the scheduling rules.

Step 5: Performance Metrics Calculation
The simulator computes the following performance metrics:

Turnaround Time (TAT):
TAT=CompletionTime−ArrivalTime
Measures how long each process takes from arrival to completion.

Waiting Time (WT):
WT=TurnaroundTime−BurstTime
Measures the total time a process spends waiting in the ready queue.

Response Time (RT):
RT=FirstCPUExecutionTime−ArrivalTime
Time taken for the CPU to start executing a process for the first time.

CPU Utilization:=(Total CPU Time / Simulation Time) × 100
Measures how effectively the CPU is utilized.

Step 6: Displaying Results and Visualization
The final output consists of:

Gantt chart (Graphical representation of execution order).

Performance metrics table (TAT, WT, RT for each process).

Comparison of algorithms (for better decision-making).

Example Output Table:

Process	Arrival Time	Burst Time	Completion Time	Turnaround Time	Waiting Time	Response Time
P1	0	5	10	10	5	0
P2	1	3	13	12	9	3
3. Features of the Simulator
✅ Real-Time Visualization:

Gantt charts are dynamically updated as the processes execute.

✅ User-Friendly Interface:

Simple input fields for process details.

✅ Performance Analysis:

Provides efficiency metrics to compare scheduling algorithms.

✅ Supports Preemptive & Non-Preemptive Scheduling:

Allows a realistic simulation of different scenarios.

4. Future Enhancements
Dynamic process addition (Add new processes at runtime).

Multi-core CPU scheduling (Simulate modern processor behavior).

AI-based algorithm selection (Choose the best algorithm dynamically based on workload).

Cloud-based deployment (Run simulations online without installation).

5. Conclusion
The Intelligent CPU Scheduler Simulator provides a powerful interactive learning experience for understanding CPU scheduling. By implementing various algorithms and offering real-time insights, the project helps users visualize scheduling behavior and compare algorithm efficiency. Future enhancements can make it even more dynamic and applicable in real-world systems.
