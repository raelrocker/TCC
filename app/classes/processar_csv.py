import pandas as pd


class ProcessarDados:

    def processarCSV(self, arquivoCSV):
        column_names = ['entrada', 'saida', 'placa', 'permanencia', 'valor']
        df = pd.read_csv(arquivoCSV, sep=',', header=None, parse_dates=[0, 1])
        df.columns = column_names
        return self._prepararDataFrame(df)

    def _prepararDataFrame(self, dataframe):
        df = dataframe.dropna(subset=['entrada', 'saida'])
        df = df.fillna(0)
        return df