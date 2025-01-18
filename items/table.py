from rich.table import Table as rTable
from items.item import Item


class Table(Item):
    
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x, y)
        self.table = rTable(*args, **kwargs) 
        self.printable = self.table
        
    def __getattr__(self, name):
        return getattr(self.table, name)