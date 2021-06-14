from stat_roller_samurai import samurai_stats
class Street_Samurai:
    def __init__(self):
        stats = samurai_stats()
        self.agility = stats["agility"]
        self.strength = stats["strength"]
        self.logic = stats["logic"]
        self.hacking = stats["hacking"]
        

        