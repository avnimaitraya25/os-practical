class Process:
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst
        self.start = 0
        self.finish = 0
        self.waiting = 0
        self.turnaround = 0

def fcfs(processes):
    processes.sort(key=lambda p: p.arrival)
    current_time = 0
    gantt = []

    for p in processes:
        if current_time < p.arrival:
            current_time = p.arrival
        p.start = current_time
        p.finish = current_time + p.burst
        p.waiting = p.start - p.arrival
        p.turnaround = p.finish - p.arrival
        current_time = p.finish
        gantt.append((p.pid, p.start, p.finish))
    return gantt
