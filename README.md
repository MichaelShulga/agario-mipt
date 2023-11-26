# Multiplayer Non-Turn-Based Game

This is an online Agar.io game implemented using pygame and socket modules.

## Functionality:

- Client-server (advanced functionality): Both players connect to a single server, requiring client-server communication and server implementation.

## Files

- `agario.py`: Contains the game logic.
- `client.py`: Manages the client-side interactions and rendering.
- `server.py`: Handles server-side operations and manages game state.

## How to play?
1. Download and install [pygame](https://www.pygame.org/wiki/about) by entering:
    ```bash
    pip install pygame
    ```
2. Start the `server.py` file by entering:
    ```bash
    python server.py --host localhost --port 8080
    ```
3. Add client 1 by running the `client.py` file by entering:
    ```bash
    python client.py --host localhost --port 8080
    ```
4. On another computer, add client 2 by running the `client.py` file by entering:
    ```bash
    python client.py --host localhost --port 8080
    ```
5. Enjoy!
