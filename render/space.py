from blessed import Terminal

class Space:
    
    def __init__(self):
        self.term = Terminal()
        
    def render(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            print(self.term.clear + self.term.home)
            print(self.term.on_color_rgb(25, 25, 25) + " " * self.term.width * self.term.height, 
                  end="", flush=True)
            
            while True:
                
                key = self.term.inkey(timeout=0.1)

                if key.name == "KEY_ESCAPE":
                    break
                

                    
                