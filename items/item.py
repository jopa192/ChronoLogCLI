from rich.console import Console as rConsole
from io import StringIO
import re

class Item:

    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1
        self.print_lines = []
        
        self.console = rConsole(file=StringIO(), force_terminal=True)
        
    @staticmethod
    def anis_len(line):
        ansi_escape = re.compile(r"\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        visible_string = ansi_escape.sub('', line)
        return len(visible_string)
    
    def render(self, term):
        for l, line in enumerate(self.print_lines):
            print(term.home + term.move_xy(self.x, self.y+l) + line)
        print(term.home, end="")
        
    def delete(self, term):
        for l, line in enumerate(self.print_lines):
            print(term.home + term.move_xy(self.x, self.y+l) + " "*self.width)
        print(term.home, end="")
    
    def update(self):
        with self.console.capture() as capture:
            self.console.print(self.printable)
        output = capture.get()
        
        self.print_lines = output.split("\n")[:-1]
        self.width = max([self.anis_len(l) for l in self.print_lines])
        self.height = len(self.print_lines)
        