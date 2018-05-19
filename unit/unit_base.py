from .unit_type import unit_type as ut
from abc import ABCMeta, abstractmethod, abstractproperty

class UnitBase(metaclass=ABCMeta):
    """
        These class stands for representing
        unit of any type, name and stats
    """
    @abstractproperty
    def __init__(self, name = "Wonderbolt", unit_type = ut.UnitType(), damage = 50,
                attack_speed = 200, health = 100):
        """
            Initializing Unit instance by passing
            name, type object(inflicts unit stats) 
            and stats theself (expressed in numerical)
            values
        """
    
    @abstractproperty    
    def __repr__(self):
        return self.name    

    @abstractproperty  
    def __str__(self):
        """
            Returns a string representation (name 
            and stats)of current Unit instance
        """
    @abstractmethod
    def attack(self, foe, log):
        """
            Gives ability to attack. Accepts and returns 
            "foe" - the instance of enemy unit
        """

    @abstractproperty
    def refresh_stats(self):
        """
            Refreshing attack speed depending on 
            difference between 
        """                                
    @abstractproperty
    def calculate_default_cooldown(self):
        """
            Calculating unit cooldown, depends on
            all stats
        """

    @abstractproperty
    def get_cooldown_default(self):
        """
            Get default cooldown
        """

    @abstractproperty
    def get_cooldown(self):
        """
            Get current cooldown
        """

    @abstractproperty
    def set_cooldown(self):
        """ 
            set cooldown 
        """

    @abstractproperty
    def decrease_cooldown(self):
        """ 
            Decreasing cooldown
        """ 

    def get_type(self):
        """ 
            Returns unit type 
        """

    def set_type(self, unit_type = ut.UnitType()):
        """ 
            Set unit type, by passing Type instance
        """

    def get_name(self):
        """ 
            Returns unit name 
        """        

    def set_name(self, name = "Wonderbolt"):
        """ 
            Set unit name, by passing a string 
        """
        
    def get_damage(self):
        """ 
            Returns unit damage 
        """

    def set_damage(self, damage = 50):
        """ 
            Set damage, by passing numerical value
        """

    def get_attack_speed(self):
        """ 
            Get unit attack speed 
        """

    def get_attack_speed_default(self):
        """ 
            Get unit defult attack speed 
        """

    def set_attack_speed(self, attack_speed = 200):
        """ 
            Set attack speed, by passing numerical value
        """

    def get_health(self):
        """ 
            Returns unit health     
        """

    def get_health_default(self):
        """ 
            Returns default unit health
        """        

    def set_health(self, health):
        """ 
            Set current unit health, by 
            passing numerical value 
        """