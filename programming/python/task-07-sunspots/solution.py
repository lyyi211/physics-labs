from pathlib import Path

import matplotlib.pyplot as p

def read_data():
    months = []
    sunspots = []
    with open(Path(__file__).with_name("sunspots.txt"), 'r', encoding='utf-8-sig') as f:
        for line in f:
            parts = line.strip().split()
            months.append(int(parts[0]))
            sunspots.append(float(parts[1]))
    return months, sunspots

def all_sunspots(months, sunspots):
    p.figure(figsize=(12, 5))
    p.plot(months, sunspots)
    p.xlabel("Months")
    p.ylabel("Sunspot count")
    p.title("Sunspot count by month")
    p.grid(True)
    p.show(block=False)

def first_1000(months, sunspots):
    p.figure(figsize=(12, 5))
    p.plot(months[:1000], sunspots[:1000])
    p.xlabel("Months")
    p.ylabel("Sunspot count")
    p.title("First 1000 observations")
    p.grid(True)
    p.show(block=False)

def moving_average(months, sunspots, r=5):
    moving_avg = []
    for k in range(len(sunspots)):
        if k >= r and k + r < len(sunspots):
            suma = sum(sunspots[k + m] for m in range(-r, r + 1))
            Y_k = suma / (2 * r + 1)
        else:
            Y_k = None
        moving_avg.append(Y_k)

    p.figure(figsize=(12, 5))
    p.plot(months[:1000], sunspots[:1000], label="Перші 1000")
    p.plot(months[:1000], moving_avg[:1000], label="Moving average", linewidth=2)
    p.xlabel("Months")
    p.ylabel("Sunspot count")
    p.title("First 1000 observations and moving average")
    p.grid(True)
    p.legend()
    p.show(block=False)

months, sunspots = read_data()
all_sunspots(months, sunspots)
first_1000(months, sunspots)
moving_average(months, sunspots)
