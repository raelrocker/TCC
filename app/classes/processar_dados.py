import json

import pandas as pd
from pandas.io.json import json_normalize
from xml.etree import ElementTree

class ProcessarDados:

    def processarCSV(self, arquivoCSV):
        column_names = ['entrada', 'saida', 'placa', 'permanencia', 'valor']
        df = pd.read_csv(arquivoCSV, sep=',', header=None, parse_dates=[0, 1])
        df.columns = column_names
        return self._prepararDataFrame(df)

    def processarXml(self, arquivoXML):
        if (type(arquivoXML) is str):
            root = ElementTree.fromstring(arquivoXML)
        else:
            tree = ElementTree.parse(arquivoXML)
            root = tree.getroot()
        data = []
        for registro in root:
            entrada = registro.find('entrada').text
            saida = registro.find('saida').text
            placa = registro.find('placa').text
            permanencia = registro.find('permanencia').text
            valor = registro.find('valor').text
            data.append([entrada, saida, placa, permanencia, valor])
        df = pd.DataFrame(data, columns=['entrada', 'saida', 'placa', 'permanencia', 'valor'])
        return  self._prepararDataFrame(df)

    def processarJSON(self, arquivoJSON):
        dados = json.loads(arquivoJSON)
        df = pd.DataFrame.from_dict(dados['registros'])
        return df

    def _prepararDataFrame(self, dataframe):
        df = dataframe.dropna(subset=['entrada', 'saida'])
        df = df.fillna(0)
        return self._prepararDataFrame(df)

if __name__ == "__main__":

    proc = ProcessarDados()
    file = open('teste.json').read().replace('\n', '')
    df = proc.processarJSON(file)
    print(df)