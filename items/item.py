import re

class Item:

    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1
        self.print_lines = []
        
    @staticmethod
    def anis_len(line):
        ansi_escape = re.compile(r"\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        visible_string = ansi_escape.sub('', line)
        return len(visible_string)
    
    def render(self, term):
        print(term.home, term.move_down(self.y))
        for line in self.print_lines:
            print(term.move_right(self.x) + line)
        