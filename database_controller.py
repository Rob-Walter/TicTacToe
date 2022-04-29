import sqlite3
import os
import globals
from unittest import result
from sqlite.init_database import init_command
from board import Board


class DB_Controller:
    
    #2 methoden hinzufügen GetDb für selects und Setdb für insert, update, delete
    #diese methode funkioniert
    def __init__(self):
        self.path = os.path.join(os.path.abspath(os.curdir),"sqlite/datenbank.db")
        self.verbindung = sqlite3.connect(self.path)
        self.zeiger = self.verbindung.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='user_table'"
        result = self.zeiger.execute(sql).fetchone()
        self.verbindung.commit()
        if result == None:
            self.initDatabase()
            #führe init_methode aus
        print("End of init")
        
    def initDatabase(self):
        for command in init_command:
            print(command)
            result = self.zeiger.execute(command)
            self.verbindung.commit()

    #diese methode funkioniert
    def insertnewplayer(self, nickname, password):
        sql = f"INSERT INTO user_table (nickname, password) VALUES ('{nickname}', '{password}')" 
        result = self.zeiger.execute(sql)
        self.verbindung.commit()
        if result.rowcount == 1:
            return True
        else:
            return False
        
        
    #diese methode funkioniert
    def checkifplayerexistinDB(self, nickname, password):
        sql = f"SELECT * FROM user_table WHERE nickname = '{nickname}' AND password = '{password}'"
        if(self.zeiger.execute(sql)):
            id = self.zeiger.fetchone()[0]
            globals.setUser(nickname, id)
            return True
        else:
            return False    

    #diese methode funkioniert
    def setnewgameintogametable(self, user_id, game_id):        
        sql = f"INSERT INTO user_game_table (user_id, game_id, game_status) VALUES ({user_id}, {game_id}, 0)"
        self.zeiger.execute(sql)
        self.verbindung.commit()
        return self.zeiger.lastrowid

    def savefilegame(self,userid, board : Board):
        id = self.setnewgameintogametable(userid,1)
        for columnIndex,column in enumerate(board.get2dArray()):
            for rowIndex, field in enumerate(column):
                if(field.getPawn() != None):
                    team = field.getPawn().getTeam()
                    sql = f"INSERT INTO savefile_table (user_id, game_number, figur_team, figur_row, figur_column) VALUES ({userid}, {id}, '{team}', {rowIndex}, {columnIndex})"
                    self.zeiger.execute(sql)
                    self.verbindung.commit()

    def loadfilegame(self, game_id):
        sql = f"SELECT * FROM savefile_table WHERE game_number = {game_id}"
        self.zeiger.execute(sql)
        inhalt = self.zeiger.fetchall()
        print(inhalt)


    
        
    #def SetGameStatusOnFinished(self, game_number):
        #sql = ""
        #verbindung = sqlite3.connect("F:\Ausbildung Fachinformatiker\Berufsschule\Jahresprojekt\sqlite\database\datenbank.db")
        #zeiger = verbindung.cursor()
                
#controller = DB_Controller()
#controller.loadfilegame(8)
#controller.savegame()
#controller.setnewgameintogametable(1, 1)
#controller.insertnewplayer('test', 'test')
