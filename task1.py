A = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
B = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
D = ["", "M", "MM", "MMM"]

print("Введите арабское число")
number = int(input())
print(D[number // 1000]+C[number % 1000 // 100]+B[number % 100 // 10]+A[number % 10])