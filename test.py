import unittest
from unittest.mock import patch
import server

class TestServer(unittest.TestCase):

    @patch('server.socket.socket')
    def test_server_with_fake_address(self, mock_socket):
        # Setting up the mock to simulate a failed connection
        mock_socket.return_value.bind.side_effect = OSError("Failed to bind")

        # Define fake arguments
        fake_args = ['--host', 'fakehost', '--port', '12345']
        with patch('sys.argv', fake_args):
            with self.assertRaises(SystemExit):
                server.main()


if __name__ == '__main__':
    unittest.main()
