import math
import os

def clear():
  os.system('clear')

def prompt(_=''):
  return input(f'{_}\n>')
  
# BASIC MATH
def add(*args):
  total = 0
  for i in args:
    total += int(i)
  return total
  
def subtract(*args):
  total = args[0]
  for i in args:
    if i == args[0]:
      pass
    else:  
      total -= int(i)
  return total  
  
def multiply(*args):
  total = 1
  for i in args:
    total *= int(i)
  return total

def divide(*args):
  total = args[0]
  for i in args:
    if i == args[0]:
      pass
    else:
      total /= int(i)
  return total
  
# TRIGONOMETRY
def cosine(num):
  return math.cos(int(num))

def tangent(num):
  return math.tan(int(num))

def sine(num):
  return math.sin(int(num))
  
# ADVANCED MATH
def pow(base, power = 2):
  return int(base) ** int(power)

def sqrt(num):
  return math.sqrt(int(num))

def hyp(leg_a, leg_b):
  return sqrt(add(pow(int(leg_a)), pow(int(leg_b))))

def root(radicand, index):
  return int(radicand) ** (1/int(index))

def permutate(num):
  num = int(num)
  permutated_num = 1
  for i in range(num + 1):
    if i > 0:
      permutated_num *= i
  return permutated_num

def scinot(num):
  '''
  returns scientific notation of **INTEGERS**
  still working on supporting floating numbers
  '''
  num = str(num)    
  if len(num) == 1: 
    return num +  ' ✕ 10^0'
  elif len(num) == 2:
    return f'{num[0]}.{num[1:]} ✕ 10'
  else:
    return f'{num[0]}.{num[1:]} ✕ 10^{len(num) - 1}'

def factorial(num):
  num = int(num)
  total = 1
  for n in range(num + 1):
    if n != 0:
      total *= n
  return total

pi = math.pi

# 2D SHAPES
def sq(len):
  return pow(int(len))

def tri(b, h):
  return int(b)*int(h)*0.5

def quad(b, h):
  return int(b)*int(h)

def rhom(d1, d2, s=0):
  return int(d1)*int(d2)*0.5
  
def trap(b1, b2, h, d1=0,d2=0):
  return multiply(add(int(b1), int(b2)), int(h), 0.5)

def circ(r):
  return multiply(pi, pow(r))

def regpoly(apo, s, ns):
  return multiply(0.5, int(apo), multiply(int(s), int(ns)))
  
# 3D SHAPES
def Cube(side_length, volume = True, SA = False):
  if volume:
    return pow(int(side_length), 3)
  else:
    return multiply(pow(int(side_length)), 6)

def Cylinder(radius, height, volume = True, SA = False):
  RAndPi = multiply(pow(int(radius)), pi)
  if volume == True:
    return multiply(RAndPi, int(height))
  else:
    return add(multiply(RAndPi, 2), multiply(int(radius), pi, 2, int(height)))

def Sphere(radius, volume = True, SA = False):
  if volume:
    return multiply(divide(4, 3), pi, pow(int(radius), 3))
  else:
    return multiply(4, pi, pow(int(radius)))

def Cone(radius, height, slant_height = 0, volume = True, SA = False):
  RAndPi = multiply(pow(int(radius)), pi)
  if volume:
    return multiply(divide(1,3), pi, pow(radius), height)
  else:
    if int(slant_height) == 0:
      slant_height = sqrt(add(pow(int(radius)), pow(int(height))))
    else:
      pass
    return add(multiply(pi, int(radius), slant_height), RAndPi)

def RecBasedPyramid(length, height, width, slant_height1 = 0, slant_height2 = 0, volume = True, SA = False):
  if slant_height1 == 0:
    slant_height1 = sqrt(add(pow(int(height)), divide(pow(int(length)), 4)))
  if slant_height2 == 0:
    slant_height2 = sqrt(add(pow(int(height)), divide(pow(int(width)), 4)))
  if volume:
    return multiply(divide(1, 3), int(length), int(height), int(width))
  else:
    return add(multiply(2, multiply(divide(1, 2), int(length), int(slant_height2))), multiply(2, multiply(divide(1, 2), int(width), int(slant_height1))), multiply(int(length), int(width)))

def SqBasedPyramid(width, height, slant_height, volume = True, SA = False):
  if slant_height == 0:
    slant_height = sqrt(add(pow(int(height)), divide(pow(int(width)), 4)))
    sqslant = pow(int(slant_height))
  if volume:
    return multiply(divide(1, 3), sqslant, int(height))
  else:
    return add(multiply(4, multiply(divide(1, 2), int(width), int(slant_height))), int(sqslant))

