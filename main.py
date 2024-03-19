import random
import math
import os

class Main():
    def __init__(self):
        self.loose_list = []
        self.win_counter = 0
        self.loss_counter = 0
        self.random_number = None
        self.exponent = 2
        self.power = 10
        self.quiz = None
        self.answer = None
        ...

    def start(self):
        self.set_numbers(self.exponent, "Your exponent` ")
        self.set_numbers(self.power, "Your power` ")
        while (True):
            self.random_number = random.randint(self.exponent, self.power)
            self.quiz = int(math.pow(self.exponent, self.random_number))
            os.system("clear")
            print(self.print_score())
            print()
            print(self.get_prompt())
            self.ask_answer()
            print(self.quiz)
        ...

    def set_numbers(self, target, string):
            while(True):
                try: 
                    match target:
                        case self.exponent:
                            self.exponent = int(input(string + "(default = 2): "))
                        case self.power:
                            self.power = int(input(string +"(default = 10): "))
                    break
                except:
                    return "input number only"

    def ask_answer(self):
        try:
            self.answer = int(input("Your answer: "))
            if self.quiz != self.answer:
                print(f"Your answer is {self.answer}", f"Expect answer is {self.quiz}")
                input()
                self.loose_list.append([{self.answer}, {self.quiz}])
                self.loss_counter += 1
                return self.answer
            self.win_counter += 1
        except:
            print("Enter again int type")
            input()
            self.loss_counter += 1
            return

    def get_prompt(self):
        return f"{self.exponent} to the power of {self.random_number}"
    
    def print_score(self):
        return f"| Correct: {self.win_counter} | Wrong: {self.loss_counter} |"

if __name__ == "__main__":
    game = Main()
    game.start()
