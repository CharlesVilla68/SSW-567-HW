import math

def classify_triangle(a, b, c): 
    if a + b <= c or b + c <= a or a + c <= b: 
        return "Not a triangle"
    
    if a == b == c: 
        triType =  "Equilateral"
    elif a == b or b == c or a == c: 
        triType = "Isosceles"
    else: 
        triType = "Scalene"
    
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a **2) or (a ** 2 + c ** 2 == b ** 2): 
        triType += " Right"
    
    return triType

def triangleTesting(): 
    assert classify_triangle(3, 4, 5) == "Scalene Right"
    assert classify_triangle(7, 10, 5) == "Scalene"
    assert classify_triangle(2, 2, 2) == "Equilateral"
    assert classify_triangle(5, 5, 8) == "Isosceles"
    assert classify_triangle(1, 1, 2) == "Not a triangle"

if __name__ == "__main__": 
    triangleTesting()
    print("Tests Passed")