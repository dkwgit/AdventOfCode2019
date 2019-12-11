class Image:

    def __init__(self,columns, rows, rawData):
        self._columns = columns
        self._rows = rows
        self._rawData = rawData
        self._layers = []

    def Process(self):
        assert(len(self._rawData)  % (self._columns * self._rows) == 0)
        numberOfLayers = int(len(self._rawData) / (self._columns * self._rows))
        for i in range(0,numberOfLayers):
            self._layers.append(self._rawData[i*(self._columns * self._rows):(i+1)*(self._columns * self._rows)])
        assert(len(self._layers[0])==self._columns * self._rows)
    
    def GetLayers(self):
        return self._layers
