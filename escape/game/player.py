class Player:
    '''
    An instance of player.

    Sterotype: Information Holder

    attributes:
    _inventory - the players current inventory, all items in the game are logged there and if found, updated to true.
    _current_room - logs the players current location
    _previous_room - logs the players previous location 
    '''
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
            
            """
        self._inventory = {
            "book_1": False,
            "book_2": False,
            "knife": False,
            "umbrella": False,
            "magnifying glass": False,
            "key_mb": False,
            "key_cellar": False
        }
        self._current_room = None
        self._previous_room = None

    def get_inventory(self):
        '''
        returnst the players current inventory
        '''
        return self._inventory

    def get_current_location(self):
        '''
        gets players current location
        '''
        return self._current_room

    def get_item_value(self, key):
        '''
        returns anything attached to a specified item in dictionary
        '''
        return self._inventory[key]

    def add_item_inventory(self, key, value):
        '''
        adds a new item to inventory
        '''
        self._inventory[key] = value

    def get_previous_location(self):
        '''
        gets previous location
        '''
        return self._previous_room
    
    def set_current_room(self, room):
        '''
        sets current location
        '''
        self._previous_room = self._current_room
        self._current_room = room

    def return_previous_room(self):
        '''
        returns player to previous location in game. 
        '''
        self._current_room, self._previous_room = self._previous_room, self._current_room
        
