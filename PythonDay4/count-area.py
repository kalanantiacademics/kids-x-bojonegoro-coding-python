print("AREA CALCULATOR")
print("========================")

# Square
print("1. SQUARE")
side = float(input("Masukkan panjang sisi: "))
square_area = side * side
print("Square area =", square_area)

# Triangle
print("2. TRIANGLE")
base = float(input("Masukkan panjang alas: "))
height = float(input("Masukkan tinggi: "))
triangle_area = 0.5 * base * height
print("Triangle area =", triangle_area)

# Rectangle
print("3. RECTANGLE")
length = float(input("Masukkan panjang: "))
width = float(input("Masukkan lebar: "))
rectangle_area = length * width
print("Rectangle area =", rectangle_area)

# Circle
print("4. CIRCLE")
radius = float(input("Masukkan jari-jari: "))
circle_area = 3.14 * radius * radius
print("Circle area =", circle_area)

print("========================")
print("ALL CALCULATIONS COMPLETE")