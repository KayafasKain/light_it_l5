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
        except e:
            print(e)

    def encouter(self):
        """
            Determines attack turns
        """
        form_str = "{:/^125}"
        print(form_str.format("")) 
        print(form_str.format("( BATTLE REPORT )"))
        print(form_str.format(""))         
        while self.army_one.is_capable() and self.army_two.is_capable():
            if self.army_one.get_initiative() > self.army_two.get_initiative():  
                self.army_one.attack(self.army_two)
            else:
                self.army_two.attack(self.army_one)

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
            print(form_str.format(""))
            print(form_str.format(army.get_name() + " " + outcome))
            print(form_str.format(""))
            print(str(army))
            print()
        elif ranks[depth-1] == "army":
            form_str = "{:+^" + str(len(str(army))) + "}"
            print(form_str.format(""))            
        elif ranks[depth-1] == "squad":
            form_str = "{:_^" + str(len(str(army))) + "}"
            print(form_str.format(""))

        if depth == len(ranks):
            return
        else:
            for k in army.get_member_list():             
                print(str(k))
                self.print_army_rec(k, ranks, outcome, depth + 1)
            form_str = "{:*^" + str(len(str(army))) + "}"
            print(form_str.format(""))
