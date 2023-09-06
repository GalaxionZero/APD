def convert_to_grades(N):
    if N >= 90 and N <= 100:
        return "A+"
    elif N >= 80 and N <= 89:
        return "A-"
    elif N >= 75 and N <= 79:
        return "B+"
    elif N >= 70 and N <= 74:
        return "B-"
    elif N >= 65 and N <= 69:
        return "C+"
    elif N >= 60 and N <= 64:
        return "C-"
    elif N >= 50 and N <= 59:
        return "D"
    elif N < 50:
        return "E"
    else:
        return "Invalid input"
    
try:
    n = int(input("Enter an integer value for Nilai: "))
    result = convert_to_grades(n)
    print(f"Nilai {result}")

except ValueError:
    print("Invalid input. Please enter an integer value.")