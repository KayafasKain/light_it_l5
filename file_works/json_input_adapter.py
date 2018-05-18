import json
import argparse


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
        with open("data.json") as f:
            self.data = json.load(f)

    def get_armies_num(self):
        return len(self.data)

def main():
    parser = argparse.ArgumentParser(
        description="Adapting battle simulator json",
    )

    parser.add_argument(
        "forces",
        metavar="NAME",
        nargs="+",
        help="Force name",
    )
