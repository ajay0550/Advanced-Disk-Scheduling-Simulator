import matplotlib.pyplot as plt  

def fcfs(requests, start):
    seek_sequence = [start] + requests
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))
    return seek_sequence, seek_time

def sstf(requests, start):
    requests = requests[:]  
    seek_sequence = [start]
    total_seek_time = 0
    current = start

    while requests:
        closest = min(requests, key=lambda x: abs(x - current))
        total_seek_time += abs(closest - current)
        seek_sequence.append(closest)
        current = closest
        requests.remove(closest)

    return seek_sequence, total_seek_time

def scan(requests, start, disk_size=200, direction="left"):
    requests.sort()
    left = [r for r in requests if r < start]
    right = [r for r in requests if r >= start]

    seek_sequence = []
    total_seek_time = 0
    current = start

    if direction == "left":
        for r in reversed(left):
            seek_sequence.append(r)
            total_seek_time += abs(r - current)
            current = r
        seek_sequence.append(0)
        total_seek_time += current
        current = 0
        for r in right:
            seek_sequence.append(r)
            total_seek_time += abs(r - current)
            current = r
    else:
        for r in right:
            seek_sequence.append(r)
            total_seek_time += abs(r - current)
            current = r
        seek_sequence.append(disk_size - 1)
        total_seek_time += (disk_size - 1 - current)
        current = disk_size - 1
        for r in reversed(left):
            seek_sequence.append(r)
            total_seek_time += abs(r - current)
            current = r

    return seek_sequence, total_seek_time

def c_scan(requests, start, disk_size=200):
    requests.sort()
    right = [r for r in requests if r >= start]
    left = [r for r in requests if r < start]

    seek_sequence = []
    total_seek_time = 0
    current = start

    for r in right:
        seek_sequence.append(r)
        total_seek_time += abs(r - current)
        current = r

    seek_sequence.append(disk_size - 1)
    total_seek_time += (disk_size - 1 - current)
    current = 0  
    seek_sequence.append(0)

    for r in left:
        seek_sequence.append(r)
        total_seek_time += abs(r - current)
        current = r

    return seek_sequence, total_seek_time
