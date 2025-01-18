from blessed import Terminal

class Space:
    
    def __init__(self):
        self.term = Terminal()    
        self.term_width = self.term.width
        
        
    def render(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            print(self.term.clear + self.term.home)
            
            while True:
                
                key = self.term.inkey(timeout=0.5)

                if key.name == "KEY_ESCAPE":
                    break