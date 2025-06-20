A = float(input())



if A <= 280.00:
    N = A *1.2
    P = 20
    V = A*0.2

else:
    if A > 280.00 and A < 700.00:
        N =A*1.15
        P = 15
        V = A*0.15
    elif A >= 700.00 and A < 1500.00:
          N =A*1.1
          P = 10
          V = A*0.1
    elif A >= 1500.00:
           N =A*1.05
           P = 5
           V = A*0.05

print(f"{A:.2f}\n{P}\n{V:.2f}\n{N:.2f}")           





