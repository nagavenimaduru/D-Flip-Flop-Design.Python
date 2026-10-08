print("===== D Flip-Flop =====")

D = int(input("Enter D (0 or 1): "))

if D == 0:
    Q = 0
elif D == 1:
    Q = 1
else:
    print("Invalid input! Enter 0 or 1.")
    exit()

print("Next State Q =", Q)
