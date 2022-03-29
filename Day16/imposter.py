from player import Player
from crewmate import Crewmate
from amongus import Amongus

class Imposter(Player):
    def __init__(self,name,color,is_alive):
        super.__init__(name,color,is_alive)
        
    def kill_crewmate(self,crewmate:Crewmate):
        """This method will remove killed crewmate from crew_list and set is_alive to False.

        Args:
            crewmate (Crewmate): _description_
        """
        pass
    
    def sabotage(self,obj:Amongus):
        """This method will obstruct any task given in the task list and during time call for
        emergency meeting will be blocked.

        Args:
            obj (Amongus): _description_
        """
        pass