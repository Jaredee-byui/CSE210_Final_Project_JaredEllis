class Room:
    '''
    Any given location within the game.

    Sterotype: Information Holder

    attributes:
    _room_intro - plays when a player enters the rooms, lists available actions.
    _unique_text - soome rooms will have unique dialogue options, this handles those cases.
    _ending_1 - some rooms will be impacted by player choice, ending_1 handles one outcome.
    _ending_2 - similar to ending_1 handles other outcome. 
    '''
    def __init__(self, intro_1, unique_text, ending_1, ending_2):
        """The class constructor.
        
        Args:
            self (Room): an instance of Room.
            _intro_1 - stores room intro
            _unique_text - stores unique text
            _ending_1 - stores ending_1
            _ending_2 - stores ending_2
            """
        self._room_intro_1 = self.create_scene_string(intro_1)
        self._unique_text = self.create_scene_string(unique_text)
        self._ending_1 = self.create_scene_string(ending_1)
        self._ending_2 = self.create_scene_string(ending_2)

    def get_unique_text(self):
        """
        gets unqiue text
        """
        return self._unique_text
    
    def get_room_intro(self):
        '''
        gets room intro
        '''
        return self._room_intro_1

    def get_ending_1(self):
        '''
        gets ending 1
        '''
        return self._ending_1

    def get_ending_2(self):
        '''
        gets ending 2
        '''
        return self._ending_2

    def create_scene_string(self, file_name):
        '''
        converts a .txt file into a string that can be used by the program. 
        '''
        if file_name == " ":
            pass
        else:
            with open(file_name,"rt") as work_file:
                work_string = work_file.read()
            return work_string
