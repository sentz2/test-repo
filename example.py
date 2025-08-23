import random
import matplotlib.pyplot as plt

# Generate 10 random numbers
numbers = [random.randint(1, 100) for _ in range(10)]

# Compute average
average = sum(numbers) / len(numbers)

print("Random numbers:", numbers)
print("Average:", average)

# Plot
plt.plot(numbers, marker="o")
plt.axhline(average, color="red", linestyle="--", label=f"Average = {average:.2f}")
plt.legend()
plt.title("Random Numbers and Their Average")
plt.show()
