class Amongus:

    def __init__(self,player_count,imposters,crewmates) -> None:
        self.player_count = player_count
        self.imposters = imposters
        self.crewmates = crewmates
        self.tasks = []
        self.crew_list = []
        self.imposter_list = []
        
    def start_game(self):
        """This method will create crewmate and imposters from given player 
        count.
        """
        pass
    
    def assign_task(self,tasks):
        """This method assign task to crewmates and imposters.

        Args:
            tasks (_string_): _description_
        """
        self.tasks = self.tasks.append(tasks) 
    
    def game_over(self):
        """This mathod will check count of crewmates and imposters and based on that it will return.
        if All tasks is done by crewmates and still imposter is alive these function will return "Game Over"
        if no. of crewmates is less then the imposter these function will return "Game Over"
        """
        pass     