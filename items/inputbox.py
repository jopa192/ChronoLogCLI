from items.item import Item
from rich.panel import Panel


class InputBox(Item):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.printable = Panel("")