class trajectPlanner(object):
    def __init__(self, rtde_r, debug = False):
        self.rtde_r = rtde_r
        self.debug = debug
        if self.debug:
            print(trajectPlanner)
            print(self.rtde_r)
            print()
        super().__init__()


    def a_PointToPoint(self, point1,  point2, point_count):
        if len(point1) != len(point2):
            print("Error: different point length")
            return
        if point_count <= 0:
            print("Error: point count < 0")
        result = []
        for i in range(point_count):
            result.append(self.__param_line(point1, point2, i/(point_count-1)))

        if self.debug:
            print(self.a_PointToPoint)
            print(point1)
            print(point2)
            print(point_count)
            print()

        return result


    def a_CurPoseToPoint(self, point2, point_count):
        result = []
        cur_pos = self.rtde_r.getActualTCPPose()
        for i in range(point_count):
            result.append(self.__param_line(cur_pos, point2, i/(point_count-1)))
        
        if self.debug:
            print(self.a_PointToPoint)
            print(point2)
            print(point_count)
            print(result)
            print()

        return result


    def __param_line(self, point1, point2, t):
        result = []
        for i in range(len(point1)):
            result.append(point1[i]+(point2[i]-point1[i])*t)

        if self.debug:
            print(self.__param_line)
            print(point1)
            print(point2)
            print(t)
            print(result)
            print()
        return result

class rtde_kinematic:
    def __init__(self, rtde_r, rtde_c, debug = False):
        self.rtde_c = rtde_c
        self.rtde_r = rtde_r
        self.debug = debug


    def get_joint_pose(self, cart):
        result = []
        if len(cart) == 0: 
            print("Error: cart has zero lenth")
            return

        result.append(self.rtde_c.getInverseKinematics(cart[0], cart[0]))
        for i in range(1,len(cart)):
            q =self.rtde_c.getInverseKinematics(cart[i], cart[i-1])
            result.append(q)

        if self.debug:
            print(self.get_joint_pose)
            print(cart)
            print(result)
        return result
        
    