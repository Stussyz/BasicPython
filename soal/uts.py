N = int(input("Masukkan batas angka (N): ")) 
 
for i in range(1, N + 1): 
    if i % 3 == 0 and i % 5 == 0: 
        print("Python Coding") 
    elif i % 3 == 0: 
        print("Python") 
    elif i % 5 == 0: 
        print("Coding") 
    else: 
        print(i) 