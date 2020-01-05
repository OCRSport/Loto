from pytest import raises
from models.bag import Bag, EmptyBagError


class TestBag:

    def setup(self):
        # 1, 2, 3
        self.bag = Bag(3)

    def test_init(self):
        # 1, 2, 3
        assert len(self.bag) == 3
        assert self.bag._numbers == [1, 2, 3]

    def test_len(self):
        assert len(self.bag) == 3

    def test_get_random_numbers(self):
        # чисел столько сколько нужно
        numbers = self.bag.get_random_numbers(2)
        assert len(numbers) == 2
        # нет лишних чисел
        for item in numbers:
            assert item in self.bag._numbers

    def test_get_next_number(self):
        old_numbers = self.bag._numbers[:]
        number = self.bag.get_next_number()
        assert len(self.bag) == 2
        # действительно должен быть в мешке до этого
        assert number in old_numbers

        self.bag.get_next_number()
        self.bag.get_next_number()

        # В мешке больше нет номеров
        with raises(EmptyBagError):
            self.bag.get_next_number()

