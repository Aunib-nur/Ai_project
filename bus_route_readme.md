# Bus Route Finder (numBusesToDestination)

This project contains a Python solution for finding the **minimum number of buses** required to travel from a **source stop** to a **target stop**, using Breadth-First Search (BFS).

---

## 🚍 Problem Overview
Given a list of bus routes:
- Each route represents a bus and the stops it covers.
- You start from a `source` stop.
- You need to reach a `target` stop.

The challenge is to determine the **minimum number of buses** you must take to reach your destination.

If it is **not possible**, the function returns `-1`.

---

## 🧠 Approach Summary
The algorithm uses **BFS (Breadth-First Search)** because:
- Each bus route can lead to many new stops.
- BFS guarantees the shortest path in terms of number of buses.

### Key Ideas:
- Map each **stop → list of buses** that pass through it.
- Use a queue to explore stops level-by-level.
- Track visited buses and stops to avoid repetition.
- For each stop, try taking every bus that visits it.

---

## 📂 Code Implementation
```python
from collections import deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        stop_to_buses = {}
        for bus_index in range(len(routes)):
            route = routes[bus_index]
            for stop in route:
                if stop not in stop_to_buses:
                    stop_to_buses[stop] = []
                stop_to_buses[stop].append(bus_index)

        queue = deque()
        queue.append((source, 0))
        visited_buses = set()
        visited_stops = set([source])

        while queue:
            stop, buses_taken = queue.popleft()
            if stop not in stop_to_buses:
                continue
            for bus_index in stop_to_buses[stop]:
                if bus_index in visited_buses:
                    continue
                visited_buses.add(bus_index)
                for next_stop in routes[bus_index]:
                    if next_stop == target:
                        return buses_taken + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        return -1
```

---

## ▶️ Example Usage
```python
routes = [[1,2,7], [3,6,7]]
source = 1
target = 6

sol = Solution()
print(sol.numBusesToDestination(routes, source, target))
```
Output:
```
2
```
Meaning: You need **2 buses** to go from stop **1** to stop **6**.

---

## 📘 Explanation of Example
- From **stop 1**, you take bus **0** (route: [1,2,7]).
- You reach stop **7**.
- From stop **7**, take bus **1** (route: [3,6,7]).
- That bus reaches **stop 6**.

Therefore: **2 buses required**.

---

## ✅ Features
- Uses BFS for guaranteed minimum bus count
- Efficient for large datasets
- Avoids revisiting buses/stops

---

## 📄 License
This is a simple educational implementation for algorithm learning and interview practice.

---

If you want, brother, I can also create:
- A visual diagram of BFS flow
- An explanation in Bangla
- A simplified beginner version of the code.

