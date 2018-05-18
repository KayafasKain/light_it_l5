from combat import formation as fo
from .unit import Unit

class Squad(Unit):
    """
        Squad, inheritant of Unit represents
        list of units, and provides nesessery
        methods 
    """
    def __init__(self, name = "some party", member_list = None, formation = fo.Formation() ):
        """
            Initializing object, by passing
            name, list of memebers and formation
            also, calculating some depended paremeters
        """
        super().__init__(name)
        self.name = name
        self.member_list = member_list
        self.formation = formation
        self.initiative = 0
        self.casulties = 0
        self.refresh_formation()
        self.calculate_initiative()

    def __str__(self):
        """
            Converting class instace to string
        """
        self.calculate_initiative()
        prop_list = [
            self.name,
            self.formation.name, 
            "{:^.3f}{}".format(self.get_damage() ,"dam"), 
            "{:^.3f}{}".format(self.get_attack_speed(),"spd"), 
            "{:^.3f}{}".format(self.get_health(),"hp"),
            "{:^.3f}{}".format(self.initiative, "initiative:"),
            "{} {}".format(str(self.get_casulties()), "lost")
        ]
        string =  "|".join("{: ^25}".format(x) for x in prop_list)

        return string       

    def attack(self, foe, log):
        """
            Represents ability to attack
        """
        if(foe.get_health() > 0 and self.get_health() > 0): 
            for a_unit in self.get_member_list():
                for d_unit in foe.get_member_list():
                    if "get_healing_strenght" in dir(a_unit):
                        log.info(a_unit.get_name() + " applies heal")
                        a_unit.heal(self.get_member_list())         
                    d_unit = a_unit.attack(d_unit)
        return foe             

    def calculate_initiative(self):
        """
            Calculating squad initiative, which 
            is determines ability to attack first
        """
        if len(self.member_list) > 0:
            total_damage = 0
            total_speed = 0
            total_health = 0            
            for i in self.member_list:
                if i.get_health() > 0:
                    total_damage += i.get_damage() * 0.85
                    total_speed += i.get_attack_speed()
                    total_health += i.get_health() * 0.70

            self.initiative = (total_damage + total_speed + total_health) / len(self.member_list) 

    def get_casulties(self):
        """
            Calculating and returns count of 
            lost units (those whose health <= 0)
        """
        temp = 0
        for i in self.member_list:
            if i.get_health() <= 0:
                temp += 1 

        if temp > self.casulties:
            self.casulties = temp
            
        return self.casulties

    def is_capable(self):
        """
            Returns True if at list one of units
            survived, othervise - False
        """
        self.calculate_initiative()
        for i in self.member_list:
            if i.get_health() > 0:
                return True
        return False

    def refresh_member_list(self):
        """
            Removing 'dead' units
        """
        for i, instance in enumerate(self.member_list):
            if instance.get_health() <= 0:
                self.delete_member(i)

    def refresh_formation(self):
        """
            Applying formatin, if unit list 
            changed
        """
        if len(self.member_list) > 0:
            self.member_list = self.formation.apply_formation(self.member_list)

    def add_member(self, member):
        """
            Add new member to the list of units
        """
        self.member_list.append(member)
        self.refresh_formation()
        self.calculate_initiative()     

    def get_last_member(self):
        """
            Get last added member o squad
        """
        return self.member_list[len(self.member_list)-1]

    def delete_member(self, pos):
        """
            Delating squad member, by passing 
            position argument
        """
        if pos > 0 and pos < len(self.member_list):
            del self.member_list[pos]

    def get_member_list(self):
        """
            Returns list of units in squad
        """
        return self.member_list

    def set_member_list(self, member_list):
        """
            Set list of units, by passing
            member_list argument
        """
        self.member_list = member_list
        self.refresh_formation()
        self.calculate_initiative()

    def get_formation(self):
        """
            Get current formatin of squad
        """
        return self.formation

    def set_formation(self, formation):
        """
            Set and apply new formation, by passing 
            formation argument
        """
        self.formation = formation
        self.refresh_formation()

    def get_initiative(self):
        """  Returns current initiative """
        return self.initiative

    def get_damage(self):
        """ 
            Returns damage sum of all units
        """
        damage = 0
        for i in self.member_list:
            damage += i.get_damage()            
        return damage

    def get_attack_speed(self):
        """ 
            Returns attack speed sum of all units
        """        
        get_attack_speed = 0
        for i in self.member_list:
            get_attack_speed += i.get_attack_speed()            
        return get_attack_speed

    def get_health(self):
        """ 
            Returns health sum of all units
        """        
        health = 0
        for i in self.member_list:
            health += i.get_health()
        return health