# MENUS
def BasicMathMenu():
  print('''[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division''',end='')
  choice2 = prompt()
  if choice2 == '1':
    clear()
    num1 = int(prompt('First Number'))
    num2 = int(prompt('Second Number'))  
    num3 = int(prompt('Third Number'))
    if num3 != 0:
      num4 = int(prompt('Fourth Number'))
      if num4 != 0:
        num5 = int(prompt('Fifth Number'))
        if num5 != 0:
          num6 = int(prompt('Sixth Number'))
          clear()
          print(add(num1, num2, num3, num4, num5, num6))
        else:
          clear()
          print(add(num1, num2, num3, num4, num5))
      else:
        clear()
        print(add(num1, num2, num3, num4))
    else:
      clear()
      print(add(num1, num2, num3))
  elif choice2 == '2':
    clear()
    num1 = int(prompt('First Number'))
    num2 = int(prompt('Second Number'))  
    num3 = int(prompt('Third Number'))
    if num3 != 0:
      num4 = int(prompt('Fourth Number'))
      if num4 != 0:
        num5 = int(prompt('Fifth Number'))
        if num5 != 0:
          num6 = int(prompt('Sixth Number'))
          clear()
          print(subtract(num1, num2, num3, num4, num5, num6))
        else:
          clear()
          print(subtract(num1, num2, num3, num4, num5))
      else:
        clear()
        print(subtract(num1, num2, num3, num4))
    else:
      clear()
      print(subtract(num1, num2, num3))
  elif choice2 == '3':
    clear()
    num1 = int(prompt('First Number'))
    num2 = int(prompt('Second Number'))
    num3 = int(prompt('Third Number'))
    if num3 != 0:
      num4 = int(prompt('Fourth Number'))
      if num4 != 0:
        num5 = int(prompt('Fifth Number'))
        if num5 != 0:
          num6 = int(prompt('Sixth Number'))
          clear()
          print(multiply(num1, num2, num3, num4, num5, num6))
        else:
          clear()
          print(multiply(num1, num2, num3, num4, num5))
      else:
        clear()
        print(multiply(num1, num2, num3, num4))
    else:
      clear()
      print(multiply(num1, num2, num3))
  elif choice2 == '4':
    clear()
    num1 = int(prompt('First Number'))
    num2 = int(prompt('Second Number'))  
    num3 = int(prompt('Third Number'))
    if num3 != 0:
      num4 = int(prompt('Fourth Number'))
      if num4 != 0:
        num5 = int(prompt('Fifth Number'))
        if num5 != 0:
          num6 = int(prompt('Sixth Number'))
          clear()
          print(divide(num1, num2, num3, num4, num5, num6))
        else:
          clear()
          print(divide(num1, num2, num3, num4, num5))
      else:
        clear()
        print(divide(num1, num2, num3, num4))
    else:
      clear()
      print(divide(num1, num2, num3))
  
def Shapes3DMenu():
  print('''[1] Cube
[2] Cylinder
[3] Cone
[4] Pyramids
[5] Sphere''',end='')
  choice3 = prompt()
  if choice3 == '1':
    print('[1] Volume\n[2] Surface Area')
    choice4 = prompt()
    if choice4 == '1':
      print('Side Length:')
      sidelength = prompt()
      print(Cube(sidelength))
    else:
      print('Side Length:')
      side_length = prompt()
      print(Cube(side_length, volume = False))
  elif choice3 == '2':
    print('[1] Volume\n[2] Surface Area')
    choice8 = prompt()
    if choice8 == '1':
      print('Radius:')
      radius_for_cylinder = prompt()
      print('Height:')
      height = prompt()
      print(Cylinder(radius_for_cylinder, height))
    else:
      print('Radius:')
      radius_for_cylinder = prompt()
      print('Height:')
      height = prompt()
      print(Cylinder(radius_for_cylinder, height, volume = False))
  elif choice3 == '3':
    print('[1] Volume\n[2] Surface Area')
    choice9 = prompt()
    if choice9 == '1':
      print('Radius:')
      radius_for_cone = prompt()
      print('Height:')
      height_for_cone = prompt()
      print('Slant Height:')
      slant_height = prompt()
      if slant_height == '' or slant_height == '0':
        print(Cone(radius_for_cone, height_for_cone))
      else:
        print(Cone(radius_for_cone, height_for_cone, slant_height))
    else:
      print('Radius:')
      radius_for_cone = prompt()
      print('Height:')
      height_for_cone = prompt()
      print('Slant Height:')
      slant_height = prompt()
      if slant_height == '' or slant_height == '0':
        print(Cone(radius_for_cone, height_for_cone, volume = False))
      else:
        print(Cone(radius_for_cone, height_for_cone, slant_height, volume = False))
  elif choice3 == '4':
    print('[1] Square Based Pyramid\n[2] Rectangular Based Pyramid')
    choice11 = prompt()
    if choice11 == '1':
      print('[1] Volume\n[2] Surface Area')
      choice20 = prompt()
      if choice20 == '1':
        print('Width:')
        width = prompt()
        print('Height:')
        height_for_pyramid1 = prompt()
        print('Slant_height')
        SH_for_pyramid1 = prompt()
        if SH_for_pyramid1 == '' or SH_for_pyramid1 == '0':
          print(SqBasedPyramid(width, height_for_pyramid1))
        else:
          print(SqBasedPyramid(width, height, slant_height))
      else:
        print('Width:')
        width = prompt()
        print('Slant_height')
        SH_for_pyramid1 = prompt()
        if SH_for_pyramid1 == '' or SH_for_pyramid1 == '0':
          print(SqBasedPyramid(width, SH_for_pyramid1, volume = False))
        else:
          print(SqBasedPyramid(width, SH_for_pyramid1, volume = False))
    else:
      print('[1] Volume\n[2] Surface Area')
      choice20 = prompt()
      if choice20 == '1':
        print('Length:')
        length_for_pyramid2 = prompt()
        print('Height:')
        height_for_pyramid2 = prompt()
        print('Width:')
        width_for_pyramid2 = prompt()
        print(RecBasedPyramid(length_for_pyramid2, height_for_pyramid2, width_for_pyramid2))
      else:
        print('Length:')
        length_for_pyramid2 = prompt()
        print('Height:')
        height_for_pyramid2 = prompt()
        print('Width:')
        width_for_pyramid2 = prompt()
        print(RecBasedPyramid(length_for_pyramid2, height_for_pyramid2, width_for_pyramid2, volume = False))   
  else:
    print('[1] Volume\n[2] Surface Area')
    choice12 = prompt()
    if choice12 == '1':
      print('Radius:')
      radius_for_sphere = prompt()
      print(Sphere(radius_for_sphere))
    else:
      print('Radius:')
      radius_for_sphere = prompt()
      print(Sphere(radius_for_sphere, volume = False))

