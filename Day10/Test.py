import math

def CalculateAngle(point1, point2):
        x1,y1 = point1
        x2,y2 = point2
        if (x1 != x2):
            slope = (y2 - y1) / (x2 - x1)
            angle = math.atan(slope)
        else:
            angle = math.pi / 2   #90 degrees in radians
        angle = round(angle,6)
        vector = (x2 - x1, y2 - y1)
        direction = (1 if x2 - x1 > 0 else -1 if x2 - x1 < 0 else 0, 1 if y2 - y1 > 0 else -1 if y2 - y1 < 0 else 0)
        if (x1 != x2):
            distance = math.sqrt(vector[0]**2 + vector[1]**2)
        else:
            distance = abs(vector[1])
        distance = round(distance, 6)
        return (angle,distance,direction)

point1 = (1,1)
point2 = (2,2)
print(f"{CalculateAngle(point1, point2)}")
point1 = (4,2)
point2 = (4,5)
print(f"{CalculateAngle(point1, point2)}")
point1 = (4,5)
point2 = (6,5)
print(f"{CalculateAngle(point1, point2)}")
point2 = (1,1)
point1 = (2,2)
print(f"{CalculateAngle(point1, point2)}")
