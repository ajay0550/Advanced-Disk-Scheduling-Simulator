from disk_scheduler import fcfs

# Sample disk requests and start position
requests = [98, 183, 37, 122, 14, 124, 65, 67]
start = 53

sequence, time = fcfs(requests, start)

print("Seek Sequence:", sequence)
print("Total Seek Time:", time)
