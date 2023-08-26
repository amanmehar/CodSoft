#-----------------------------------------------------FINAL------------------------------------------------------

import random

class Generator:
    def generate(self, size:int) -> str:
        alpha = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '$', '&']
        password = random.sample(alpha, size)
        return password

if __name__ == '__main__':
    size = int(input("Enter the desired password length : "))
    g = Generator()
    p = g.generate(size)
    print(p)
    # print(type(p))