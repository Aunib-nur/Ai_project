1. Introduction
The Bus Routes Problem is a classic  application of graph search techniques used in Artificial Intelligence and algorithm design. The goal is to determine the minimum number of buses required to travel from a given source bus stop to a target bus stop. Each bus route is represented as a circular path containing several stops, and a traveler may transfer between buses at any common stop.
This problem models real-world public transportation navigation and demonstrates how Breadth-First Search (BFS) can be used to compute shortest-path solutions in unweighted graphs.
2. Theory: Breadth‑First Search (BFS)
Breadth-First Search (BFS) is a graph traversal algorithm that explores all nodes at the present depth before moving on to nodes at the next level.
Why  we used BFS :
Each bus ride represents a uniform cost.
Transfers between buses represent graph edges.
BFS guarantees the minimum number of bus transfers.
BFS in this context:
Nodes → Bus stops
Edges → Reaching new stops through a bus route
Cost → Number of bus routes used
Because all "edges" have equal weight, BFS is optimal for solving this type of transportation shortest-path problem.
3. Objectives
To represent bus routes and stops as a graph.
To implement an efficient BFS algorithm to compute the minimum number of buses needed to travel from source to target.
To create a mapping between stops and buses to enable fast traversal.
To determine when the destination is unreachable.
To develop practical understanding of BFS and real-world graph modeling.


4. Algorithm
Algorithm: Minimum Bus Transfers (BFS-Based Solver)
Check Trivial Case: If source == target, return 0.
Build Stop-to-Bus Map: Create a dictionary where each stop maps to all buses passing through it.
Initialize BFS:
Start queue with (source_stop, 0 buses_taken)
Maintain two visited sets:
visited_buses → Avoid reboarding same bus
visited_stops → Avoid revisiting stops
BFS Traversal:
Pop a stop from queue
Explore all buses that go through this stop
For each unvisited bus:
Mark the bus as visited
Traverse all stops that this bus can reach
If a stop == target → return buses_taken + 1
Else enqueue the stop with incremented bus count
If queue empties without reaching target: Return -1 (destination unreachable)
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

# Now create input and call the function:
routes = [[1,2,7], [3,6,7]]
source = 1
target = 6

sol = Solution()
print(sol.numBusesToDestination(routes, source, target))  # <-- should print 2
6. Sample Input and Output
Input:
routes = [[1,2,7], [3,6,7]]
source = 1
target = 6
Output:
2
8. Conclusion
In this work, the BFS algorithm was successfully applied to determine the minimum number of bus transfers required to travel between two stops. The problem was modeled as a graph where stops and bus routes form interconnected nodes. BFS proved optimal for this unweighted shortest‑path scenario
BFS is effective for transportation network problems.
Mapping entities (stops → buses) is crucial for fast traversal.
Python data structures such as dictionaries, sets, and queues enable efficient state exploration
