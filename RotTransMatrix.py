import math

def matrixMult(matA : list, matB : list, result : list):
    for i in range(len(matA)):
        for j in range(len(matB[0])):
            for k in range(len(matB)):
                result[i][j] += matA[i][k] * matB[k][j]
    return result

def TwoDChangeOfReferenceFrame(angle: float, originPoint: list, translation: list) -> list:
    rotTransMat = [[math.cos(angle), -math.sin(angle), translation[0]],[math.sin(angle), math.cos(angle), translation[1]],[0,0,1]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    return matrixMult(rotTransMat, originPoint, result)


def ThreeDChangeOfReferenceFrame(angle: float, translation: list, axisOfRotation: str):
    axisOfRotation = axisOfRotation.upper()
    if axisOfRotation == "X":
        row1 = [1,0,0]
        row2 = [0,math.cos(angle), -math.sin(angle)]
        row3 = [0,math.sin(angle), math.cos(angle)]
    elif axisOfRotation == "Y":
        row1 = [math.cos(angle), 0, math.sin(angle)]
        row2 = [0, 1, 0]
        row3 = [-math.sin(angle), 0, math.cos(angle)]
    elif axisOfRotation == "Z":
        row1 = [math.cos(angle), -math.sin(angle), 0]
        row2 = [math.sin(angle), math.cos(angle), 0]
        row3 = [0,0,1]
    row1.append(translation[0])
    row2.append(translation[1])
    row3.append(translation[2])
    rotTransMat = [row1, row2, row3, [0,0,0,1]]
    return rotTransMat
    #return matrixMult(rotTransMat, originPoint, result)

if __name__ == "__main__":
    """
    Example 1: Consider a robot has a location (3,4) in a frame called map_frame
    There is another frame called odom_frame. The transformation from map_frame to odom_frame has a translation vector (3,2)
    and a rotation angle 35 degree. 
    What is the location of the robot in the odom frame? 
    """
    originPoint = [[3],[4],[1]]
    translation = [3,2]
    angle = math.radians(35)
    result = TwoDChangeOfReferenceFrame(angle, originPoint, translation)
    print("Result: {}".format(result))

    """
    Example 2: A point, a(4,3,2) is attached to a rotating frame, the frame rotates 60 degrees about the OZ axis of the reference
    frame. Find the coordinates of the point relative to the reference frame after the rotation. 
    """
    originPoint = [[4],[3],[2]]
    angle = math.radians(60)
    translation = [0,0]
    result = TwoDChangeOfReferenceFrame(angle, originPoint, translation)
    print("Result: {}".format(result))

    """
    Example 3: W1 to W2. Rotation with Respect to the Y1 axis of 90 degrees. Translation over the vector (5,3,7).
    Find the transformation matrix
    """
    angle = math.radians(90)
    translation = [5,3,7]
    result = ThreeDChangeOfReferenceFrame(angle, translation, "Y")
    print("Result of exercise three: {}".format(result))