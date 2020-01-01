class TextScreen:
    def __init__(self):
        self._currentLine = ""
        self._lines = []

    def AddLine(self, line):
        line.strip()
        if (len(line) > 0):
            self._lines.append(line)

    def AddToLine(self, val):
        if (val == 10):
            self._lines.append(self._currentLine)
            self._currentLine = ""
            return
        ch = TextScreen.GetCharFromAscii(val)
        self._currentLine = self._currentLine + ch

    def SetPoint(self,y,x,ch):
        assert(y < len(self._lines))
        line = list(self._lines[y])
        head, oldItem, tail = line[0:x],line[x],line[x+1:]
        newLine = []
        newLine.extend(head)
        newLine.append(ch)
        newLine.extend(tail)
        self._lines[y]=newLine
        return oldItem


    def GetCharFromAscii(val):
        return chr(val)