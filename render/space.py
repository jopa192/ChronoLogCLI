from blessed import Terminal
from items.table import Table
from items.inputbox import InputBox
from rich import box

class Space:
    
    def __init__(self):
        self.term = Terminal()
        
    def render(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            print(self.term.clear + self.term.home)
            print(self.term.on_color_rgb(25, 25, 25) + " " * self.term.width * self.term.height, 
                  end="", flush=True)
            
            while True:
                
                key = self.term.inkey(timeout=0.5)

                if key.name == "KEY_ESCAPE":
                    break
                
                # For test case
                elif key.lower() == "t":
                    t = Table(5, 5, title="Table 1", box=box.ROUNDED)
                    t.add_column("Col 1")
                    t.add_column("Col 2")
                    t.add_row("Row 11", "Row 12")
                    t.add_row("Row 21", "Row 22")
                    t.update()
                    t.render(self.term)
                    
                elif key.lower() == "i":
                    i = InputBox(0, self.term.height-3)
                    i.update()
                    i.render(self.term)    
                    
                elif key.lower() == "d":   
                    i.delete(self.term)    
                    t.delete(self.term)
                    
                