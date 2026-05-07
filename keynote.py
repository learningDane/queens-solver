import time
from matplotlib import pyplot as plt
from queens_solver import solve_queens, solve_queens_matte
from queens_solver_claude import solve_queens as solve_queens_claude

max_board = 61
X = range(4,max_board,2)
#Y = [0.]*np.floor(((max_board-2)/2))
Y = [0.]*((max_board-2)//2)
for i,x in enumerate(X):
    time_tot = 0
    start_time = time.time()
    solution = solve_queens(x)
    elapsed = time.time() - start_time
    time_tot = time_tot + elapsed
    print(f"Davide {x}x{x}: {time_tot*1000} ms")
    Y[i] = (time_tot)*1000

Y_matte = [0.]*((max_board-2)//2)
for i,x in enumerate(X):
    time_tot = 0
    start_time = time.time()
    solution = solve_queens_matte(x)
    elapsed = time.time() - start_time
    time_tot = time_tot + elapsed
    #Y[i] = round(time_tot/4, 3)
    print(f"Matteo {x}x{x}: {time_tot*1000} ms")
    Y_matte[i] = (time_tot)*1000

Y_claude = [0.]*((max_board-2)//2)
for i,x in enumerate(X):
    time_tot = 0
    start_time = time.time()
    solution = solve_queens_claude(x)
    elapsed = time.time() - start_time
    time_tot = time_tot + elapsed
    #Y[i] = round(time_tot/4, 3)
    print(f"claudeo {x}x{x}: {time_tot*1000} ms")
    Y_claude[i] = (time_tot)*1000

plt.plot(X,Y, label="Davide (L)")
plt.plot(X,Y_matte, label="Matteo (MRV)")
plt.plot(X,Y_claude, label="Claude")
plt.title("Average time of solution found")
plt.xlabel("N")
plt.ylabel("time to complete (ms)")
plt.grid(True, linestyle='--'
, alpha=0.7)
plt.yscale('log')
plt.legend()
plt.show()
