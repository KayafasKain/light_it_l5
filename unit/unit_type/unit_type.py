class UnitType:
    """
        These class stands for creating
        flexible unit types, which will
        give special threats to units
    """
    def __init__(self, name="some type", damage_rate=1, attack_speed_rate=1, health_rate=1):
        """ 
            Initiation of type object, by specifying
            stats modifiers, that will be multiplied
            on unit stats. 
        """
        self.name = name
        self.attack_speed_rate = attack_speed_rate
        self.damage_rate = damage_rate
        self.health_rate = health_rate

    def __str__(self):
        """
            Generating string version of current 
            instance
        """
        prop_list = [
                        self.get_damage_rate(), 
                        self.get_attack_speed_rate(), 
                        self.get_health_rate()
                    ]
        string = self.get_name() + " | " + " | ".join(format(x, ".3f") for x in prop_list)
        return string        

    def get_name(self):
        """ Returns the name of type """
        return self.name
    
    def set_name(self, name="some type"):
        """ Set type name, by passing string  """
        self.name = name

    def get_damage_rate(self):
        """ Returns damage modifier """
        return self.damage_rate    

    def set_damage_rate(self, damage_rate=1):
        """ Set damage modifier, by passing numerical """
        self.damage_rate = damage_rate 

    def get_attack_speed_rate(self):
        """ Returns attack speed modifier """
        return self.attack_speed_rate    

    def set_attack_speed_rate(self, attack_speed_rate=1):
        """ Set attack speed modifier, by passing numerical """
        self.attack_speed_rate = attack_speed_rate         

    def get_health_rate(self):
        """ Get health modifier """
        return self.health_rate    

    def set_health_rate(self, health_rate=1):
        """ Set health modifier, by passing numerical """
        self.health_rate = health_rate     