import math

print("Welcome to PyPaint Calc!")
print("Follow the prompts below to begin calculations.")

height = int(input("Please specify wall height: "))
width = int(input("Please specify wall width: "))
paint_coverage = int(input("Please specify number of square meters to cover: "))

def calc_paint_coverage(height, width, paint_coverage):
    total = (height * width) / paint_coverage
    total = math.ceil(total)
    print(f"You will need to purchase {total} cans of paint.")
    
calc_paint_coverage(height=height, width=width, paint_coverage=paint_coverage)