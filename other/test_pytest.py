import pytest

class Test_002():
    def add_test(self,x):
        return x + 1

    def test_001(self):
        assert self.add_test(3) == 2

if __name__ == '__main__':
    pytest.main('test_pytest.py')
