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
