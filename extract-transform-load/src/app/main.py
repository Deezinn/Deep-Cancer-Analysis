from src.pipeline import Extract

class Main:
    def __init__(self):
        self.__extract = Extract()
    
    def run(self):
        self.__extract.load_data()
    
if __name__ == "__main__":
    m = Main()
    m.run()
        
        
    