from blessed import Terminal
from items.table import Table

class Space:
    
    def __init__(self):
        self.term = Terminal()   
        self.term_width = self.term.width
        
    def render(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            print(self.term.clear + self.term.home)
            print(self.term.on_color_rgb(25, 25, 25) + " " * self.term.width * self.term.height, 
                  end="", flush=True)
            
            while True:
                
                key = self.term.inkey(timeout=0.5)

                if key.name == "KEY_ESCAPE":
                    break
                
                elif key.lower() == "t":
                    t = Table(0, 0, title="Table 1")
                    t.add_column("Col 1")
                    t.add_column("Col 2")
                    t.add_row("Row 11", "Row 12")
                    t.add_row("Row 21", "Row 22")
                    t.update()
                    t.render(self.term)
                    
                    
                    
                