import operator

class Formation():
    """
        These class represents formations
        Following ofrmations ar now avaliable:
        "strongest ahead", "fastest ahead",
        "helthiest ahead" 
    """
    def __init__(self, name = "fastest ahead", property_switch=2):
        """
            Taking two arguments: formation name, and 
            id of property which will be used in sort
        """
        self.name = name
        self.property_switch = property_switch

    def apply_formation(self, members):
        """
            Applying formation by sorting 
            passed list of members
        """
        if self.property_switch == 1:
            members = sorted(members, key=lambda x: x.get_damage(), reverse = True)
        elif self.property_switch == 2:
            members = sorted(members, key=lambda x: x.get_attack_speed(), reverse = True)
        elif self.property_switch == 3:
            members = sorted(members, key=lambda x: x.get_health(), reverse = True)

        return members


    def get_name(self):
        """ Returns name """
        return self.name

    def set_name(self, name = "fastest ahead"):
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
