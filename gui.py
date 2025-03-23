class CPUSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduler Simulator")
        self.entries = []
        self.processes = []

        tk.Label(root, text="CPU Scheduler Simulator", font=("Arial", 16)).grid(row=0, column=0, columnspan=4, pady=10)

        #heading
        headers = ["Process ID", "Arrival Time", "Burst Time", "Priority"]
        for i, h in enumerate(headers):
            tk.Label(root, text=h).grid(row=1, column=i)

        #rows for process input
        for i in range(5):
            row_entries = []
            for j in range(4):
                e = tk.Entry(root, width=10)
                e.grid(row=i+2, column=j, padx=5, pady=5)
                row_entries.append(e)
            self.entries.append(row_entries)

        #Algorithm selection
        tk.Label(root, text="Algorithm:").grid(row=7, column=0, pady=10)
        self.algo_var = tk.StringVar(value="FCFS")
        algo_menu = tk.OptionMenu(root, self.algo_var, "FCFS", "SJF", "Round Robin", "Priority")
        algo_menu.grid(row=7, column=1)

        #Quantum entry for RR
        tk.Label(root, text="Quantum:").grid(row=7, column=2)
        self.quantum_entry = tk.Entry(root, width=5)
        self.quantum_entry.grid(row=7, column=3)

        #Run button
        tk.Button(root, text="Run", command=self.run_simulation).grid(row=8, column=1, columnspan=2, pady=10)

    def run_simulation(self):
        self.processes = []
        algo = self.algo_var.get()

        for row in self.entries:
            try:
                pid = int(row[0].get())
                arrival = int(row[1].get())
                burst = int(row[2].get())
                if algo == "Priority":
                    priority = int(row[3].get())
                else:
                    priority = 0  #default if we are not using priority scheduling
                self.processes.append(Process(pid, arrival, burst, priority))
            except:
                continue  #skip the incomplete or invalid rows

        if not self.processes:
            messagebox.showerror("Error", "Please enter at least one valid process")
            return

        if algo == "FCFS":
            gantt = fcfs(self.processes)
        elif algo == "SJF":
            gantt = sjf(self.processes)
        elif algo == "Round Robin":
            try:
                quantum = int(self.quantum_entry.get())
                gantt = round_robin(self.processes, quantum)
            except:
                messagebox.showerror("Error", "Enter valid quantum for RR")
                return
        elif algo == "Priority":
            gantt = priority_scheduling(self.processes)

        self.show_results(gantt)

    def show_results(self, gantt):
        avg_wait = sum(p.waiting for p in self.processes) / len(self.processes)
        avg_tat = sum(p.turnaround for p in self.processes) / len(self.processes)
        result = f"Avg Waiting Time: {avg_wait:.2f}\nAvg Turnaround Time: {avg_tat:.2f}"
        messagebox.showinfo("Results", result)

        #Gantt chart
        fig, gnt = plt.subplots()
        gnt.set_ylim(0, 10)
        gnt.set_xlim(0, max(p.finish for p in self.processes) + 2)
        gnt.set_xlabel("Time")
        gnt.set_yticks([5])
        gnt.set_yticklabels(["Processes"])
        gnt.grid(True)

        for pid, start, end in gantt:
            gnt.broken_barh([(start, end - start)], (4, 2), facecolors='tab:blue')
            gnt.text((start + end)/2 - 0.5, 5, f"P{pid}", va='center', ha='center', color='white')

        plt.show()

#running the algorithms
if __name__ == "__main__":
    root = tk.Tk()
    app = CPUSchedulerApp(root)
    root.mainloop()