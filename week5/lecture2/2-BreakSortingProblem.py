def two_break_sorting_problem(P, Q):
    seqs = []

    # START FROM HERE - making functions

    return [P]

def edge_to_point(e):
    if e > 0:
        return [2*e-1, 2*e]
    else:
        return [-2*e, -2*e-1]

def points_to_edges(points):
    if points[0] > points[1]:
        return - points[0] // 2
    else:
        return points[1] // 2

def cycles_to_edges(cycles):
    edges = []
    for cycle in cycles:
        for i in range(len(cycle)):
            prev = cycle[i-1]
            cur = cycle[i]

            edges.append([edge_to_point(prev)[1], edge_to_point(cur)[0]])
    
    return edges

def edge_intersect(edges, i1, i2, i3, i4):
    for i in range(len(edges)):
        if i1 in edges[i]:
            edges[i][edges[i].index(i1) - 1] = i3
        elif i4 in edges[i]:
            edges[i][edges[i].index(i4) - 1] = i2
    return edges


def adjacent_node(e):
    if e % 2 == 0:
        return e - 1
    else:
        return e + 1


def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        chromosome.append(points_to_edges([cycle[i], cycle[i+1]]))
        
    return chromosome

def edges_to_cycles(edges):
    dp = [0] * len(edges)
    cycles = []

    for i in range(len(edges)):
        print(i)
        if dp[i] == 0:
            startPoint = edges[i][0]
            cur = edges[i][1]
            next = adjacent_node(cur)
            cycle = []
            dp[i] = 1

            while next != startPoint:
                for j in range(i+1, len(edges)):
                    if dp[j] == 1:
                        continue
                    
                    if next == edges[j][0]:
                        cycle.append(cur)
                        cycle.append(edges[j][0])
                        cur = edges[j][1]
                        next = adjacent_node(cur)
                        dp[j] = 1
                        break
                print(startPoint, cur, next)
                if startPoint == 14 and next == 68:
                    exit()
            
            cycle.append(cur)
            cycle.append(startPoint)
            cycles.append(cycle_to_chromosome(cycle))
    return cycles


def two_break_on_genome(P, i1, i2, i3, i4):
    edges = cycles_to_edges(P)
    print('edges', edges)
    new_edges = edge_intersect(edges, i1, i2, i3, i4)
    print('new_edges', new_edges)
    new_P = edges_to_cycles(new_edges)
    print('new_P', new_P)
    
    return new_P


def print_result(ress):
    for res in ress:
        output = ""
        print(res)
        for cycle in res:
            output += "("
            R = []
            for ele in cycle:
                if ele > 0:
                    R.append(f"+{ele}")
                else:
                    R.append(f"{ele}")
            output += " ".join(R) + ")"
        print(output)
a = list(map(int, "+26 +53 +56 -8 +50 +13 +5 -32 -52 -64 -60 -41 -6 +20 -2 -44 -4 +59 +42 +22 +38 -57 -18 +66 +45 +16 +48 +43 +10 -61 -21 -62 -49 -27 +1 +36 +40 -9 -54 +30 +35 -24 +25 -34 -3 +15 -19 -58 -31 +46 +65 +55 -39 +12 +17 -29 -28 +63 -33 -37 -47 -11 -23 +51 +14 +7".split()))


print_result([two_break_on_genome([a], 86, 19, 67, 6)])

fn = "1.txt"
f = open(f"./data/{fn}", "r")
reads = f.readline().strip().lstrip("(").rstrip(")").split(")(")
P = [ list(map(int, read.split())) for read in reads ]
reads = f.readline().strip().lstrip("(").rstrip(")").split(")(")
Q = [ list(map(int, read.split())) for read in reads ]

# ress = two_break_sorting_problem(P, Q)
# print_result(ress)
