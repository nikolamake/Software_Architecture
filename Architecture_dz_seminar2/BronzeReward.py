import random
import GameItem


class BronzeReward(GameItem.GameItem):
    def open_item(self):
        random_amount = random.randrange(self.lb, self.rb + 1)
        print(f'получено {random_amount} монет бронзы!!!')