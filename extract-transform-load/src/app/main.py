from src.pipeline import ExtractWorldData, ExtractKaggle, TransformWorldData, TransformKaggle, LoadmWorldData, LoadKaggle
class Main:
    def __init__(self):
        self.__extract_world_data = ExtractWorldData.load_api_url()
        self.__extract_kaggle = ExtractKaggle.load_api_url()
        self.__tramsform_kaggle = TransformKaggle
        self.__LoadmWorldData = LoadmWorldData()
        self.__loadKaggle = LoadKaggle()

    def run(self):
        raw_dataset = self.__extract_world_data.fetch_data()
        path_dataset = self.__extract_kaggle.fetch_data()

        transformerWorldData = TransformWorldData.to_dataframe(raw_dataset)
        transformerKagge = self.__tramsform_kaggle.verify_if_exists(path=path_dataset)

        process_data = transformerWorldData.process()
        process_images = transformerKagge.transform_images()

        self.__LoadmWorldData.save(process_data)
        self.__loadKaggle.save(process_images)

        
if __name__ == "__main__":
    m = Main()
    m.run()
        
        
    