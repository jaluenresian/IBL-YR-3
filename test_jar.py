from jar import Jar

def test_init():
    j = Jar(10)
    assert j.capacity == 10
    assert j.size == 0

def test_init_default():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

def test_init_invalid_capacity():
    try:
        j = Jar(-5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when initializing jar with negative capacity"

def test_str():
    j = Jar()
    assert str(j) == ""
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"
    j.withdraw(2)
    assert str(j) == "🍪"

def test_deposit():
    j = Jar()
    j.deposit(3)
    assert j.size == 3
    j.deposit(5)
    assert j.size == 8
    try:
        j.deposit(-2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when depositing negative number of cookies"
    try:
        j.deposit(10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when depositing more cookies than jar's capacity"

def test_withdraw():
    j = Jar()
    j.deposit(5)
    j.withdraw(3)
    assert j.size == 2
    try:
        j.withdraw(-2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when withdrawing negative number of cookies"
    try:
        j.withdraw(4)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when withdrawing more cookies than are in the jar"