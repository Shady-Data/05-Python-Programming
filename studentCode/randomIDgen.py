import random

class RandomID:

    def __init__(self):
        self.__nums = set()
        self.generate_nums()

    def generate_nums(self):
        while len(self.__nums) < 100:
            self.__nums.add(random.randint(10000, 99999))

    def get_id(self):
        return self.__nums.pop(random.randint(0, len(self.__nums) - 1))

