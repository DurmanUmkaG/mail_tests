import pytest


class TestInt:

    def test_sum(self):
        assert 2 + 2 == 4

    def test_negative_sum(self):
        with pytest.raises(TypeError):
            "a" + 2

    @pytest.mark.parametrize(
        "val1, val2, expected",
        [
            pytest.param(2, 3, 6),
            pytest.param(-2, 3, -6),
            pytest.param(-1, -2, 2),
            pytest.param(0, 1, 0)
        ]
    )
    def test_multiplication(self, val1: int, val2: int, expected: int):
        assert val1 * val2 == expected


class TestSet:

    def test_remove(self):
        s = {1, 2, 3}
        s.remove(3)
        assert s == {1, 2}

    def test_remove_non_existent_element(self):
        s = {1, 2, 3}
        with pytest.raises(KeyError):
            s.remove(20)

    @pytest.mark.parametrize("s, val, expected",
                             [
                                 pytest.param({1, 2}, 3, {1, 2, 3}),
                                 pytest.param(set(), 1, {1}),
                                 pytest.param({1, 2}, 2, {1, 2})
                             ]
                             )
    def test_add(self, s: set, val: int, expected: set):
        s.add(val)
        assert s == expected
