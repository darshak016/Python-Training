from amongus import Amongus
from crewmate import Crewmate

class Player:
    
    def __init__(self,name,color,is_alive):
        self.name = name
        self.color = color
        self.is_alive = is_alive
        
    def call_meeting(self,obj: Amongus) ->str:
        """This method will take list of players from crew_list amd imposter_list and all member will vote 
        any player or skip.
        if any player got more then 50% vote then that player got eliminated.
        Args:
            obj (Amongus): _description_
        """
        pass 
    
    def vote(self,obj:Amongus):
        """From the crew_list and imposter_list all player give vote or skip vote.

        Args:
            obj (Amongus): _description_
        """
        pass
    
    def report_killed_player(self,obj:Crewmate):
        """when crewmate or imposter find a deadbody then this method will be called.

        Args:
            self (_type_): _description_
        """
        pass