"""PROBLEM NUMBER: 1232- Check If It Is a Straight Line """

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

#Solution

def checkStraightLine(coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        #(Y2-Y1)/(X2-X1)=(Y3-Y1)/(X3-X1)
        #(Y2-Y1)*(X3-X1)=(Y3-Y1)*(X2-X1)
        
        for i in coordinates[1:-1]:
            if (i[1]-coordinates[0][1])*(coordinates[0][0]-coordinates[-1][0])!=(i[0]-coordinates[0][0])*(coordinates[0][1]-coordinates[-1][1]):
                return False
        return True
        
#checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
#checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]])


