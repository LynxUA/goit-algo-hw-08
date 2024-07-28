import heapq

def min_cost_to_connect_cables(lengths):
    heapq.heapify(lengths)
    
    total_cost = 0

    while len(lengths) > 1:
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        combined_length = first + second
        
        total_cost += combined_length
        
        heapq.heappush(lengths, combined_length)
    
    return total_cost

cable_lengths = [4, 3, 2, 6]
print(min_cost_to_connect_cables(cable_lengths))
