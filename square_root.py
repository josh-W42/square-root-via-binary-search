def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int:
        raise ValueError('Input must be of type int, {}, given'.format(type(number)))
    
    if number < 0:
        print("Input must be greater than zero.")
        return None

    return int(binary_search(number))
    


def binary_search(number):
    '''Helper function to find the square root'''
    left = 0
    right = number

    while(left != number):
        mid = (left + right) / 2.0
        
        if int(mid * mid) == number:
            return mid
        elif int(mid * mid) < number:
            left = mid
        else:
            right = mid 

    return left

def test_suite():
    print("Basic Function Tests: ")
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")

    print("Negative Number Test:")
    if sqrt(-1) is None:
        print("Pass")
    else:
        print("Fail")

    import math

    print("Large Input Test:")
    if sqrt(10**10) == math.floor(math.sqrt(10**10)):
        print("Pass")
    else:
        print("Fail")

    print("Null input test:")
    try:
        sqrt(None)
    except ValueError:
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_suite()
