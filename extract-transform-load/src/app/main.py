from src.pipeline import ExtractWorldData, ExtractKaggle
import pandas as pd

class Main:
    def __init__(self):
        self.__extract_world_data = ExtractWorldData.load_api_url()
        self.__extract_kaggle = ExtractKaggle.load_api_url()
        
    
    def run(self):
        raw_dataset = self.__extract_world_data.fetch_data()
        self.__extract_kaggle.fetch_data()
        
        
        # temporario
        df = pd.read_csv(raw_dataset, sep=',')
        df.to_csv('../data/dataset-casos-cancer.csv')
        
        
if __name__ == "__main__":
    m = Main()
    m.run()
        
        
    