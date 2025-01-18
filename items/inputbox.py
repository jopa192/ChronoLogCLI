from items.item import Item
from rich.panel import Panel


class InputBox(Item):
    
    def __init__(self, tw, th):
        super().__init__(0, th-3)
        self.buffer = ""
        self.printable = Panel(self.buffer + "[#999999]|")
        print(tw)
        self.max_buffer_len = tw-5
        
    def type_in(self, char, term):
        self.buffer += char
        self.update_buffer(term)
        
    def delete(self, term):
        self.buffer = self.buffer[:-1]
        self.update_buffer(term)    
        
    def update_buffer(self, term):
        if len(self.buffer) > self.max_buffer_len:
            self.printable = Panel(self.buffer[len(self.buffer)-self.max_buffer_len:] + "[red]|")
        else:
            self.printable = Panel(self.buffer + "[red]|")
        self.update()
        self.render(term)