marks = [float(input(f"enter marks{i+1}:"))for i in range(5)]
highest_marks = max(marks)
lowest_marks = min(marks)
mean_marks = sum(marks)/len(marks)

print(f"highest mark:{highest_marks}")
print(f"lowest mark:{lowest_marks}")
print(f"mean mark: {mean_marks:.2f}")
