from game.room import Room
from game.player import Player
from game import constants

class GameLogic:
    '''
    Handles all logic related to user choice in game.

    Sterotype: service provider

    attributes:
    none 
    '''
    def __init__(self):
        """The class constructor.
        
        Args:
            self (GameLogic): an instance of GameLogic.
            """
        pass
        

    def handle_logic(self, rooms, player, user_input):
        '''
        The first layer of logic in the game, depending on current location, the respective secondary function is called.

        Args:
            rooms
            player
            user_input
        '''
        self._rooms = rooms
        self._player = player
        self._user_input = user_input

        if self._player.get_current_location() == 0:
            self.handle_cellar()
            return False
        elif self._player.get_current_location() == 1:
            self.handle_den()
        elif self._player.get_current_location() == 2:
            self.handle_dining_room()
        elif self._player.get_current_location() == 3:
            self.handle_foyer_closet()
        elif self._player.get_current_location() == 4:
            self.handle_foyer()
        elif self._player.get_current_location() == 5:
            self.handle_kitchen()
        elif self._player.get_current_location() == 6:
            self.handle_pantry()
        elif self._player.get_current_location() == 7:
            self.handle_staircase()
        elif self._player.get_current_location() == 8:
            self.handle_bathroom()
        elif self._player.get_current_location() == 9:
            self.handle_bedroom_1()
        elif self._player.get_current_location() == 10:
            self.handle_bedroom_2()
        elif self._player.get_current_location() == 11:
            self.handle_hall_1()
        elif self._player.get_current_location() == 12:
            self.handle_hall_2()
        elif self._player.get_current_location() == 13:
            self.handle_landing()
        elif self._player.get_current_location() == 14:
            self.handle_master_bath()
        elif self._player.get_current_location() == 15:
            self.handle_master_bed()
        elif self._player.get_current_location() == 16:
            self.handle_music_room()
        elif self._player.get_current_location() == 17:
            self.handle_study()


    def handle_cellar(self):
        '''
        handles all logic related to the cellar
        '''
        if self._user_input.upper() == "FORGIVE":
            print(f"\n{self._rooms[self._player.get_current_location()].get_ending_1()}")
        elif self._user_input.upper() == "STRANGE DOOR":
            
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        else:
            print(f"\n{self._rooms[self._player.get_current_location()].get_ending_2()}")
    
    def handle_den(self):
        '''
        handles all logic related to the den
        '''
        if self._user_input.upper() == "EXIT":
            
            self._player.return_previous_room()
        elif self._user_input.upper() == "BOOK":
            if self._player.get_item_value("magnifying glass"):
                print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
            else:
                print(f"\nYou can't seem to make out the text, its too small! ")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_dining_room(self):
        '''
        handles dining room logic
        '''
        if self._user_input.upper() == "FOYER":
            
            self._player.set_current_room(4)
        elif self._user_input.upper() == "KITCHEN":
            
            self._player.set_current_room(5)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_foyer_closet(self):
        '''
        foyer closet logic
        '''
        if self._user_input.upper() == "EXIT":
            
            self._player.return_previous_room()
        elif self._user_input.upper() == "UMBRELLA":
            self._player.add_item_inventory("umbrella", True)
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_foyer(self):
        '''
        foyer logic
        '''
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DOOR":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
        elif self._user_input.upper() == "CELLAR":
            if self._player.get_item_value("key_cellar"):
                
                self._player.set_current_room(0)
            else:
                print(f"\nYou lack the required item(s). ")
        elif self._user_input.upper() == "DEN":
            
            self._player.set_current_room(1)
        elif self._user_input.upper() == "DINING ROOM":
            
            self._player.set_current_room(2)
        elif self._user_input.upper() == "CLOSET":
            
            self._player.set_current_room(3)
        elif self._user_input.upper() == "STAIRCASE":
            self._player.set_current_room(7)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_kitchen(self):
        '''
        kitchen logic
        '''
        if self._user_input.upper() == "DINING ROOM":
            self._player.set_current_room(2)
        elif self._user_input.upper() == "PANTRY":
            self._player.set_current_room(6)
        elif self._user_input.upper() == "KNIFE":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
            self._player.add_item_inventory("knife", True)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_pantry(self):
        '''
        pantry logic
        '''
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_staircase(self):
        if self._user_input.upper() == "FOYER":
            self._player.set_current_room(4)
        elif self._user_input.upper() == "LANDING":
            self._player.set_current_room(13)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bathroom(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bedroom_1(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_bedroom_2(self):
        
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "CAGE":
            if self._player.get_item_value("knife"):
                print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
                self._player.add_item_inventory("key_mb", True)
            else:
                print(f"\nYou lack the required item(s). ")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_hall_1(self):
        
        if self._user_input.upper() == "LANDING":
            self._player.set_current_room(13)
        elif self._user_input.upper() == "BATHROOM":
            self._player.set_current_room(8)
        elif self._user_input.upper() == "LEFT BEDROOM":
            self._player.set_current_room(9)
        elif self._user_input.upper() == "RIGHT BEDROOM":
            self._player.set_current_room(10)
        elif self._user_input.upper() == "STUDY":
            self._player.set_current_room(17)
        elif self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(12)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_hall_2(self):
        
        if self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(11)
        elif self._user_input.upper() == "MUSIC ROOM":
            self._player.set_current_room(16)
        elif self._user_input.upper() == "MASTER BEDROOM":
            self._player.set_current_room(15)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_landing(self):
      
        if self._user_input.upper() == "STAIRCASE":
            self._player.set_current_room(7)
        elif self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(11)
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_master_bath(self):
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_master_bed(self):
        
        if self._user_input.upper() == "HALLWAY":
            self._player.set_current_room(12)
        elif self._user_input.upper() == "MASTER BATH":
            self._player.set_current_room(14)
        elif self._user_input.upper() == "KEY":
            if self._player.get_item_value("umbrella"):
                print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
                self._player.add_item_inventory("key_cellar", True)
            else:
                print(f"\nYou lack the required item(s). ")
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_music_room(self):
       
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DESK":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
            
        else:
            print(f"\nI'm sorry I don't understand. ")

    def handle_study(self):
        
        if self._user_input.upper() == "EXIT":
            self._player.return_previous_room()
        elif self._user_input.upper() == "DESK":
            print(f"\n{self._rooms[self._player.get_current_location()].get_unique_text()}")
            self._player.add_item_inventory("magnifying glass", True)
        else:
            print(f"\nI'm sorry I don't understand. ")