import heapq # Priority queue implementation

def dijkstra(vertices, edges, start):
    # Initialize distances to infinity for all vertices except the start vertex
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    # Previous vertices dictionary to store the previous vertex for each visited vertex
    prev = {}

    # Priority queue to store vertices and their corresponding distances
    pq = [(0, start)]

    while pq:
        # Get the vertex with the minimum distance from the priority queue
        current_dist, current_vertex = heapq.heappop(pq)

        # Ignore outdated entries in the priority queue
        if current_dist > distances[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, edge_weight in edges[current_vertex]:
            distance = current_dist + edge_weight

            # Update the distance and previous vertex if a shorter path is found
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor)) 

    return distances, prev

def get_path(prev, start, end):
    # Reconstruct the path from the previous vertices
    path = []
    current_vertex = end

    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = prev[current_vertex]

    path.append(start)
    path.reverse()

    return path

def main():
    vertices = ['Capinopolis', 'Centralina', 'Itumbiara', 'Tupaciguara', 'Uberlandia', 'Araguari', 'Cascalho Rico', 'Grupiara',
                'Estrela do Sul', 'Romaria', 'Sao_Juliana', 'Indianapolis', 'Douradinhos', 'Monte Alegre de Minas', 'Ituiutaba']
    
    edges = {
        'Capinopolis': [('Centralina', 40), ('Ituiutaba', 30)],
        'Centralina': [('Capinopolis', 40), ('Itumbiara', 20), ('Monte Alegre de Minas', 70)],
        'Itumbiara': [('Centralina', 20), ('Tupaciguara', 55)],
        'Tupaciguara': [('Itumbiara', 55), ('Monte Alegre de Minas', 44), ('Uberlandia', 60)],
        'Uberlandia': [('Tupaciguara', 60), ('Monte Alegre de Minas', 60), ('Douradinhos', 63), ('Araguari', 30), ('Romaria', 78), ('Indianapolis', 45)],
        'Araguari': [('Uberlandia', 30), ('Cascalho Rico', 28), ('Estrela do Sul', 34)],
        'Cascalho Rico': [('Araguari', 28), ('Grupiara', 32)],
        'Grupiara': [('Cascalho Rico', 32), ('Estrela do Sul', 38)],
        'Estrela do Sul': [('Grupiara', 38), ('Romaria', 27)],
        'Romaria': [('Estrela do Sul', 27), ('Sao_Juliana', 28), ('Uberlandia', 78)],
        'Sao_Juliana': [('Romaria', 28), ('Indianapolis', 40)],
        'Indianapolis': [('Sao_Juliana', 40), ('Uberlandia', 45)],
        'Douradinhos': [('Uberlandia', 63), ('Monte Alegre de Minas', 28), ('Ituiutaba', 90)],
        'Monte Alegre de Minas': [('Douradinhos', 28), ('Ituiutaba', 85), ('Centralina', 70), ('Tupaciguara', 44)],
        'Ituiutaba': [('Monte Alegre de Minas', 85), ('Capinopolis', 30), ('Douradinhos', 90)]
    }

    while True:
        print("1. Find the shortest path")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start = input("Enter the starting vertex: ")
            end = input("Enter the destination vertex: ")

            if start in vertices and end in vertices:
                distances, prev = dijkstra(vertices, edges, start)
                shortest_distance = distances[end]

                if shortest_distance == float('inf'):
                    print("No path found.")
                else:
                    path = get_path(prev, start, end)
                    print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
                    print(f"Shortest distance: {shortest_distance}")
            else:
                print("Invalid vertices.")

        elif choice == '2':
            break

        print()

if __name__ == '__main__':
    main()
