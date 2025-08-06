def minBordersAB(pointA:complex,pointB:complex, cityCenters:list[complex], cityRadii:list[float])-> int:
    """
    given two points and a list of cities with center points, radii
    determine minimum number of borders that must be crossed while traveling in a straight line from point to point
    points and city centers must be provided in complex numbers (e.g. 3+6j)
    """
    #slope of AB vs perpindicular from radii
    #get the perpindicular tangent? point on arc
    #what about if point a lies within the radius... perp tangent may be outside of range
    #what about points on the "line" but not "between" A and B

    def checkSide(pointA:complex, unitVector:complex, comparePoint:complex) -> bool:
        """
        returns true if a given coordinates imaginary component is greater than the imag component of
        a point on a line with given slope and y intercept , else fale
        """
        if unitVector==1j:
            return comparePoint.real>pointA.real

        slope=unitVector.imag/unitVector.real
        yInt=pointA.imag - slope * pointA.real
        return comparePoint.imag > (slope*comparePoint.real + yInt)

    def checkBounds(pointA:complex, pointB:complex, cityPoint:complex, unitVector:complex):
        """
        returns true if a city center is one dimensionally between point A and B
        ie cosine projection onto line AB is between points A and B
        """
        aDir=cityPoint-pointA
        bDir=cityPoint-pointB
        return (aDir.real*unitVector.real + aDir.imag*unitVector.imag) >=0 and (bDir.real*unitVector.real + bDir.imag*unitVector.imag) <=0

    #initialize numBorders , get unit vector for direction of AB
    numBorders=0
    unitVector=(pointB-pointA)/abs(pointB-pointA)

    #loop through city centers. if point a XOR point B lie inside a border, add a border. if both do, do not add a border, continue to next city
    for i in range(len(cityCenters)):
        if (abs(pointA-cityCenters[i])<cityRadii[i]) or (abs(pointB-cityCenters[i])<cityRadii[i]):
            if (abs(pointA-cityCenters[i])<cityRadii[i]) == (abs(pointB-cityCenters[i])<cityRadii[i]):
                continue
            numBorders+=1
            continue

        #if neither of the points are within city radius, check if city center lies between A and and B in AB dimension
        #if true, find the two points in the cities border that are perpindicular to line ab from the citycenter
        # if either of two points are on the other side of the line, line crosses the border
        #final check to also include instances where circle is tangent to line , and intersection is technically not on other side of line
        if checkBounds(pointA,pointB,cityCenters[i],unitVector):
            comparePoint1=(cityCenters[i]+unitVector*1j*cityRadii[i])
            comparePoint2=(cityCenters[i]-unitVector*1j*cityRadii[i])

            if checkSide(pointA, unitVector,comparePoint1) != checkSide(pointA,unitVector,cityCenters[i]):
                numBorders+=1
            elif checkSide(pointA,unitVector,comparePoint2) != checkSide(pointA,unitVector,cityCenters[i]):
                numBorders+=1
            elif (comparePoint1-pointA)/abs(comparePoint1-pointA) == unitVector or (comparePoint2-pointA)/abs(comparePoint2-pointA)== unitVector:
                numBorders+=1


    return numBorders
