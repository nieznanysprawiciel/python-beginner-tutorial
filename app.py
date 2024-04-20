

def add(a, b):
    return a + b


sum = add(3, 1)
print(sum)




def test_add():
    assert add(1, 2) == 3
    assert add(3, 5) == 8
