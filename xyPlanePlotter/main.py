xyPlane = [['10|','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['9 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['8 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['7 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['6 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['5 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['4 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['3 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['2 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['1 |','  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  0',' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']]

def fn():
    x = 1
    y = 1
    coordinates = {}
    #fn defined
    # y = 2x

    for temp_var in range(len(xyPlane) - 1) :
        y = x
        if y in range(0, len(xyPlane) + 1):
            coordinates.update({x:y})
        x += 1

    return coordinates


#substituting coordinates in xyPlane

coordinates = fn()

for x in coordinates:
    xyPlane[ -coordinates.get(x) - 1][x]= '⍟'


#plotting Graph

for row in xyPlane:
    for cell in row:
        print(cell, end= " ")
    print()

