import pandas as pd
from io import StringIO

class TransformWorldData:
    def __init__(self, dataframe) -> None:
        self.__dataframe = dataframe
    
    @classmethod
    def to_dataframe(cls, raw_data):
        if raw_data:
            return cls(dataframe=pd.read_csv(StringIO(raw_data)))
        return None
            
    def process(self):
        self._rename_column()
        self._set_types()
        self._sanitize_str_columns()
        return self
        
    def _rename_column(self):
        nova_traducao = {}
        valores_traduzidos = ['entidade', 'codigo', 'ano', 'taxa_mortalidade', 'ano_referencia']
        
        for novo_nome, coluna_original in zip(valores_traduzidos, self.__dataframe.columns):
            nova_traducao[coluna_original] = novo_nome.lower()
            
        self.__dataframe = self.__dataframe.rename(columns=nova_traducao)
        
        # Deletando a coluna ano, pois, ela já se baseia no ano de referencia
        
        if 'ano' in self.__dataframe.columns:
            del self.__dataframe['ano']

    def _set_types(self):
        for coluna in self.__dataframe.columns:
            match coluna:
                case 'entidade' | 'codigo':
                    self.__dataframe[coluna] = self.__dataframe[coluna].astype('str')
                case 'ano' | 'ano_referencia':
                    self.__dataframe[coluna] = self.__dataframe[coluna].fillna(0).astype('int16')
                case 'taxa_mortalidade':
                    self.__dataframe[coluna] = self.__dataframe[coluna].fillna(0.0).astype('float32')
                case _:
                    pass
                
    def _sanitize_str_columns(self):
        self.__dataframe['entidade'] = (self.__dataframe['entidade'].str.title().str.strip())
        
        for coluna in self.__dataframe.columns:
            if coluna == 'entidade' or coluna == 'codigo':
                self.__dataframe[coluna] = self.__dataframe[coluna].fillna('Não informado')
                self.__dataframe[coluna] = self.__dataframe[coluna].replace('nan', 'Não informado')
            
            # temporario
        self.__dataframe.to_csv('../data/dataset-casos-cancer-process-pipeline.csv')
                    
                    
        

        

