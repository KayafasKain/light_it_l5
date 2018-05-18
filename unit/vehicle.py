from .unit import Unit
from .unit_type import unit_type as ut

class Vehicle(Unit):
    def __init__(self, name = "Fanct vehicle", unit_type = ut.UnitType(), damage = 50,
                attack_speed = 30, health = 100, crew = None):
        super().__init__(name, unit_type, damage, attack_speed, health)
        """
            Initializing Unit instance by passing
            name, type object(inflicts unit stats) 
            and stats theself (expressed in numerical)
            values, crew is list of units

        """ 
        try: 
            if len(crew) >= 0:
                self.crew = crew
        except ValueError(e):
            print(e)
            self.crew = []

    def get_crew(self):
        """ Get vehicle crew """
        return self.crew

    def set_crew(self, crew = None):
        """ 
            Set vehicle crew, by passing
            list of crew 
        """
        try: 
            if len(crew) >= 0:
                self.crew = crew
        except ValueError(e):
            print(e)
            self.crew = []      