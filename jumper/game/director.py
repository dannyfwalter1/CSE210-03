from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.word import Word


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper.
        word (Word): The game's word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._word = Word()
        self._terminal_service = TerminalService()

    def start_game():
        None
    
    def _get_input():
        None

    def _do_update():
        None

    def check_game_over(is_playing, jumper, word, guess):
        None
        