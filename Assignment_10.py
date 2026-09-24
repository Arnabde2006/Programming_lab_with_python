# Lab 10 - AI Based Lab Assignment (BCACC393)
# Run the file and choose a question number from the menu.
# Q1, Q2 and Q10 open a Tkinter window (close the window to return to the menu).

import tkinter as tk
import random
import time
import heapq
from collections import deque

# =====================================================================
# Part A - GUI Based AI Applications
# =====================================================================

#Q1 - AI-Based Tic-Tac-Toe using GUI (Minimax)

WIN_LINES=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def ttt_winner(board):
    for a,b,c in WIN_LINES:
        if board[a]!=" " and board[a]==board[b]==board[c]:
            return board[a],(a,b,c)
    return None,None

def minimax(board,is_ai,depth):
    # AI plays 'O' (maximiser), human plays 'X' (minimiser)
    w,_=ttt_winner(board)
    if w=="O":
        return 10-depth
    if w=="X":
        return depth-10
    if " " not in board:
        return 0
    if is_ai:
        best=-100
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                best=max(best,minimax(board,False,depth+1))
                board[i]=" "
        return best
    best=100
    for i in range(9):
        if board[i]==" ":
            board[i]="X"
            best=min(best,minimax(board,True,depth+1))
            board[i]=" "
    return best

def ai_best_move(board):
    best_score=-100
    best_move=None
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(board,False,1)
            board[i]=" "
            if score>best_score:
                best_score=score
                best_move=i
    return best_move

