# Dado el sheet click , dirigirse al tab reto1 donde se encuentra una tabla con los autores
# que han sido clasificados en base a sentimiento, country y thema. Se necesita que se realice
# una pivot table en la cual las columnas base sean author y sentimiento y las columnas variables
# sean country y thema. Aqui un ejemplo del formato de salida del doc. Las columnas de country y
# tema serán variables dependiendo del total de countries y temas que exista en el sheet de base,
# ejemplo si en la base existen 12 countries , esta sección en el sheet de salida deberá tener 12
# columnas , del mismo modo con temas.

# El sheet de salida tiene que estar en el mismo formato que el del ejemplo , incluido las columnas
# de cabecera del ejemplo además que el tab deberá ser creado desde 0, no se admite que exista un
# template fijo al momento de crearlo

# Este reto debe ser realizado en python en conjunto con el uso del api de google sheet y el test
# del reto será modificando la data de la base para comprobar su dinamismo.

import pandas as pd
from .google_sheets_test import google_sheets_test

# Se crea una instancia de la clase google sheet
instanciaSheets = google_sheets_test("Copia Python")


class create_table:

    def __init__(self, records, worksheet, worksheet_name):
        self.df = pd.DataFrame(instanciaSheets.getAllRecords(records))
        self.worksheet = worksheet
        self.worksheet_name = worksheet_name

    def init(self):
        # Se imprime lo que se ha modificado
        tabla = self.crearTabla(["Country", "Theme"], self.df)
        self.ingresarTablaGoogleSheets(
            self.worksheet, self.worksheet_name, tabla)
        return tabla

    def crearTabla(self, indexArray, dataFrame):

        # Variables importantes
        dataframe_collection = {}
        columnsFrames = []
        valuesFrames = []
        indexFrames = []
        valuesFramesFinal = []
        special = []
        length = []
        contador = 0

        for index in indexArray:
            dataframe_collection[index] = pd.crosstab(
                [dataFrame["Author"], dataFrame["Sentiment"]], dataFrame[index], rownames=["Author", "Sentiment"]).astype(bool)

        for key in dataframe_collection.keys():
            length.append(
                len(dataframe_collection[key].columns.values.tolist()))
            columnsFrames = columnsFrames + \
                dataframe_collection[key].columns.values.tolist()

            indexFrames = dataframe_collection[key].index.tolist()

            valuesFrames = valuesFrames + \
                [dataframe_collection[key].values.tolist()]

        for array in valuesFrames[0]:
            array = list(indexFrames[contador]) + \
                array + valuesFrames[1][contador]
            valuesFramesFinal.append(array)
            contador += 1

        columnsFrames.insert(0, "Sentiment")
        columnsFrames.insert(0, "Author")

        special = columnsFrames.copy()
        special[0] = ""
        special[1] = ""
        special[2] = indexArray[0]
        special[length[0]+3] = indexArray[1]

        return [special] + [columnsFrames] + valuesFramesFinal + [length]

    def ingresarTablaGoogleSheets(self, worksheet, nameWorksheet, dataFrame):

        start1 = (1, 3)
        end1 = (1, dataFrame[len(dataFrame)-1:][0][0]+3)
        start2 = (1, dataFrame[len(dataFrame)-1:][0][0]+4)
        end2 = (1, dataFrame[len(dataFrame)-1:][0][1] +
                dataFrame[len(dataFrame)-1:][0][0]+2)

        instanciaSheets.deleteWorksheet(worksheet)
        instanciaSheets.createWorksheet(nameWorksheet)
        instanciaSheets.merge(nameWorksheet, start1, end1)
        instanciaSheets.merge(nameWorksheet, start2, end2)
        dataFrame.pop()
        instanciaSheets.writeWorksheet(dataFrame, worksheet)
