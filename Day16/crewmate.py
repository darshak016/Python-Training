from player import Player
from amongus import Amongus

class Crewmate(Player):
    def __init__(self,name,color,is_alive):
        super.__init__(name,color,is_alive)
        
    def complete_task(self,obj:Amongus):
        """when crewmate has completed any task this method will be called

        Args:
            obj (Amongus): _description_
        """
        pass        
    
    