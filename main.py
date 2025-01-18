from render.space import Space

class App:
    
    def __init__(self):
        self.space = Space()
        
        
    def run(self):
        self.space.render()
        
        
if __name__ == "__main__":
    App().run()