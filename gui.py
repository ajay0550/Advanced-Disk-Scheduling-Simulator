import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from disk_scheduler import fcfs, sstf, scan, c_scan  # Import scheduling functions

def run_algorithm():
    try:
        requests = list(map(int, entry_requests.get().split(",")))
        start = int(entry_start.get())
        algo = algo_var.get()

        if algo == "FCFS":
            sequence, time = fcfs(requests, start)
        elif algo == "SSTF":
            sequence, time = sstf(requests, start)
        elif algo == "SCAN":
            sequence, time = scan(requests, start, disk_size=200, direction="left")
        elif algo == "C-SCAN":
            sequence, time = c_scan(requests, start, disk_size=200)
        else:
            raise ValueError("Invalid Algorithm Selected")

        # Performance Metrics
        avg_seek_time = round(time / len(requests), 2) if requests else 0  # Avoid division by zero
        throughput = round(len(requests) / time, 4) if time != 0 else 0  # Avoid division by zero

        result_label.config(
            text=f"Seek Sequence: {sequence}\nTotal Seek Time: {time}\n"
                 f"Avg Seek Time: {avg_seek_time}\nThroughput: {throughput}"
        )

        # Plot Seek Sequence Graph
        plt.figure(figsize=(6, 4))
        plt.plot(sequence, range(len(sequence)), marker='o', linestyle='-', color='b', label="Disk Head Movement")
        plt.xlabel("Disk Position")
        plt.ylabel("Request Order")
        plt.title(f"{algo} Seek Sequence")
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers separated by commas.")

# Create GUI window
root = tk.Tk()
root.title("Disk Scheduling Simulator")
root.geometry("400x350")

# Input fields
tk.Label(root, text="Enter Disk Requests (comma-separated):").pack()
entry_requests = tk.Entry(root)
entry_requests.pack()

tk.Label(root, text="Enter Start Position:").pack()
entry_start = tk.Entry(root)
entry_start.pack()

# Algorithm selection dropdown
tk.Label(root, text="Select Algorithm:").pack()
algo_var = tk.StringVar(root)
algo_var.set("FCFS")  # Default selection
algo_menu = tk.OptionMenu(root, algo_var, "FCFS", "SSTF", "SCAN", "C-SCAN")
algo_menu.pack()

# Run button
run_button = tk.Button(root, text="Run", command=run_algorithm)
run_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
