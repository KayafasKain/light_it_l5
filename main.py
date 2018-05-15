from random import randint
from math import ceil
import copy

from unit import unit as un
from unit import healer as he

from unit.unit_type import unit_type as ut
from unit import squad as sq 
from combat import formation as fo
from combat import battle as ba
from file_input import file_input as fi


def initiate(squad, units, formations, side_name, ranks, sizes, depth=0):
    if depth == len(ranks)-1:
        for i in range(int(sizes[ranks[depth]])):            
            squad.add_member(units[randint(0, len(units)-1)])
        return
    else:
        for i in range(sizes[ranks[depth]]):
            squad.add_member(sq.Squad(side_name + " " + ranks[depth] + str(i), [], formations[randint(0, len(formations)-1)]))
            initiate( squad.get_last_member(), units, formations, side_name, ranks, sizes, depth+1)    

def main():

    ranks = {
        0: "army",
        1: "squad",
        2: "unit"
    }

    sizes = {
        "army": 2,
        "squad": 2,
        "unit": 5
    }
    
    unit_types = {
        "inf": ut.UnitType("infantry", 0.9, 1.4, 0.9),
        "zep": ut.UnitType("zeppelin", 2.3, 1.1, 2.7),
        "tank": ut.UnitType("tank", 1.2, 2.4, 2.9)      
    }

    eq_units = [
        un.Unit("guards", unit_types["inf"], 100, 70, 140),
        un.Unit("wonderbolt", unit_types["inf"], 110, 120, 95),
        un.Unit("baloon", unit_types["zep"], 150, 100, 160),
        he.Healer("medical unicorn", unit_types["inf"], 30, 10, 180, 60)
    ]

    som_units = [
        un.Unit("slave", unit_types["inf"], 120, 80, 90),
        un.Unit("dragon", unit_types["inf"], 120, 30, 190),
        un.Unit("changelig tank", unit_types["tank"], 120, 80, 90),
        he.Healer("leach-healer", unit_types["zep"], 35, 100, 190, 20)
    ]

    formations = [
        fo.Formation("fastest ahead", 2),
        fo.Formation("strongest ahead", 1),
        fo.Formation("helthiest ahead", 3),
    ]

    while True:
        print("squad consist of units")
        print("army consist of squad")
        print("force consist of armies")
        try:
            sizes["unit"] = int(input("Pleas, enter squad size (must be > 2): ")) 
            sizes["squad"] = int(input("Pleas, enter army size (must be > 2): ")) 
            sizes["army"] = int(input("Pleas, enter force size (must be > 2): "))

            if sizes["unit"] < 2 or sizes["squad"] < 2 or sizes["army"] < 2:
                raise ValueError("Sizes must be > 2")       

        except ValueError as e:
            print(e)
        finally:
            sizes["unit"] = 2
            sizes["squad"] = 2
            sizes["army"] = 2        

        eq_force = sq.Squad("lf_middle", [], formations[randint(0, len(formations)-1)])
        som_force = sq.Squad("sombra", [], formations[randint(0, len(formations)-1)]) 

        initiate(eq_force, eq_units, formations, eq_force.get_name(), ranks, sizes, 0)
        initiate(som_force, som_units, formations, som_force.get_name(), ranks, sizes, 0)           

        battle = ba.Battle(eq_force, som_force, ranks)
        battle.print_army_rec(eq_force, ranks)
        battle.print_army_rec(som_force, ranks)
        battle.encouter()
           





main()