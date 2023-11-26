import argparse
import socket
import _thread
import pickle

import pygame

import agario


def parse_args():
    parser = argparse.ArgumentParser(description="Code Parser")

    parser.add_argument("--host", required=True, help="Host name or IP address")
    parser.add_argument("--port", required=True, type=int, help="Port number")

    return parser.parse_args()


def main():
    args = parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((args.host, args.port))
    sock.listen(2)
    print("Waiting for a connection, Server Started")

    pygame.init()

    game = agario.Game()

    def threaded_client(conn, player):
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                if not data:
                    print("Disconnected")
                    break
                else:
                    key = data
                    speed = 5
                    if key[pygame.K_UP]:
                        player.y -= speed
                    if key[pygame.K_DOWN]:
                        player.y += speed
                    if key[pygame.K_LEFT]:
                        player.x -= speed
                    if key[pygame.K_RIGHT]:
                        player.x += speed
                conn.sendall(pickle.dumps(game))
            except:
                break
        game.player_list.remove(player)
        print("Lost connection")
        conn.close()

    def serve_game():
        while True:
            game.update()

    _thread.start_new_thread(serve_game, ())

    while True:
        conn, addr = sock.accept()
        print("Connected to:", addr)
        
        player = game.new_player()
        _thread.start_new_thread(threaded_client, (conn, player))


if __name__ == "__main__":
    main()
