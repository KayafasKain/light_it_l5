from file_works import custom_logger as cla
import logging
import os

"""
    Work in progress yet
"""
class Battle:
    """
        Tese class allows to fight armies,
        which are consist of squads and
        squads consists of units
    """
    def __init__(self, army_one, army_two, ranks):
        """
            Accepting two armies
        """
        try:
            self.army_one = army_one
            self.army_two = army_two
            self.ranks = ranks
            custom_log = cla.CustomLogger()
            self.log = custom_log.get_logger("COMBAT") 
            self.log.info("Battle is about to start!") 
                                
        except NameError as e:
            print(e)

    def encouter(self):
        """
            Determines attack turns
        """
        self.log.info("Battle is about to start!")
        form_str = "{:/^125}"      
        while self.army_one.is_capable() and self.army_two.is_capable():
            if self.army_one > self.army_two:  
                self.log.info(self.army_one.get_name() + " strikes first! ")
                self.army_one.attack(self.army_two, self.log)
            else:
                self.log.info(self.army_one.get_name() + " strikes first! ")
                self.army_two.attack(self.army_one, self.log)

        if self.army_one.is_capable():
            self.print_army_rec(self.army_one, self.ranks, "won!", 0)
            self.print_army_rec(self.army_two, self.ranks, "lost!", 0)
        else:
            self.print_army_rec(self.army_two, self.ranks, "won!", 0)
            self.print_army_rec(self.army_one, self.ranks, "lost!", 0)

    def print_army_rec(self, army, ranks, outcome = "", depth = 0):
        """
            Print army recursivly, recursion remain till 
            depth come to the ehnd of the ranks
        """
        if depth == 0:
            form_str = "{:=^125}"
            self.log.info(form_str.format(army.get_name() + " " + outcome))
            self.log.info(str(army))
        elif ranks[depth-1] == "army":
            form_str = "{:+^" + str(len(str(army))) + "}"
            self.log.info(form_str.format(""))            
        elif ranks[depth-1] == "squad":
            form_str = "{:_^" + str(len(str(army))) + "}"
            self.log.info(form_str.format(""))

        if depth == len(ranks):
            return
        else:
            for k in army.get_member_list():
                self.log.info(str(k))
                self.print_army_rec(k, ranks, outcome, depth + 1)
            form_str = "{:*^" + str(len(str(army))) + "}"
            self.log.info(form_str.format(""))
