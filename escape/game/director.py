from game import constants
from game import room
from game.room import Room
from game import player
from game.game_logic import GameLogic

class Director:
    '''
    Controls the progression of gameplay, handles starting and ending the game.

    Sterotype: controller

    attributes:
    _rooms - a list that contains all the room actors in game.
    _player - the player entity. 
    '''
    def __init__(self, rooms, player):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
            rooms - stores the rooms list to a variable _rooms.
            player - stores the player entity.
            """
        self._rooms = rooms
        self._player = player
        self._keep_playing = True
        self._game_logic = GameLogic()
        

    def start_game(self):
        '''
        Starts the game loop, while true game continues
        '''
        starting_room = 4
        self._player.set_current_room(starting_room)
        self._output_text = self._rooms[self._player.get_current_location()].get_ending_1()

        self._play_room_text()
        self._output_text = self._rooms[self._player.get_current_location()].get_room_intro()

        while self._keep_playing:
            input(f"\nPress enter to continue. ")
            self._play_room_text()
            self._get_input()
            self._update_game()


    def _play_room_text(self):
        '''
        prints the current game dialogue
        '''
        print(f"\n{self._output_text}")
        

    def _get_input(self):
        '''
        gets input from user, parses input, and the returns to start_game
        '''
        invalid_input = True
        while invalid_input:
            self._user_input = input("What would you like to do? ")
            try:
                self._user_input.upper()
                invalid_input = False
            except:
                invalid_input = True
        

    def _update_game(self):
        '''
        updates game, when user input is received its passed to game logic and sent through the
        cases to return output state. 
        '''
        _logic_output = self._game_logic.handle_logic(self._rooms, self._player, self._user_input)
        if _logic_output == False:
            self._keep_playing = False

        else:
            self._keep_playing = True
            self._output_text = self._rooms[self._player.get_current_location()].get_room_intro()
