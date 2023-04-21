import um


def test_count_no_um():
    assert um.count("hello world") == 0
    assert um.count("um, I think") == 1
    assert um.count("a long text without any ums") == 0


def test_count_one_um():
    assert um.count("um") == 1
    assert um.count("um, um, um") == 3
    assert um.count("Um...") == 1
    assert um.count("Ahem, um, ahem, um...") == 2


def test_count_multiple_ums():
    assert um.count("um um um") == 3
    assert um.count("um and um and um") == 3
    assert um.count("um, yummy, um, yummy, um") == 2
    assert um.count("um, a bit more um, and then some um...") == 3