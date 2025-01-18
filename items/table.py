from rich.table import Table as rTable
from rich.console import Console as rConsole
from io import StringIO
from items.item import Item


class Table(Item):
    
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x, y)
        self.table = rTable(*args, **kwargs) 
        self.console = rConsole(file=StringIO(), force_terminal=True)
        
    def __getattr__(self, name):
        return getattr(self.table, name)
    
    def update(self):
        with self.console.capture() as capture:
            self.console.print(self.table)
        table_output = capture.get()
        
        self.print_lines = table_output.split("\n")[:-1]
        self.table_width = self.anis_len(self.print_lines[0])
        self.table_height = len(self.print_lines)