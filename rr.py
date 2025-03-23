def round_robin(processes, quantum):
    from collections import deque
    processes.sort(key=lambda p: p.arrival)
    queue = deque()
    time = 0
    i = 0
    completed = 0
    gantt = []
    n = len(processes)

    while completed < n:
        while i < n and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1
        if queue:
            p = queue.popleft()
            if p.remaining == p.burst:
                p.start = time
            exec_time = min(p.remaining, quantum)
            start_time = time
            time += exec_time
            p.remaining -= exec_time
            if p.remaining == 0:
                p.finish = time
                p.waiting = p.finish - p.arrival - p.burst
                p.turnaround = p.finish - p.arrival
                completed += 1
            else:
                while i < n and processes[i].arrival <= time:
                    queue.append(processes[i])
                    i += 1
                queue.append(p)
            gantt.append((p.pid, start_time, time))
        else:
            time += 1
    return gantt