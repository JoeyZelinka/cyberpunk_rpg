from stat_roller_decker import decker_stats
class Decker:
    def __init__(self):
        stats = decker_stats()
        self.agility = stats["agility"]
        self.strength = stats["strength"]
        self.logic = stats["logic"]
        self.hacking = stats["hacking"]