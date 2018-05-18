class Strategy():
    """
        Dedermines possible army strategies
    """
    def __init__(self, name = "weakest first!", property_switch=2):
        """
            Taking two arguments: Strategy name, and 
            id of property which will be used in sort
        """
        self.name = name
        self.property_switch = property_switch

    def apply_strategy(self, members):
        """
            Applying formation by sorting 
            passed list of members
        """
        if self.property_switch == 1:
            members = sorted(members, key=lambda x: x.get_damage(), reverse = True)
        if self.property_switch == 2:
            members = sorted(members, key=lambda x: x.get_damage(), reverse = False)            
        if self.property_switch == 3:
            members = sorted(members, key=lambda x: x.get_attack_speed(), reverse = True)
        if self.property_switch == 4:
            members = sorted(members, key=lambda x: x.get_attack_speed(), reverse = False)  
        if self.property_switch == 5:
            members = sorted(members, key=lambda x: x.get_health(), reverse = False)                      
        if self.property_switch == 6:
            members = sorted(members, key=lambda x: x.get_health(), reverse = False)

        return members


    def get_name(self):
        """ Returns name """
        return self.name

    def set_name(self, name = "slowest first!"):
        """ Set name, by passing name argument """
        self.name = name

    def get_property_switch():
        """ Returns property switch walue """
        return self.property_switch

    def set_property_switch(self, property_switch = 2):
        """ Switch property switch, by passing 
            property_switch argument
        """
        self.property_switch = property_switch
