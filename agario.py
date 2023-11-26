import itertools
import random


class Player:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Game:
    def __init__(self) -> None:
        self.width, self.height = 1000, 1000
        self.food_list = []
        self._update_food()
        self.player_list = []

    def _update_food(self) -> None:
        size = 50
        for _ in range(size - len(self.food_list)):
            point = (random.randint(0, self.width), random.randint(0, self.height))
            self.food_list.append(point)

    def _eat_food(self) -> None:
        for p in self.player_list:
            for food in self.food_list.copy():
                if (food[0] - p.x) ** 2 + (food[1] - p.y) ** 2 <= p.r ** 2:
                    self.food_list.remove(food)
                    p.r += 1

    def _eat_player(self) -> None:
        for p1, p2 in itertools.permutations(self.player_list, 2):
            if (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 <= p2.r ** 2 and p1.r < p2.r:
                p2.r += p1.r
                self.player_list.remove(p1)

    def new_player(self) -> Player:
        x, y = random.randint(0, self.width), random.randint(0, self.height)
        r = 20
        player = Player(x, y, r)
        self.player_list.append(player)
        return player

    def update(self) -> None:
        self._eat_player()
        self._eat_food()
        self._update_food()
    