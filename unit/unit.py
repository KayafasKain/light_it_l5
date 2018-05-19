from .unit_type import unit_type as ut
from math import ceil

class Unit:
    """
        These class stands for representing
        unit of any type, name and stats
    """
    def __init__(self, name = "Wonderbolt", unit_type = ut.UnitType(), damage = 50,
                attack_speed = 200, health = 100):
        """
            Initializing Unit instance by passing
            name, type object(inflicts unit stats) 
            and stats theself (expressed in numerical)
            values
        """
        self.name = name
        self.unit_type = unit_type
        self.cooldown = 0
        self.cooldown_default = 0
        self.damage = damage
        self.expirience = 1
        self.attack_speed = attack_speed * unit_type.get_attack_speed_rate()
        self.health = health * unit_type.get_health_rate()
        self.health_default = self.health
        self.attack_speed_default = self.attack_speed
        
    def __repr__(self):
        return self.name    

    def __str__(self):
        """
            Returns a string representation (name 
            and stats)of current Unit instance
        """
        prop_list = [
                        self.name,
                        "{:^.3f}{}".format(self.damage,"dam"), 
                        "{:^.3f}{}".format(self.attack_speed,"spd"), 
                        "{:^.3f}{}".format(self.health,"hp")
                    ]

        string = "|".join("{: ^15}".format(x) for x in prop_list)

        return "|{}|".format(string)

    def attack(self, foe, log):
        """
            Gives ability to attack. Accepts and returns 
            "foe" - the instance of enemy unit
        """
        try: 
            foe.get_name()
        except(e):
            print(e)

        self.decrease_cooldown()

        if self.get_health() > 0 and self.get_cooldown() == 0:
            faster_strike = self.get_attack_speed() > foe.get_attack_speed()
            strikes_per_turn = 1
            if faster_strike:
                #calculating ability of additiona strikes
                speed_overwhelming = int(ceil(self.get_attack_speed() / (1 + foe.get_attack_speed()))) 
                if speed_overwhelming > strikes_per_turn:
                    strikes_per_turn = speed_overwhelming 

            for i in range(0, strikes_per_turn):
                log.warning("{} {} {}".format( 
                        self.name, 
                        "dealing damage: " ,
                        (self.get_damage() * self.expirience)
                    )
                )
                foe.set_health(foe.get_health() - (self.get_damage() * self.expirience))
                if foe.get_health() <= 0:
                    break
                            
            self.expirience += 0.01

            foe.refresh_stats()

            #if attacker slower than defender, defender hits the attacker.
            if not faster_strike:
                self.set_health(self.get_health() - foe.get_damage())

            self.refresh_stats()
            self.set_cooldown()

        elif self.get_cooldown() > 0:
            log.warning("{} {} {}".format(self.get_name(), "in cooldown for: " ,self.get_cooldown()))


        return foe

    def refresh_stats(self):
        """
            Refreshing attack speed depending on 
            difference between 
        """
        if self.health_default > self.health:
            if self.health > 0:
                if self.unit_type.get_health_rate() >= 2:
                    self.set_attack_speed(self.attack_speed - (self.health_default - self.health/2))
                else:
                    self.set_attack_speed(self.attack_speed - (self.health_default - self.health))

            if self.attack_speed < 0:
                self.set_attack_speed(0) 
            if self.health < 0:
                self.set_health(0)
                self.set_attack_speed(0) 
                self.set_damage(0)                                  

    def calculate_default_cooldown(self):
        """
            Calculating unit cooldown, depends on
            all stats
        """
        self.cooldown_default = (self.get_damage() * 0.7) + (self.get_health() * 0.3) + (self.get_attack_speed() * 1.1)
        return int(self.cooldown_default / self.get_attack_speed())

    def get_cooldown_default(self):
        """
            Get default cooldown
        """
        return self.cooldown_default

    def get_cooldown(self):
        """
            Get current cooldown
        """
        return self.cooldown

    def set_cooldown(self):
        """ set cooldown """
        self.cooldown = self.get_cooldown_default()

    def decrease_cooldown(self):
        """ 
            Decreasing cooldown
        """
        self.cooldown -= 1
        if self.cooldown < 0:
            self.cooldown = 0       

    def get_type(self):
        """ Returns unit type """
        return self.unit_type

    def set_type(self, unit_type = ut.UnitType()):
        """ Set unit type, by passing Type instance """
        self.unit_type = unit_type

    def get_name(self):
        """ Returns unit name """        
        return self.name

    def set_name(self, name = "Wonderbolt"):
        """ Set unit name, by passing a string """
        self.name = name
        
    def get_damage(self):
        """ Returns unit damage """
        return self.damage * self.unit_type.get_damage_rate()

    def set_damage(self, damage = 50):
        """ Set damage, by passing numerical value """
        self.damage = damage

    def get_attack_speed(self):
        """ Get unit attack speed """
        return self.attack_speed

    def get_attack_speed_default(self):
        """ Get unit defult attack speed """
        return self.attack_speed_default

    def set_attack_speed(self, attack_speed = 200):
        """ Set attack speed, by passing numerical value """
        self.attack_speed = attack_speed

    def get_health(self):
        """ Returns unit health """
        return self.health

    def get_health_default(self):
        """ Returns default unit health """        
        return self.health_default

    def set_health(self, health):
        """ Set current unit health, by 
            passing numerical value 
        """
        if health > self.health_default:
            self.health = self.health_default
        elif health < 0:
            self.health = 0
        else:    
            self.health = health    
