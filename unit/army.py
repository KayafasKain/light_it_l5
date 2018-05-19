from combat import formation as fo
from combat import strategy as st
from .squad import Squad

class Army(Squad):
    """
        Represents a set of squads,
        determines strategy of combat
    """

    def __init__(self, name = "some party", member_list = None, formation = fo.Formation(), strategy = st.Strategy() ):
        """
            Initializing object, by passing
            name, list of memebers, formation and
            strategy
            also, calculating some depended paremeters
        """
        super().__init__(name, member_list, formation)
        self.strategy = strategy

    def __str__(self):
        """
            Converting class instace to string
        """
        self.calculate_initiative()
        prop_list = [
            self.name,
            "{} {}".format("format:", self.formation.name),
            "{} {}".format("strat:", self.strategy.name), 
            "{} {:^.3f}".format("initiative:", self.initiative),
            "{} {}".format(str(self.get_casulties()), "lost")
        ]
        string =  "|".join("{: ^15}".format(x) for x in prop_list)

        return string          

    def attack(self, foe, log):
        """
            Represents ability to attack
        """
        if(foe.get_health() > 0 and self.get_health() > 0): 
            foe.set_member_list(self.apply_strategy(foe.get_member_list())) 
            for a_squad in self.get_member_list():
                for d_squad in foe.get_member_list():
                    log.info("attacking: ")
                    log.info(str(a_squad))
                    log.info("defending: ")
                    log.info(str(d_squad))                
                    if "get_healing_strenght" in dir(a_squad):
                        a_squad.heal(self.get_member_list())         
                    d_squad = a_squad.attack(d_squad, log) 
                    if a_squad.get_health() > d_squad.get_health():
                        log.info("won: ")
                        log.info(str(a_squad))
                    else:
                        log.info("won: ")
                        log.info(str(d_squad))

        return foe                                                         

    def get_strategy(self):
        """
            Get current strategy of army
        """
        return self.formation

    def set_strategy(self, strategy):
        """
            Set and apply new strategy, by passing 
            strategy argument
        """
        self.strategy = strategy

    def apply_strategy(self, members):
        return self.strategy.apply_strategy(members)  

    def set_member_list(self, member_list):
        """
            Set list of units, by passing
            member_list argument
        """
        self.member_list = member_list
        self.calculate_initiative()