def q1():
    root=tk.Tk()
    root.title("Tic-Tac-Toe - Human (X) vs AI (O, Minimax)")
    board=[" "]*9
    state={"over":False,"busy":False}
    status=tk.Label(root,text="Your turn (X)",font=("Arial",14,"bold"))
    status.grid(row=0,column=0,columnspan=3,pady=8)
    buttons=[]
    default_bg={"c":None}

    def end_check():
        w,line=ttt_winner(board)
        if w:
            state["over"]=True
            for i in line:
                buttons[i].config(bg="lightgreen")
            status.config(text="You win!" if w=="X" else "AI (O) wins!")
            return True
        if " " not in board:
            state["over"]=True
            status.config(text="It's a draw!")
            return True
        return False

    def ai_move():
        move=ai_best_move(board)
        board[move]="O"
        buttons[move].config(text="O",fg="red")
        state["busy"]=False
        if not end_check():
            status.config(text="Your turn (X)")

    def click(i):
        if state["over"] or state["busy"] or board[i]!=" ":
            return
        board[i]="X"
        buttons[i].config(text="X",fg="blue")
        if end_check():
            return
        state["busy"]=True
        status.config(text="AI is thinking...")
        root.after(300,ai_move)

    def restart():
        for i in range(9):
            board[i]=" "
            buttons[i].config(text="",bg=default_bg["c"])
        state["over"]=False
        state["busy"]=False
        status.config(text="Your turn (X)")

    for i in range(9):
        b=tk.Button(root,text="",font=("Arial",28,"bold"),width=4,height=1,command=lambda i=i:click(i))
        b.grid(row=1+i//3,column=i%3,padx=3,pady=3)
        buttons.append(b)
    default_bg["c"]=buttons[0].cget("bg")
    tk.Button(root,text="Restart",font=("Arial",12),command=restart).grid(row=4,column=0,columnspan=3,pady=8)
    root.mainloop()


#Q2 - GUI Based 8-Puzzle Solver (BFS and A*)

GOAL=(1,2,3,4,5,6,7,8,0)

def puzzle_neighbors(state):
    i=state.index(0)
    r,c=divmod(i,3)
    result=[]
    for dr,dc,name in [(-1,0,"Down"),(1,0,"Up"),(0,-1,"Right"),(0,1,"Left")]:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            j=nr*3+nc
            s=list(state)
            s[i],s[j]=s[j],s[i]
            result.append((tuple(s),f"Move tile {state[j]} {name}"))
    return result

def manhattan(state,goal=GOAL):
    total=0
    for idx,v in enumerate(state):
        if v!=0:
            g=goal.index(v)
            total+=abs(idx//3-g//3)+abs(idx%3-g%3)
    return total

def is_solvable(state):
    tiles=[x for x in state if x!=0]
    inv=sum(1 for i in range(len(tiles)) for j in range(i+1,len(tiles)) if tiles[i]>tiles[j])
    return inv%2==0

def build_puzzle_path(parent,state):
    states=[]
    moves=[]
    while parent[state] is not None:
        prev,move=parent[state]
        states.append(state)
        moves.append(move)
        state=prev
    states.append(state)
    states.reverse()
    moves.reverse()
    return states,moves

def puzzle_bfs(start,goal=GOAL):
    t0=time.perf_counter()
    parent={start:None}
    queue=deque([start])
    explored=0
    while queue:
        cur=queue.popleft()
        explored+=1
        if cur==goal:
            states,moves=build_puzzle_path(parent,cur)
            return {"states":states,"moves":moves,"explored":explored,"time":time.perf_counter()-t0}
        for nxt,mv in puzzle_neighbors(cur):
            if nxt not in parent:
                parent[nxt]=(cur,mv)
                queue.append(nxt)
    return None

def puzzle_astar(start,goal=GOAL):
    t0=time.perf_counter()
    parent={start:None}
    g_cost={start:0}
    counter=0
    heap=[(manhattan(start,goal),0,counter,start)]
    closed=set()
    explored=0
    while heap:
        f,g,_,cur=heapq.heappop(heap)
        if cur in closed:
            continue
        closed.add(cur)
        explored+=1
        if cur==goal:
            states,moves=build_puzzle_path(parent,cur)
            return {"states":states,"moves":moves,"explored":explored,"time":time.perf_counter()-t0}
        for nxt,mv in puzzle_neighbors(cur):
            ng=g+1
            if nxt not in g_cost or ng<g_cost[nxt]:
                g_cost[nxt]=ng
                parent[nxt]=(cur,mv)
                counter+=1
                heapq.heappush(heap,(ng+manhattan(nxt,goal),ng,counter,nxt))
    return None

def random_puzzle(steps=40):
    s=GOAL
    prev=None
    for _ in range(steps):
        options=[n for n,_ in puzzle_neighbors(s) if n!=prev]
        prev=s
        s=random.choice(options)
    return s

def q2():
    root=tk.Tk()
    root.title("8-Puzzle Solver - BFS vs A*")
    current={"state":random_puzzle(),"job":None}
    board_frame=tk.Frame(root)
    board_frame.grid(row=0,column=0,padx=12,pady=12)
    tiles=[]
    for i in range(9):
        lb=tk.Label(board_frame,text="",font=("Arial",28,"bold"),width=3,height=1,relief="raised",bd=3)
        lb.grid(row=i//3,column=i%3,padx=2,pady=2)
        tiles.append(lb)

    def draw(s):
        for i,v in enumerate(s):
            tiles[i].config(text=str(v) if v else "",bg="lightblue" if v else "white")

    def log(msg):
        out.config(state="normal")
        out.insert("end",msg+"\n")
        out.see("end")
        out.config(state="disabled")

    def cancel_animation():
        if current["job"]:
            root.after_cancel(current["job"])
            current["job"]=None

    def set_state(s):
        cancel_animation()
        current["state"]=s
        draw(s)
        entry_var.set(" ".join(str(x) for x in s))

    def on_set():
        digits=entry_var.get().replace(","," ").split()
        if len(digits)==1 and len(digits[0])==9:
            digits=list(digits[0])
        try:
            s=tuple(int(d) for d in digits)
        except ValueError:
            log("Invalid input: use digits 0-8 (0 = blank)")
            return
        if sorted(s)!=list(range(9)):
            log("Invalid input: enter each digit 0-8 exactly once")
            return
        if not is_solvable(s):
            log("This configuration is not solvable")
            return
        set_state(s)
        log("Initial state set")

    def on_random():
        set_state(random_puzzle())
        log("Random solvable puzzle generated")

    def animate(states,i=0):
        draw(states[i])
        if i<len(states)-1:
            current["job"]=root.after(500,lambda:animate(states,i+1))
        else:
            current["job"]=None

    def solve(method):
        cancel_animation()
        start=current["state"]
        draw(start)
        res=puzzle_bfs(start) if method=="BFS" else puzzle_astar(start)
        if res is None:
            log(f"{method}: no solution found")
            return
        log(f"--- {method} ---")
        log(f"Moves required: {len(res['moves'])}")
        log(f"States explored: {res['explored']}")
        log(f"Time: {res['time']*1000:.2f} ms")
        for n,m in enumerate(res["moves"],1):
            log(f"  {n}. {m}")
        animate(res["states"])

    def compare():
        start=current["state"]
        b=puzzle_bfs(start)
        a=puzzle_astar(start)
        log("--- Comparison ---")
        log(f"{'Method':<8}{'Moves':>7}{'Explored':>10}{'Time(ms)':>10}")
        log(f"{'BFS':<8}{len(b['moves']):>7}{b['explored']:>10}{b['time']*1000:>10.2f}")
        log(f"{'A*':<8}{len(a['moves']):>7}{a['explored']:>10}{a['time']*1000:>10.2f}")
        log("Both give an optimal solution; A* explores fewer states thanks to the Manhattan heuristic.")

    entry_var=tk.StringVar(value=" ".join(str(x) for x in current["state"]))
    ctrl=tk.Frame(root)
    ctrl.grid(row=0,column=1,padx=10,pady=10,sticky="n")
    tk.Label(ctrl,text="Initial state (0 = blank):").pack(anchor="w")
    tk.Entry(ctrl,textvariable=entry_var,width=24).pack(anchor="w",pady=2)
    tk.Button(ctrl,text="Set Puzzle",command=on_set).pack(fill="x",pady=2)
    tk.Button(ctrl,text="Random Puzzle",command=on_random).pack(fill="x",pady=2)
    tk.Button(ctrl,text="Solve with BFS",command=lambda:solve("BFS")).pack(fill="x",pady=2)
    tk.Button(ctrl,text="Solve with A*",command=lambda:solve("A*")).pack(fill="x",pady=2)
    tk.Button(ctrl,text="Compare BFS vs A*",command=compare).pack(fill="x",pady=2)
    out=tk.Text(root,width=52,height=14,state="disabled",font=("Courier",9))
    out.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
    draw(current["state"])
    root.mainloop()


# =====================================================================
# Part B - Blind (Uninformed) Search
# =====================================================================

#Q3 - Breadth-First Search for Route Finding

def bfs_graph(graph,start,goal):
    parent={start:None}
    queue=deque([start])
    explored=0
    while queue:
        node=queue.popleft()
        explored+=1
        if node==goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1],explored
        for nb in graph.get(node,[]):
            if nb not in parent:
                parent[nb]=node
                queue.append(nb)
    return None,explored

def q3():
    print("\nQ3 - BFS for Route Finding")
    print("Enter the graph as edges, one per line, like:  A B   (blank line to finish)")
    print("Press Enter on the first line to use the sample graph.")
    graph={}
    first=input("Edge: ").strip()
    if first=="":
        edges=[("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("E","G"),("F","G"),("D","H")]
        start,goal="A","G"
        print("Sample graph edges:",edges)
    else:
        edges=[tuple(first.split())]
        while True:
            line=input("Edge: ").strip()
            if line=="":
                break
            edges.append(tuple(line.split()))
        start=input("Enter starting node: ").strip()
        goal=input("Enter goal node: ").strip()
    for u,v in edges:
        graph.setdefault(u,[]).append(v)
        graph.setdefault(v,[]).append(u)
    path,explored=bfs_graph(graph,start,goal)
    if path:
        print("Path found:"," -> ".join(path))
        print("Path length (edges):",len(path)-1)
    else:
        print("No path found between",start,"and",goal)
    print("Number of nodes explored:",explored)


#Q4 - Depth-First Search for Maze Solving

def dfs_maze(maze,start,end):
    rows,cols=len(maze),len(maze[0])
    stack=[start]
    parent={start:None}
    while stack:
        r,c=stack.pop()
        if (r,c)==end:
            path=[]
            cur=end
            while cur is not None:
                path.append(cur)
                cur=parent[cur]
            return path[::-1]
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in parent:
                parent[(nr,nc)]=(r,c)
                stack.append((nr,nc))
    return None

def q4():
    print("\nQ4 - DFS for Maze Solving  (0 = open, 1 = wall)")
    maze=[[0,1,0,0,0,0],
          [0,1,0,1,1,0],
          [0,0,0,1,0,0],
          [1,1,0,1,0,1],
          [0,0,0,0,0,0],
          [0,1,1,1,1,0]]
    start=(0,0)
    end=(5,5)
    for row in maze:
        print(" ".join(map(str,row)))
    path=dfs_maze(maze,start,end)
    if path is None:
        print("No path exists from",start,"to",end)
        return
    print("Path from",start,"to",end,":")
    print(" -> ".join(str(p) for p in path))
    print("Number of steps:",len(path)-1)
    print("Maze with path marked (*):")
    for r in range(len(maze)):
        print(" ".join("*" if (r,c) in path else str(maze[r][c]) for c in range(len(maze[0]))))


# =====================================================================
# Part C - Heuristic Search
# =====================================================================

#Q5 - A* Search for the 8-Puzzle Problem (Manhattan distance)

def print_puzzle(s):
    for r in range(3):
        print(" ".join(str(x) if x else "_" for x in s[r*3:r*3+3]))

def q5():
    print("\nQ5 - A* Search for the 8-Puzzle")
    start=(1,2,3,5,6,0,7,8,4)
    print("Initial state:")
    print_puzzle(start)
    res=puzzle_astar(start)
    if res is None:
        print("No solution")
        return
    for i,(s,m) in enumerate(zip(res["states"][1:],res["moves"]),1):
        print(f"\nStep {i}: {m}")
        print_puzzle(s)
    print("\nFinal state:")
    print_puzzle(res["states"][-1])
    print("Total path cost:",len(res["moves"]))
    print("Number of states explored:",res["explored"])


#Q6 - Greedy Best-First Search for Route Planning

ROADS={
    "Arad":{"Zerind":75,"Sibiu":140,"Timisoara":118},
    "Zerind":{"Arad":75,"Oradea":71},
    "Oradea":{"Zerind":71,"Sibiu":151},
    "Timisoara":{"Arad":118,"Lugoj":111},
    "Lugoj":{"Timisoara":111,"Mehadia":70},
    "Mehadia":{"Lugoj":70,"Drobeta":75},
    "Drobeta":{"Mehadia":75,"Craiova":120},
    "Craiova":{"Drobeta":120,"Rimnicu Vilcea":146,"Pitesti":138},
    "Sibiu":{"Arad":140,"Oradea":151,"Fagaras":99,"Rimnicu Vilcea":80},
    "Rimnicu Vilcea":{"Sibiu":80,"Craiova":146,"Pitesti":97},
    "Fagaras":{"Sibiu":99,"Bucharest":211},
    "Pitesti":{"Rimnicu Vilcea":97,"Craiova":138,"Bucharest":101},
    "Bucharest":{"Fagaras":211,"Pitesti":101,"Giurgiu":90,"Urziceni":85},
    "Giurgiu":{"Bucharest":90},
    "Urziceni":{"Bucharest":85,"Hirsova":98,"Vaslui":142},
    "Hirsova":{"Urziceni":98,"Eforie":86},
    "Eforie":{"Hirsova":86},
    "Vaslui":{"Urziceni":142,"Iasi":92},
    "Iasi":{"Vaslui":92,"Neamt":87},
    "Neamt":{"Iasi":87}}

# estimated straight-line distance to Bucharest (heuristic values)
H_BUCHAREST={"Arad":366,"Bucharest":0,"Craiova":160,"Drobeta":242,"Eforie":161,"Fagaras":176,
             "Giurgiu":77,"Hirsova":151,"Iasi":226,"Lugoj":244,"Mehadia":241,"Neamt":234,
             "Oradea":380,"Pitesti":100,"Rimnicu Vilcea":193,"Sibiu":253,"Timisoara":329,
             "Urziceni":80,"Vaslui":199,"Zerind":374}

def greedy_search(graph,h,start,goal):
    parent={start:None}
    visited=set()
    heap=[(h[start],0,start)]
    counter=0
    explored=0
    while heap:
        _,_,node=heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        explored+=1
        if node==goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1],explored
        for nb in graph[node]:
            if nb not in visited and nb not in parent:
                parent[nb]=node
                counter+=1
                heapq.heappush(heap,(h[nb],counter,nb))
    return None,explored

def path_distance(graph,path):
    return sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))

def q6():
    print("\nQ6 - Greedy Best-First Search vs BFS (goal: Bucharest)")
    goal="Bucharest"
    for start in ["Arad","Timisoara"]:
        gp,gn=greedy_search(ROADS,H_BUCHAREST,start,goal)
        bp,bn=bfs_graph({k:list(v) for k,v in ROADS.items()},start,goal)
        print(f"\nStart: {start}")
        print("Greedy path:"," -> ".join(gp))
        print(f"  cities on path: {len(gp)}, distance: {path_distance(ROADS,gp)} km, nodes explored: {gn}")
        print("BFS path:   "," -> ".join(bp))
        print(f"  cities on path: {len(bp)}, distance: {path_distance(ROADS,bp)} km, nodes explored: {bn}")
    print("\nDiscussion:")
    print("- BFS ignores distances and finds the path with the fewest cities (hops), exploring level by level, so it explores many nodes.")
    print("- Greedy uses only the heuristic (estimated distance to the goal), so it usually explores fewer nodes and is fast.")
    print("- Greedy is neither optimal nor guaranteed to give the shortest path: it can follow a promising-looking route that turns out longer (see Timisoara).")


# =====================================================================
# Part D - Knowledge Representation
# =====================================================================

#Q7 - Knowledge Representation using Propositional Logic (classroom domain)

facts={"teacher_present","students_present","projector_on"}
rules=[({"teacher_present","students_present"},"class_started"),
       ({"class_started"},"attendance_taken"),
       ({"class_started","projector_on"},"presentation_running"),
       ({"presentation_running","students_attentive"},"students_learning"),
       ({"class_started","doubts_raised"},"discussion_held")]

def infer(query,facts,rules):
    known=set(facts)
    steps=[]
    changed=True
    while changed:
        changed=False
        for premises,conclusion in rules:
            if premises<=known and conclusion not in known:
                known.add(conclusion)
                steps.append(f"{' AND '.join(sorted(premises))}  =>  {conclusion}")
                changed=True
    return query in known,steps,known

def q7():
    print("\nQ7 - Propositional Logic Knowledge Base (Classroom Activities)")
    print("Facts:",sorted(facts))
    print("Rules:")
    for p,c in rules:
        print("  ",' AND '.join(sorted(p)),"=>",c)
    while True:
        q=input("\nEnter a proposition to check (or 'exit'): ").strip()
        if q.lower()=="exit" or q=="":
            break
        result,steps,known=infer(q,facts,rules)
        print("Inference steps:")
        for s in steps:
            print("  ",s)
        print(f"'{q}' CAN be inferred from the knowledge base." if result else f"'{q}' can NOT be inferred from the knowledge base.")
        print("Try e.g. attendance_taken, presentation_running, students_learning")


#Q8 - Knowledge Representation using a Semantic Network (vehicles)

network={
    "Vehicle":{"IS-A":[],"HAS-A":["wheels","engine"],"CAN":["move","carry load"]},
    "Car":{"IS-A":["Vehicle"],"HAS-A":["4 wheels","steering wheel"],"CAN":["carry passengers"]},
    "ElectricCar":{"IS-A":["Car"],"HAS-A":["battery","electric motor"],"CAN":["be charged"]},
    "Bike":{"IS-A":["Vehicle"],"HAS-A":["2 wheels","handlebar"],"CAN":["be pedalled"]},
    "Truck":{"IS-A":["Vehicle"],"HAS-A":["cargo bed"],"CAN":["carry heavy goods"]}}

def get_relation(entity,rel):
    # collects relation values along the IS-A chain (inheritance)
    result=[]
    node=entity
    seen=set()
    while node in network and node not in seen:
        seen.add(node)
        for v in network[node][rel]:
            result.append((v,node))
        parents=network[node]["IS-A"]
        node=parents[0] if parents else None
    return result

def q8():
    print("\nQ8 - Semantic Network (Vehicles)")
    print("Entities:",list(network.keys()))
    print("Query formats:  'Car'  (everything about Car)   or   'Car CAN' / 'Car HAS-A' / 'Car IS-A'")
    while True:
        q=input("\nEnter query (or 'exit'): ").split()
        if not q or q[0].lower()=="exit":
            break
        entity={k.lower():k for k in network}.get(q[0].lower())
        if entity is None:
            print("Unknown entity")
            continue
        rels=["IS-A","HAS-A","CAN"] if len(q)==1 else [q[1].upper()]
        for rel in rels:
            if rel not in ("IS-A","HAS-A","CAN"):
                print("Unknown relation:",rel)
                continue
            if rel=="IS-A":
                chain=[]
                node=entity
                while network[node]["IS-A"]:
                    node=network[node]["IS-A"][0]
                    chain.append(node)
                print(f"{entity} IS-A {' -> '.join(chain) if chain else '(nothing)'}")
            else:
                for value,source in get_relation(entity,rel):
                    note="" if source==entity else f"   (inherited from {source})"
                    print(f"{entity} {rel} {value}{note}")


# =====================================================================
# Part E - PEAS and Intelligent Agents
# =====================================================================

#Q9 - Python Program to Generate PEAS Description

PEAS={
    "vacuum-cleaner agent":{"Performance Measure":["Cleanliness of floor","Time taken","Electricity used","Noise produced"],
        "Environment":["Rooms","Floor (carpet/tiles)","Dirt","Furniture"],
        "Actuators":["Wheels","Brushes","Vacuum suction motor"],
        "Sensors":["Dirt sensor","Bump/obstacle sensor","Cliff sensor","Position sensor"]},
    "self-driving car":{"Performance Measure":["Safety","Reaching destination","Travel time","Passenger comfort","Obeying traffic rules"],
        "Environment":["Roads","Traffic","Pedestrians","Weather"],
        "Actuators":["Steering","Accelerator","Brakes","Indicators","Horn"],
        "Sensors":["Cameras","Radar/LiDAR","GPS","Speedometer"]},
    "medical diagnosis system":{"Performance Measure":["Accuracy of diagnosis","Patient recovery","Cost of tests"],
        "Environment":["Patient","Hospital","Doctors/staff"],
        "Actuators":["Display of diagnosis","Test recommendations","Treatment suggestions"],
        "Sensors":["Patient symptoms input","Lab reports","Medical history"]},
    "chess player":{"Performance Measure":["Win/loss/draw","Number of moves","Time used"],
        "Environment":["Chess board","Opponent","Clock"],
        "Actuators":["Piece movement (move output)"],
        "Sensors":["Board state","Opponent's moves","Clock"]}}

def show_peas(name,peas):
    print(f"\nPEAS description for: {name}")
    print("="*50)
    for key in ["Performance Measure","Environment","Actuators","Sensors"]:
        print(f"{key}:")
        for item in peas[key]:
            print(f"   - {item}")

def q9():
    print("\nQ9 - PEAS Description Generator")
    print("Known applications:",", ".join(PEAS))
    name=input("Enter AI application (e.g. vacuum-cleaner agent): ").strip()
    key=name.lower()
    match=None
    for k in PEAS:
        if key==k or key in k or k in key:
            match=k
            break
    if match:
        show_peas(match,PEAS[match])
    else:
        print("Application not in database - enter its PEAS components (comma separated).")
        peas={}
        for part in ["Performance Measure","Environment","Actuators","Sensors"]:
            peas[part]=[x.strip() for x in input(f"{part}: ").split(",") if x.strip()]
        show_peas(name,peas)


# =====================================================================
# Part F - Integrated AI Problem
# =====================================================================

#Q10 - Intelligent Navigation Agent using Search and Heuristics

def h_grid(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def grid_neighbors(grid,cell):
    r,c=cell
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0:
            yield (nr,nc)

def grid_path(parent,goal):
    path=[]
    cur=goal
    while cur is not None:
        path.append(cur)
        cur=parent[cur]
    return path[::-1]

def grid_bfs(grid,start,goal):
    t0=time.perf_counter()
    parent={start:None}
    queue=deque([start])
    order=[]
    while queue:
        cur=queue.popleft()
        order.append(cur)
        if cur==goal:
            return {"path":grid_path(parent,cur),"order":order,"time":time.perf_counter()-t0}
        for nb in grid_neighbors(grid,cur):
            if nb not in parent:
                parent[nb]=cur
                queue.append(nb)
    return {"path":None,"order":order,"time":time.perf_counter()-t0}

def grid_dfs(grid,start,goal):
    t0=time.perf_counter()
    parent={start:None}
    stack=[start]
    visited=set()
    order=[]
    while stack:
        cur=stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        order.append(cur)
        if cur==goal:
            return {"path":grid_path(parent,cur),"order":order,"time":time.perf_counter()-t0}
        for nb in grid_neighbors(grid,cur):
            if nb not in visited:
                parent[nb]=cur
                stack.append(nb)
    return {"path":None,"order":order,"time":time.perf_counter()-t0}

def grid_greedy(grid,start,goal):
    t0=time.perf_counter()
    parent={start:None}
    heap=[(h_grid(start,goal),0,start)]
    visited=set()
    order=[]
    counter=0
    while heap:
        _,_,cur=heapq.heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        order.append(cur)
        if cur==goal:
            return {"path":grid_path(parent,cur),"order":order,"time":time.perf_counter()-t0}
        for nb in grid_neighbors(grid,cur):
            if nb not in visited and nb not in parent:
                parent[nb]=cur
                counter+=1
                heapq.heappush(heap,(h_grid(nb,goal),counter,nb))
    return {"path":None,"order":order,"time":time.perf_counter()-t0}

def grid_astar(grid,start,goal):
    t0=time.perf_counter()
    parent={start:None}
    g={start:0}
    heap=[(h_grid(start,goal),0,0,start)]
    closed=set()
    order=[]
    counter=0
    while heap:
        _,gc,_,cur=heapq.heappop(heap)
        if cur in closed:
            continue
        closed.add(cur)
        order.append(cur)
        if cur==goal:
            return {"path":grid_path(parent,cur),"order":order,"time":time.perf_counter()-t0}
        for nb in grid_neighbors(grid,cur):
            ng=gc+1
            if nb not in g or ng<g[nb]:
                g[nb]=ng
                parent[nb]=cur
                counter+=1
                heapq.heappush(heap,(ng+h_grid(nb,goal),ng,counter,nb))
    return {"path":None,"order":order,"time":time.perf_counter()-t0}

ALGORITHMS={"BFS":grid_bfs,"DFS":grid_dfs,"Greedy":grid_greedy,"A*":grid_astar}

def make_grid(rows,cols,density=0.27):
    start=(0,0)
    goal=(rows-1,cols-1)
    while True:
        grid=[[1 if random.random()<density else 0 for _ in range(cols)] for _ in range(rows)]
        grid[start[0]][start[1]]=0
        grid[goal[0]][goal[1]]=0
        if grid_bfs(grid,start,goal)["path"]:
            return grid,start,goal

PEAS_NAV="""PEAS description of the navigation agent
Performance : shortest path cost, fewest nodes explored, low execution time
Environment : 2-D grid with free cells and obstacles, start and goal cells
Actuators   : move Up / Down / Left / Right
Sensors     : current position, goal position, obstacle detection in neighbouring cells"""

def q10():
    ROWS,COLS,CELL=20,20,26
    root=tk.Tk()
    root.title("Intelligent Navigation Agent - BFS, DFS, Greedy, A*")
    st={"grid":None,"start":None,"goal":None,"job":None}
    canvas=tk.Canvas(root,width=COLS*CELL,height=ROWS*CELL,bg="white")
    canvas.grid(row=0,column=0,padx=8,pady=8,rowspan=2)
    panel=tk.Frame(root)
    panel.grid(row=0,column=1,sticky="n",padx=6,pady=8)
    out=tk.Text(root,width=58,height=20,font=("Courier",9),state="disabled")
    out.grid(row=1,column=1,padx=6,pady=4,sticky="n")
    speed=tk.Scale(panel,from_=1,to=60,orient="horizontal",label="Delay (ms per step)")
    speed.set(10)

    def log(msg,clear=False):
        out.config(state="normal")
        if clear:
            out.delete("1.0","end")
        out.insert("end",msg+"\n")
        out.config(state="disabled")

    def cell_color(r,c):
        if (r,c)==st["start"]:
            return "green"
        if (r,c)==st["goal"]:
            return "red"
        return "#333333" if st["grid"][r][c]==1 else "white"

    def draw_cell(r,c,color=None):
        canvas.create_rectangle(c*CELL,r*CELL,(c+1)*CELL,(r+1)*CELL,fill=color or cell_color(r,c),outline="#cccccc")

    def draw_grid():
        canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                draw_cell(r,c)

    def new_grid():
        stop_animation()
        st["grid"],st["start"],st["goal"]=make_grid(ROWS,COLS)
        draw_grid()
        log("New grid generated (green = start, red = goal).",clear=True)

    def stop_animation():
        if st["job"]:
            root.after_cancel(st["job"])
            st["job"]=None

    def animate(name,res,i=0):
        order=res["order"]
        step=3
        if i<len(order):
            for cell in order[i:i+step]:
                if cell not in (st["start"],st["goal"]):
                    draw_cell(cell[0],cell[1],"#9ecae1")
            st["job"]=root.after(speed.get(),lambda:animate(name,res,i+step))
        else:
            st["job"]=None
            if res["path"]:
                for cell in res["path"]:
                    if cell not in (st["start"],st["goal"]):
                        draw_cell(cell[0],cell[1],"gold")
                log(f"{name}: path cost {len(res['path'])-1}, nodes explored {len(order)}, time {res['time']*1000:.3f} ms")
            else:
                log(f"{name}: no path found")

    def run(name):
        stop_animation()
        draw_grid()
        res=ALGORITHMS[name](st["grid"],st["start"],st["goal"])
        animate(name,res)

    def compare():
        stop_animation()
        draw_grid()
        results={}
        for name,fn in ALGORITHMS.items():
            results[name]=fn(st["grid"],st["start"],st["goal"])
        log("Comparison of algorithms",clear=True)
        log(f"{'Algorithm':<10}{'Path cost':>10}{'Nodes explored':>16}{'Time (ms)':>11}")
        best=None
        for name,r in results.items():
            cost=len(r["path"])-1 if r["path"] else None
            log(f"{name:<10}{str(cost):>10}{len(r['order']):>16}{r['time']*1000:>11.3f}")
            if r["path"]:
                key=(cost,len(r["order"]),r["time"])
                if best is None or key<best[0]:
                    best=(key,name)
        if best:
            log(f"\nBest algorithm for this grid: {best[1]}")
            log("(lowest path cost, then fewest nodes explored)")
            for cell in results[best[1]]["path"]:
                if cell not in (st["start"],st["goal"]):
                    draw_cell(cell[0],cell[1],"gold")
        log("\n"+PEAS_NAV)

    tk.Label(panel,text="Choose an algorithm:",font=("Arial",10,"bold")).pack(anchor="w")
    for name in ALGORITHMS:
        tk.Button(panel,text=f"Run {name}",width=22,command=lambda n=name:run(n)).pack(pady=1)
    tk.Button(panel,text="Compare All",width=22,command=compare).pack(pady=3)
    tk.Button(panel,text="New Random Grid",width=22,command=new_grid).pack(pady=1)
    speed.pack(fill="x",pady=4)
    new_grid()
    print("\n"+PEAS_NAV)
    root.mainloop()


# =====================================================================
# Menu
# =====================================================================

def main():
    questions={1:("AI-Based Tic-Tac-Toe using GUI (Minimax)",q1),
               2:("GUI-Based 8-Puzzle Solver (BFS & A*)",q2),
               3:("BFS for Route Finding",q3),
               4:("DFS for Maze Solving",q4),
               5:("A* Search for the 8-Puzzle",q5),
               6:("Greedy Best-First Search for Route Planning",q6),
               7:("Knowledge Representation - Propositional Logic",q7),
               8:("Knowledge Representation - Semantic Network",q8),
               9:("PEAS Description Generator",q9),
               10:("Intelligent Navigation Agent",q10)}
    while True:
        print("\n========== Lab 10 - AI Based Lab Assignment ==========")
        for k,(title,_) in questions.items():
            print(f"Q{k}. {title}")
        choice=input("Enter question number (1-10), or 0 to exit: ").strip()
        if choice=="0":
            break
        if choice.isdigit() and int(choice) in questions:
            questions[int(choice)][1]()
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
