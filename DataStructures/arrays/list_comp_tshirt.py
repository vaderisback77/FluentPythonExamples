## Using list comprehension to create a cartesian product - Iterable 1 * Iterable 2
from pprint import pprint
from random import choice

tshirt_sizes = ["Small", "Medium", "Large"]
tshirt_colors = ["Red", "Blue", "Green", "Black"]

combinations = [(size, color) for size in tshirt_sizes for color in tshirt_colors]
print(
    f"Total Combinations: {len(combinations)},  T-shirt Combinations: {combinations}, "
)
## just printing a random choice for the t-shirt
print(choice(combinations))
