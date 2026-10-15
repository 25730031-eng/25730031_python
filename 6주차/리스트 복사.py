temps = [28, 31, 33, 35, 27, 26, 25] 
values = temps #(얕은 복사)


print("temps:", temps)
print("values:", values)
values.append("A")
print("temps:", temps)
print("values:", values)



temps = [28, 31, 33, 35, 27, 26, 25] 
values = list(temps) #(깊은 복사)


print("temps:", temps)
print("values:", values)
values.append("A")
print("temps:", temps)
print("values:", values)
