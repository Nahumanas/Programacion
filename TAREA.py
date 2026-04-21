import re 

hl = open("C:/Users/HP/Desktop/PY/Py4e/Access Dates in the Web/M1/regex_sum_2267904.txt")
total = 0 
for line in hl: 
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if not stuff: continue 
    for num in stuff:
        total+= int(num)
print(f"La suma total es : {total}")
    
    