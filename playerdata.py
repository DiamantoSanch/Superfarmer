#Player class
class PlayerData():
    def __init__(self, rabbits:int=0, sheeps:int=0, pigs:int=0, cows:int=0, horses:int=0, dogs:int=0, sheepdogs:int=0, guards:int=0) -> None:
        self.rabbits = rabbits
        self.sheeps = sheeps
        self.pigs = pigs
        self.cows = cows
        self.horses = horses
        self.dogs = dogs
        self.sheepdogs = sheepdogs
        self.guards = guards
        #for hints
        self.anim = [self.rabbits, self.sheeps, self.pigs, self.cows, self.horses, self.dogs, self.sheepdogs, self.guards]
        return
    
    def reset(self, rab:int=0):
        self.anim[0] = rab
        self.anim[1] = 0
        self.anim[2] = 0
        self.anim[3] = 0
        self.anim[4] = 0
        self.anim[5] = 0
        self.anim[6] = 0
        self.anim[7] = 0
        return