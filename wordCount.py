

def wordCount(str):
    count = len(str.split())
    return count

def test_functionWordpass():
    example = 'THIS STRING IS FIVE WORDS'
    expected = 5
    result = wordCount(example)
    assert result == expected

def test_functionWordpass2():
    example = 'This string is 5 words'
    expected = 5
    result = wordCount(example)
    assert result == expected

def test_functionWord():
    example = ''
    expected = 0
    result = wordCount(example)
    assert result == expected


test_functionWordpass()
test_functionWordpass2()
test_functionWord()