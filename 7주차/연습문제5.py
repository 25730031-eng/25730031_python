# f-string
PI = 3.14
r = int(input())
area =r*r*PI

print(f"PI = {PI:2f}")
print(F"Area {r} * {r} * {PI} = {area:.1f}")

#format()
PI = 3.14
r = int(input())
area =r*r*PI

print("PI = {PI:.2f}".format(PI))
print("Area = {} * {} * {} ={:.1f}".format(r, r, PI, area))
