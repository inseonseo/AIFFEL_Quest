import random

class FunnyDice:

    def __init__(self, num_faces):
        self.num_faces = num_faces
        self.number = 0

    def throw(self):
        self.number = random.randint(1, self.num_faces)

    def get_number(self):
        print("현재 주사위 값은 {} 입니다.".format(self.number))
        pass

def main():
    user_input = input("n면체 주사위를 굴립니다, n을 입력하세요: ")
    try:
        number = int(user_input)
        my_dice = FunnyDice(number)
        my_dice.throw()
        my_dice.get_number()

    except ValueError:
        print("양의 정수를 입력하세요.")


if __name__ == "__main__":
    main()


