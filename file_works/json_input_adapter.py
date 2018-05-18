import json
import argparse

from unit import unit as un
from unit import healer as he
from unit import vehicle as he

from unit.unit_type import unit_type as ut
from unit import squad as sq 
from unit import army as ar
from combat import formation as fo
from combat import strategy as st
from combat import battle as ba

class JsonInputAdapter():
    
    def __init__(self, file_path):
        """
            Initializing, by passing path to
            json file
        """
        self.file_path = file_path
        self.read_json()

    def read_json(self):
        """
            Read json file and save to
            self.data
        """
        with open(self.file_path) as f:
            self.data = json.load(f)

    def get_armies_num(self):
        """
            Get count of armies
        """
        return len(self.data["armies"])

    def get_sqads_num(self):
        """
            Get count of squads
        """
        return len(self.data["armies"]["squads"])

    def get_sqads_num(self):
        """
            Get count of units
        """
        return len(self.data["armies"]["squads"]["units"])                   

# def main():
#     parser = argparse.ArgumentParser(
#         description="Adapting battle simulator json",
#     )

#     parser.add_argument(
#         "path",
#         metavar="PATH",
#         nargs="+",
#         help="Force name",
#     )

#     args = parser.parse_args()
#     instance = JsonInputAdapter(args.path[0])
#     print(instance.get_armies_num())

#     # print(instance.get_armies_num)
    
# main()