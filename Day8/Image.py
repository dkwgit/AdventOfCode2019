class Image:

    def __init__(self,rows, columns, rawData):
        self._rows = rows
        self._columns = columns
        self._rawData = rawData
        self._layers = []
        self._renderLayerPixels = []

    def Process(self):
        assert(len(self._rawData)  % (self._rows * self._columns) == 0)
        numberOfLayers = int(len(self._rawData) / (self._rows * self._columns))
        for layer in range(0,numberOfLayers):
            self._layers.append(self._rawData[layer*(self._rows * self._columns):(layer+1)*(self._rows * self._columns)])
        assert(len(self._layers[0])==self._rows * self._columns)
    
    def GetLayers(self):
        return self._layers
        
    def FlattenLayers(self):
        #Bore down vertically through the layers at a pixel.  First color encountered is the color.
        stopValue = 0
        for rowIndex in range(0,self._rows):
            for columnIndex in range(0,self._columns):
                firstColoredPixel = -1
                for layerIndex in range(0,len(self._layers)):
                    layer = self._layers[layerIndex]
                    pixel = int(layer[rowIndex*self._columns + columnIndex])
                    #The first non-transparent color we find is it.
                    if (pixel == 1 or pixel == 0):
                        firstColoredPixel = pixel
                        break;
                assert(firstColoredPixel != -1)
                self._renderLayerPixels.append(firstColoredPixel)
        return self._renderLayerPixels

    def Render(self):
        #since we only have black and white, use a character for color.
        pixels = self.FlattenLayers()
        renderToText = pixels.copy()
        #Use '*' as pen, easier to read if we target white (1), so mapping '*' to white
        renderToText = list(map(lambda x: '*' if x == 1 else ' ',pixels)) 
        text = []
        #Render into lines and get list of lines
        for x in range(0, self._rows):
            string = ''
            for y in range(0, self._columns):
                string = string + renderToText[x * self._columns + y]
            text.append(string)
        for line in text:
            print(line)


