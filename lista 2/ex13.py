S = float(input())

if S < 300:
    R = S*1.05
elif S >= 300 and S < 500:
    R = S*1.07
else:
    R = S*1.10

print(f"{R:.2f}")                 