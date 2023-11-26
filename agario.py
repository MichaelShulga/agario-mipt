import itertools
import random


class Player:
    """
    Represents a player in the game.

    Attributes:
        x (int): The x-coordinate of the player's position.
        y (int): The y-coordinate of the player's position.
        r (int): The radius of the player, representing the player's size.
        color (tuple): The color of the player, represented as an RGB tuple.
    """
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Game:
    """
    This class represents a simple game environment.

    Attributes:
        width (int): The width of the game area.
        height (int): The height of the game area.
        food_list (list): A list of food locations in the game.
        player_list (list): A list of players in the game.

    Methods:
        _update_food(): Updates the food list by adding new food points.
        _eat_food(): Handles the process of players eating food.
        _eat_player(): Handles the process of players eating other players.
        new_player(): Creates a new player and adds it to the game.
        update(): Updates the game state, including player and food positions.
    """
    def __init__(self) -> None:
        self.width, self.height = 1000, 1000
        self.food_list = []
        self._update_food()
        self.player_list = []

    def _update_food(self) -> None:
        """Updates the food list by adding new food points until reaching the maximum size."""
        size = 50
        for _ in range(size - len(self.food_list)):
            point = (random.randint(0, self.width), random.randint(0, self.height))
            self.food_list.append(point)

    def _eat_food(self) -> None:
        """Allows players to eat food within their radius, increasing their size accordingly."""
        for p in self.player_list:
            for food in self.food_list.copy():
                if (food[0] - p.x) ** 2 + (food[1] - p.y) ** 2 <= p.r ** 2:
                    self.food_list.remove(food)
                    p.r += 1

    def _eat_player(self) -> None:
        """Enables players to consume other smaller players, growing in size as a result."""
        for p1, p2 in itertools.permutations(self.player_list, 2):
            if (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 <= p2.r ** 2 and p1.r < p2.r:
                p2.r += p1.r
                self.player_list.remove(p1)

    def new_player(self) -> Player:
        """Creates a new player with a random position and initial size, adding it to the game."""
        x, y = random.randint(0, self.width), random.randint(0, self.height)
        r = 20
        player = Player(x, y, r)
        self.player_list.append(player)
        return player

    def update(self) -> None:
        """Updates the game state by processing player and food interactions and refreshing food."""
        self._eat_player()
        self._eat_food()
        self._update_food()
    