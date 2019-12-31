class TextScreen:
    def __init__(self):
        self._currentLine = ""
        self._lines = []

    def AddToLine(self, val):
        if (val == 10):
            self._lines.append(self._currentLine)
            self._currentLine = ""
            return
        ch = TextScreen.GetCharFromAscii(val)
        self._currentLine = self._currentLine + ch

    def GetCharFromAscii(val):
        return chr(val)