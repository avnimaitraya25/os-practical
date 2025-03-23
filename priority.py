def priority_scheduling(processes):
    processes.sort(key=lambda p: p.arrival)
    n = len(processes)
    completed = 0
    current_time = 0
    gantt = []
    ready_queue = []

    while completed < n:
        for p in processes:
            if p.arrival <= current_time and p not in ready_queue and p.finish == 0:
                ready_queue.append(p)
        if ready_queue:
            ready_queue.sort(key=lambda p: p.priority)
            p = ready_queue.pop(0)
            p.start = current_time
            p.finish = current_time + p.burst
            p.waiting = p.start - p.arrival
            p.turnaround = p.finish - p.arrival
            current_time = p.finish
            gantt.append((p.pid, p.start, p.finish))
            completed += 1
        else:
            current_time += 1
    return gantt
