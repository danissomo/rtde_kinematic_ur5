import rtde_control
import rtde_receive

def array_sum(vec1, vec2):
    result = []
    for i in range(vec1.__len__()):
        result.append(vec1[i]+vec2[i])
    return result
        

def __get_cord_by_param(point1, point2, t):
    result =[]
    result.append(point1[0]+(point2[0]-point1[0])*t)
    result.append(point1[1]+(point2[1]-point1[1])*t)
    result.append(point1[2]+(point2[2]-point1[2])*t)
    return result


def divide_cord(point1, point2, n):
    result = []
    for i in range(n):
        result.append(__get_cord_by_param(point1, point2, i/(n-1)))
    return result    
    
