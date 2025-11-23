from src.pipeline import Extract

class Main:
    def __init__(self):
        self.__extract = Extract.load_api_url()
    
    def run(self):
        self.__extract.fetch_data()
    
if __name__ == "__main__":
    m = Main()
    m.run()
        
        
    