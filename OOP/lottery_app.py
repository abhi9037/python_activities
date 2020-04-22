import random


class LotteryApp():
    def userInput(self):
        user_input = input("Enter 6 digits within 20 separated by comma: ")
        num_list = user_input.split(',')
        input_values = {int(val) for val in num_list}
        return input_values

    def lotteryValue(self):
        value = set()
        while len(value) < 6:
            value.add(random.randint(1,20))
        return value

    def menu(self):
        user_values = self.userInput()
        lottery_values = self.lotteryValue()
        match = user_values.intersection(lottery_values)
        print("Matching numbers are: {}. And winning amount is ${}".format(match,len(match)*100))

obj = LotteryApp()
obj.menu()