import math

def TwoDChangeOfReferenceFrame(angle: float, originPoint: list, translation: list) -> list:
    rotTransMat = [[math.cos(angle), -math.sin(angle), translation[0]],[math.sin(angle), math.cos(angle), translation[1]],[0,0,1]]
    map_frame = originPoint#[[3],[4],[1]]
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(rotTransMat)):
        for j in range(len(map_frame[0])):
            for k in range(len(map_frame)):
                result[i][j] += rotTransMat[i][k] * map_frame[k][j]
    return result


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