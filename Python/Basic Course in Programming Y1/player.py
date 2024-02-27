'''
Created on 28.11.2018

@author: mikaeltunturi
'''
class Player:
    
    def __init__(self, new_name):
        self.__name = new_name
        self.__no_of_games = 0
        self.__total = 0
        self.__record = 0

    def get_name(self):
        return self.__name
        
    def get_no_of_games(self):
        return self.__no_of_games
                
    def get_record(self):
        return self.__record

    def add_game(self, points):
        if points >= 0:
            self.__total += points
            self.__no_of_games += 1
            if points > self.__record:
                self.__record = points
        
    def average(self):
        if self.__no_of_games > 0:
            self.__average = self.__total / self.__no_of_games
            return self.__average
        else:
            return 0.0
        
    def is_master(self):
        if self.__record >= 3000 and self.__average >= 2000:
            return True
        else:
            return False
        
    def is_better(self, another_player):
        if self.__record > another_player.__record:
            return True
        elif self.__record == another_player.__record:
            if self.__average > another_player.__average:
                return True
            else:
                return False
        else:
            return False
        
    def __str__(self):
        if self.is_master() == True:
            str1 = "{:s}, number of games {:d}, record {:d} points, MASTER.".format(self.__name, self.__no_of_games, self.__record)
            return str1
        elif self.is_master() == False:
            str1 = "{:s}, number of games {:d}, record {:d} points, has not achieved master title.".format(self.__name, self.__no_of_games, self.__record)
            return str1