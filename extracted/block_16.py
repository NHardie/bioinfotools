# Distance
# Input: Two lists of floats of equal length
# Output: Euclidean distance between the two lists, considered as vectors, equal to the length of the lists
# Compute element by element difference, square, sum the squares, take square root
# Raise a Dimensionality exception if two lists are unequal lengths, or both empty
# Return a float

# Example: values = [1, 2, 3, 4, 5]
# Example: list_1 = [float(i) for i in values]
# Example: list_2 = [float(i) for i in values]
# Example: distance(list_1, list_2)

# Define function
def distance(list1, list2):
    
    # Check for length match
    if len(list1) != len(list2):
        raise DimensionalityException("Lists have to be same length")
    
    # Check for empty list
    if len(list1) == 0:
        raise DimensionalityException("Lists cannot be empty")
    
    # Zip two lists together
    zipped = zip(list1, list2)
    
    # Work out difference, absolute value fine, as will be squaring
    # Could write as sqrt(sum((a-b)**2)) but for clarity:
    diff = [a - b for a,b in zipped]
    
    # Square values
    square = [a **2 for a in diff]
    
    # Sum squares
    summed = sum(square)
    
    # Square root using math from standard library
    sqrt = math.sqrt(summed)
    
    # Return sqrt value as a float
    return sqrt
