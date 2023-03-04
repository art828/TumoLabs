import random
import time

when_won = [7, 11]
when_lose = [2, 3, 12]

class DiceGame:
  def start_game(self):
    while True:
      self.dice_1, self.dice_2 = random.randint(1, 6), random.randint(1, 6)
      self.dice_summ = self.dice_1 + self.dice_2
      return f"{self.dice_1} + {self.dice_2} = {self.dice_summ}"

  def game(self):
    if self.dice_summ in when_won:
      time.sleep(1)
      return "You won!"
    elif self.dice_summ in when_lose:
      time.sleep(1)
      return """You lose!
The casino won."""
    else:
      time.sleep(1)
      print(f"Now your goal number is {self.dice_summ}")
      while True:
        dice_1, dice_2 = random.randint(1, 6), random.randint(1, 6)
        goal_number_summ = dice_1 + dice_2
        time.sleep(0.3)
        print(goal_number_summ)
        if goal_number_summ == self.dice_summ:
          time.sleep(0.3)
          return "You won!"
        elif goal_number_summ == 7:
          time.sleep(0.3)
          return """You lose!
The casino won."""

dice_game = DiceGame()
print(dice_game.start_game())
print(dice_game.game())