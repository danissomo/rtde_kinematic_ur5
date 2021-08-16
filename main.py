import rtde_control
import rtde_receive
from tools import *
from planner import *

class topicPublisher(object):
    def __init__(self, topicname):
        self.t_name = topicname
        super().__init__()

    def send(slef, message):
        print(message)
        pass
    

def main():
    offset_from_init = [0.2, 0,0, 0, 0 ,0]
    count_of_divide  = 10
    rtde_c = rtde_control.RTDEControlInterface("127.0.0.1")
    rtde_r = rtde_receive.RTDEReceiveInterface("127.0.0.1")
    rtde_c.moveJ([0, -0.55, -2.5, 0, 1.5, 0])
    current_pos = rtde_r.getActualTCPPose()
    point2 = array_sum(offset_from_init, current_pos)

    tp = trajectPlanner(rtde_r, debug=False)
    cart_a = tp.a_PointToPoint(current_pos, point2, count_of_divide)

    ik = rtde_kinematic(rtde_r, rtde_c, debug=False)
    joint_Q = ik.get_joint_pose(cart_a)
    
    for q in joint_Q:
        rtde_c.moveJ(q)
    

main()
