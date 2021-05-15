

def palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def test_functionWordpass():
    example = 'WOW'
    expected = True
    result = palindrome(example)
    assert result == expected

def test_functionWordFail():
    example = 'Not a Palindrome'
    expected = False
    result = palindrome(example)
    assert result == expected
    
def test_functionWordFail2():
    example = ''
    expected = False
    result = palindrome(example)
    assert result == expected
    
test_functionWordpass()
test_functionWordFail()
test_functionWordFail2()

