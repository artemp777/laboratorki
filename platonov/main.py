def unique_sorted(iterable):
    return sorted(set(iterable))
def test1():
    assert unique_sorted("hello") == ['e', 'h', 'l', 'o']
    print(unique_sorted("hello"))
def test2():
    assert unique_sorted("a1b2c1a3") == ['1', '2', '3', 'a', 'b', 'c']
    print(unique_sorted("a1b2c1a3"))
def test3():
    assert unique_sorted([5, 1, 3, 1, 5]) == [1, 3, 5]
    print(unique_sorted([5, 1, 3, 1, 5]))
def test4():
    assert unique_sorted("") == []
    print(unique_sorted(""))
def test5():
    assert unique_sorted("abc!cba!") == ['!', 'a', 'b', 'c']
    print(unique_sorted("abc!cba!"))
def test6():
    assert unique_sorted((2, 2, 3, 1, 3)) == [1, 2, 3]
    print(unique_sorted((2, 2, 3, 1, 3)))
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()