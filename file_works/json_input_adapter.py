import json
from random import randint

from unit import unit as un
from unit import vehicle as ve

from unit.unit_type import unit_type as ut
from unit import squad as sq 
from unit import army as ar
from combat import formation as fo
from combat import strategy as st

class JsonInputAdapter():
    
    def __init__(self, file_path):
        """
            Initializing, by passing path to
            json file
        """
        self.file_path = file_path
        self.ranks = {
            0: "army",
            1: "squad",
            2: "unit"
        }

        self.strategies = [
            st.Strategy("strongest first", 1),
            st.Strategy("weakest first", 2),
            st.Strategy("fastest first", 3),
            st.Strategy("slowest first", 4),
            st.Strategy("helthiest first", 5),
            st.Strategy("weak constitudtion first", 6),
        ]

        self.formations = [
            fo.Formation("fastest ahead", 2),
            fo.Formation("strongest ahead", 1),
            fo.Formation("helthiest ahead", 3),
        ] 

        self.unit_types = {
            "inf": ut.UnitType("infantry", 0.9, 1.4, 0.9),
            "zep": ut.UnitType("zeppelin", 2.3, 1.1, 2.7),
            "tank": ut.UnitType("tank", 1.2, 2.4, 2.9)      
        }                     


        self.read_json()

    def read_json(self):
        """
            Read json file and save to
            self.data
        """
        with open(self.file_path) as f:
            self.data = json.load(f)

    def convert(self):
        """
            converting json to force object
        """
        self.recognize_strategy()
        self.prepeare_sizes()
        self.one_force = ar.Army(self.data["armies"][0]["name"] , [], self.formations[randint(0, len(self.formations)-1)], self.strategy)
        self.initiate(self.one_force, self.formations, self.strategies, self.data["armies"], self.ranks, self.sizes, 0) 

        return self.one_force

    def initiate(self, squad, formations, strategies, data, ranks, sizes, strategy, depth = 0):
        """
            Recursively filling force object
        """
        if depth == len(ranks)-1:
            for i in data:
                print(i)
                if "vehicle" in i["name"]:
                    squad.add_member(ve.Vehicle(i["name"], 
                    self.unit_types["tank"],
                    crew = [
                            un.Unit("crew", self.unit_types["tank"], 0, 30, 50),
                            un.Unit("crew", self.unit_types["tank"], 0, 30, 50),
                            un.Unit("crew", self.unit_types["tank"], 0, 30, 50)
                        ]
                    ))
                else:
                    squad.add_member( un.Unit(i["name"], self.unit_types["inf"], 50, 50, 50))                                                                        
            return
        else:
            for i in data: 
                if 'squads' in i.keys(): 
                    squad.add_member(ar.Army(i["name"], [], formations[randint(0, len(formations)-1)], strategies[randint(0, len(strategies)-1)]))
                    self.initiate( squad.get_last_member(), self.formations, self.strategies, i["squads"], self.ranks, self.sizes, strategy, depth+1)
                elif 'units' in i.keys(): 
                    squad.add_member(sq.Squad(i["name"], [], formations[randint(0, len(formations)-1)]))
                    self.initiate( squad.get_last_member(), self.formations, self.strategies, i['units'], self.ranks, self.sizes, strategy, depth+1) 

    def recognize_strategy(self):
        """
            Recognozing and saving strategy
        """
        if "random" in self.data["armies"][0]["strategy"]:
            self.strategy = self.strategies[randint(0, len(self.strategies)-1)]
        elif "weakest" in self.data["armies"][0]["strategy"]:
            self.strategy = self.strategies[1]
        elif "strongest" in self.data["armies"][0]["strategy"]:
            self.strategy = self.strategies[0]
        else:
            self.strategy = self.strategies[randint(0, len(self.strategies)-1)]

    def prepeare_sizes(self):
        """
            Prepearing dictionary of sizes
        """
        self.sizes = {
            "army": self.get_armies_num(),
            "squad": self.get_sqads_num(),
            "unit": self.get_units_num()
        } 
        print(self.sizes)             

    def get_armies_num(self):
        """
            Get count of armies
        """
        return len(self.data["armies"])

    def get_sqads_num(self):
        """
            Get count of squads
        """
        return len(self.data["armies"][0]["squads"])

    def get_units_num(self):
        """
            Get count of units
        """
        return len(self.data["armies"][0]["squads"][0]["units"])                   

    