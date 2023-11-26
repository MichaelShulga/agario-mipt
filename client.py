import argparse
import pickle
import socket
import sys

import pygame


class Client:
    """
    A client for handling socket connections and data transmission.

    Attributes:
        sock (socket.socket): The socket object used for network communication.

    Methods:
        __init__(host, port): Initializes the client's socket and connects to the specified host and port.
        send(data): Sends data to the server and waits for a response.
    """
    def __init__(self, host, port):
        """
        Initialize a new Client instance and establish a socket connection.

        Args:
            host (str): The host name or IP address to connect to.
            port (int): The port number to connect on.
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send(self, data):
        """
        Send data to the server and receive a response.

        Args:
            data: The data to be sent to the server.

        Returns:
            The response received from the server.
        """
        self.sock.send(pickle.dumps(data))
        return pickle.loads(self.sock.recv(2048))


def parse_args():
    parser = argparse.ArgumentParser(description="Code Parser")

    parser.add_argument("--host", required=True, help="Host name or IP address")
    parser.add_argument("--port", required=True, type=int, help="Port number")

    return parser.parse_args()


def main():
    args = parse_args()
    client = Client(args.host, args.port)

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption(("Agar.io"))

    while True:
        key = pygame.key.get_pressed()
        game = client.send(key)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        # draw_food
        for x, y in game.food_list:
            polygons = [
                (x, y),
                (x + 4, y),
                (x + 6, y + 2),
                (x + 6, y + 6),
                (x + 4, y + 8),
                (x, y + 8),
                (x - 2, y + 6),
                (x - 2, y + 2),
                ]
            pygame.draw.polygon(screen, (0, 0, 255), polygons)

        # draw players
        for p in game.player_list:
            pygame.draw.circle(screen, (255, 0, 0), (p.x, p.y), p.r + 2)
            pygame.draw.circle(screen, p.color, (p.x, p.y), p.r)

        pygame.display.flip()


if __name__ == "__main__":
    main()
