

def max(tableau):
    if len(tableau) == 0:
        return -1
    grand = tableau[0]
    
    for element in tableau:
        if element > grand:
            grand = element
    
    return grand
print(max([1,33,2,1099,32,-12,3.1345678]))

