from .unit import Unit
from .unit_type import unit_type as ut

class Healer(Unit):
    """
        Support unit, may eather attack
        foes and heal friends, inherit 
        from Unit
    """
    def __init__(self, name = "Medical Unicorn", unit_type = ut.UnitType(), damage = 50,
                attack_speed = 30, health = 100, healing = 80):
        super().__init__(name, unit_type, damage, attack_speed, health)
        """
            Initializing Unit instance by passing
            name, type object(inflicts unit stats) 
            and stats theself (expressed in numerical)
            values, healing_strenght added

        """        
        self.healing_strenght = healing

    def heal(self, squad_members):
        """
            Allows healer to heal. Acepts the list of
            squad members. Each time find wounded 
            and heals all of them. The amount of
            restoret health and speed depends on
            own healing_strenght and amound of 
            wounded
            
        """
        wounded_count, pos_list = self.count_wounded(squad_members)

        if wounded_count > 0:
            heal_strenght = self.healing_strenght / wounded_count
            for i in pos_list:
                self.restore_health(squad_members[i], heal_strenght)
                self.restore_speed(squad_members[i], heal_strenght)

    def restore_health(self, member, heal_strenght):
        """
            Restores some health of friendly unit.
            Accepts member of squad and heal strenght
        """
        health_restore = heal_strenght + member.get_health()
        if health_restore > member.get_health_default():
            member.set_health(member.get_health_default())
        else:
            member.set_health(health_restore + member.get_health())

    def restore_speed(self, member, heal_strenght):
        """
            Restores some health of friendly unit.
            Accepts member of squad and heal strenght
        """        
        speed_restore = heal_strenght + member.get_attack_speed()
        if speed_restore > member.get_attack_speed_default():
            member.set_attack_speed(member.get_attack_speed_default())
        else:
            member.set_attack_speed(speed_restore + member.get_attack_speed())                      

    def count_wounded(self, squad_members):
        """
            Counts wounded, sccepts list of 
            squad members, returns count of
            wounded and list of positions in 
            a squad 
        """
        counter = 0
        pos_list = []
        for i, member in enumerate(squad_members):
            if member.get_health() > 0 and member.get_health() < member.get_health_default():
                counter += 1
                pos_list.append(i)

        return counter, pos_list

    def get_healing_strenght(self):
        """ Returns healing strenght """
        return self.healing_strenght

    def set_healing_strenght(self, healing = 80):
        """ Set healing strenght  """
        self.healing_strenght = healing