def AdvancedMathMenu():
  print('''[1] Square Root
[2] Permutation
[3] Exponents
[4] Root
[5] Absolute Value
[6] Scientific Notation (Integers)''',end='')
  c = prompt()
  clear()
  if c == '1':
    Radicand = prompt('Radicand')
    print(sqrt(Radicand))
  elif c == '2':
    n = prompt('Number')
    print(permutate(n))
  elif c == '3':
    base = prompt('Base')
    power = prompt('Power')
    print(pow(base, power))
  elif c == '4':
    Radicand = prompt('Radicand')
    Index = prompt('Index')
    print(root(Radicand, Index))
  elif c == '5':
    num = prompt('Number')
    print(abs(int(num)))
  elif c == '6':
    num = prompt('Number')
    print(scinot(num))

def Shapes2DMenu():
  print('''[1] Triangle
[2] Square
[3] Rectangle
[4] Parallelogram
[5] Rhombus
[6] Trapezoid
[7] Circle
[8] Regular Polygon''',end='')
  c = prompt()
  if c == '1':
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    if pa:
      s = prompt('Side Length')
      print(multiply(3, s))
    else:
      b = prompt('Base')
      h = prompt('Height')
      print(tri(b, h))
  elif c == '2':
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    len = prompt('Side Length')
    if pa:
      print(multiply(4, len))
    else:  
      print(sq(len))
  elif c == '3':
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    l = prompt('Length')
    w = prompt('Width')
    if pa:
      print(multiply(2, add(l, w)))
    else:
      print(quad(l, w))
  elif c == '4':
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    l = prompt('Length')
    if pa:
      d = prompt('Diagonal Hieght')
      print(multiply(2, add(l, d)))
    else:
      print(multiply(2, add(l, w)))
      print(quad(l, h))
  elif c == '5':
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    if pa:
      s = prompt('Side Length')
      return multiply(4, int(s))
    d1 = prompt('Vertical Diagonal')
    d2 = prompt('Horizontal Diagonal')
    print(rhom(d1, d2))
  elif c == '6':
    b1 = prompt('First Base')
    b2 = prompt('Second Base')
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    if pa:
      d1 = prompt('First Slant Height')
      d2 = prompt('Second Slant Height')
      print(trap(b1, b2, 0, d1, d1, pa))
    else:
      h = prompt('Height')
      print(trap(b1, b2, h))
  elif c == '7':
    r = prompt('Radius')
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    if pa:
      print(multiply(pi, 2, r))
    else:
      print(circ(r))
  elif c == '8':
    s = prompt('Side Length')
    nside = prompt('Number of Sides')
    pa = prompt('Perimeter or Area? [p if perimeter, ENTER if area]')
    if not(pa):
      apo = prompt('Apothem')
      print(regpoly(apo, s, nside))
    else:
      print(multiply(s, nside))

def TrigonometryMenu():
  print('''[1] Sine
[2] Cosine
[3] Tangent''', end='')
  c = prompt()
  if c == '1':
    n = prompt('Number')
    print(sine(n))
  elif c == '2':
    n = prompt('Number')
    print(cosine(n))
  elif c == '3':
    n = prompt('Number')
    print(tangent(n))

def Menu():
  print('''[1] Basic Math
[2] Advanced Math
[3] 2D Shapes 
[4] 3D Shapes
[5] Trigonometry''',end='')
  choice1 = prompt()
  clear()
  if choice1 == '1':
    BasicMathMenu()
  elif choice1 == '2':
    AdvancedMathMenu()
  elif choice1 == '3':
    Shapes2DMenu()
  elif choice1 == '4':
    Shapes3DMenu()
  elif choice1 == '5':
    TrigonometryMenu() 

Menu()