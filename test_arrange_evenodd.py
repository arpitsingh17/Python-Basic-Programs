import arrange_evenodd

def test_arrange_even_odd():
    result = arrange_evenodd.arrange_even_odd([1,3,2,5,4,6,9,0])
    print "result", result
    assert check_array(result) == True

def check_array(arr):

    for i in range(len(arr)):
        if (i+arr[i])%2 != 0:
            return False
    return True

