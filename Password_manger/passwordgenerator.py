import random


class Password:
    def __init__(self):
        alphabets = ['a', "A", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        numericals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        symbols = ['!', '@', "#", "$", "%", "&", "*", "(", ")", "_", "-"]

        self.password = ""

        # while( 1 ):

        length = random.randint(8, 13)
        count = 0
        while (1):
            x = random.randint(-1, 1)
            if x == -1:
                self.password = self.password + alphabets[random.randint(0, 26)]
                count += 1
            elif x == 0:
                self.password = self.password + symbols[random.randint(0, 10)]
                count += 1
            else:
                self.password = self.password + numericals[random.randint(0, 9)]
                count += 1
            if count == length:
                break

        return self.password


