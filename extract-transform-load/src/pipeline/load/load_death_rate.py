import pandas as pd

class LoadmWorldData:
    def save(self, dataframe):
        if not dataframe.empty:
            dataframe.to_csv('../data/casos_cancer.csv')
