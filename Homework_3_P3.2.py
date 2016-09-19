# Generate all (x, y, z) coordinates from three lists
x=[1, 2, -1]
y=[8, 4, 3, 0]
z=[0, -1]

points=[[a,b,c] for a in x for b in y for c in  z]
    
print points

