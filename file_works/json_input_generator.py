import argparse
import json
from random import randint
import sys
import os


class JsonInputGenerator():
    """
        Generates army json template
    """
    def __init__(self, name):
        """ Initiate by passing force name """
        self.name = name

    def generate_soldier(self, appendix = "crew"):
        """ Generating soldier or crew """
        return { 
            "name": "{} {} {}".format(self.name, "soldier", str(appendix)),
            "health": 50 
        }

    def generate_vehicle(self, appendix):
        """ Generating vehicle """
        return { 
                    "name": "{} {} {}".format(self.name, "vehicle", str(appendix)),
                    "health":50,
                    "operators": [
                        self.generate_soldier(),
                        self.generate_soldier(),
                        self.generate_soldier(),
                    ]
                }

    def generate_squad(self, appendix, v_min = 2, v_max = 2, s_min = 2, s_max = 2):
        """ 
            Generating squad, consist of soldiers and vehicles 
        """

        name = "{} {} {}".format(self.name, "squad", str(appendix))
        units = []
        for i in range(randint(v_min, v_max)):
            units.append(self.generate_vehicle(i))
        for i in range(randint(s_min, s_max)):
            units.append(self.generate_soldier(i))

        return { "name": name, "units": units }

    def generate_army(self, appendix, strategy = "random", sq_min = 2, sq_max = 2, v_min = 2, v_max = 2, s_min = 2, s_max = 2):
        """
            Generating army, consist of squads
        """

        name = "{} {} {}".format(self.name, "army", str(appendix))
        squads = []
        for i in range(randint(sq_min, sq_max)):
            squads.append(self.generate_squad(i, v_min, v_max, s_min, s_max))

        print("STRATARAERARARAR")
        print(strategy)
        return {
            "name": name,
            "strategy": strategy,
            "squads": squads
        }

    def generate_force(self, amount = 2, strategy = "random", sq_min = 2, sq_max = 2, v_min = 2, v_max = 2, s_min = 2, s_max = 2):
        """
            Generating force, consists of armies
        """

        armies = []
        for i in range(amount):
            armies.append(self.generate_army(i, strategy, sq_min, sq_max, v_min, v_max, s_min, s_max))

        return {
            "armies": armies
        }

def main():

    parser = argparse.ArgumentParser(
        description='Battle simulator template',
    )

    parser.add_argument(
        'forces',
        metavar='NAME',
        nargs='+',
        help='Force name',
    )

    parser.add_argument(
        'strategy',
        metavar='STRAT',
        nargs='+',
        help='Army strategy',
    )

    parser.add_argument(
        '--army-num',
        metavar='AMOUNT',
        type=int,
        required=False,
        help='Amount of armies',
    )

    parser.add_argument(
        '--min-squads',
        metavar='N',
        type=int,
        required=False,
        help="Min. number of squads per army",
    )

    parser.add_argument(
        '--max-squads',
        metavar='N',
        type=int,
        required=False,
        help="Max. number of squads per army",
    )

    parser.add_argument(
        '--min-soldiers',
        metavar='N',
        type=int,
        required=False,
        help="Min. number of soldiers per squad",
    )

    parser.add_argument(
        '--max-soldiers',
        metavar='N',
        type=int,
        required=False,
        help="Max. number of soldiers per squad",
    )

    parser.add_argument(
        '--min-vehicles',
        metavar='N',
        type=int,
        required=False,
        help="Min. number of vehicles per squad",
    )

    parser.add_argument(
        '--max-vehicles',
        metavar='N',
        type=int,
        required=False,
        help="Max. number of vehicles per squad",
    )

    parser.add_argument(
        '--pprint',
        action='store_true',
        help="Produce human-readable json",
    )

    args = parser.parse_args()

    dir_path = os.path.dirname(__file__)
    fname = dir_path + '_armies.json'
    generator = JsonInputGenerator(args.forces[0])
    result = generator.generate_force( 
        args.army_num, args.strategy[0],
        args.min_squads, args.max_squads,
        args.min_soldiers, args.max_soldiers,
        args.min_vehicles, args.max_vehicles
    )

    json.dump(result, sys.stdout, sort_keys=True, indent=2 if args.pprint else None)
    # with open(fname, 'r+') as outfile:
    #     json.dump(result, outfile, sort_keys=True, indent=2 if args.pprint else None)    


if __name__ == '__main__':
    sys.exit(main())