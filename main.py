import rtde_control
import rtde_receive
from tools import *
import matplotlib.pyplot as ptl
offset_from_init = [0.4, 0,0]
count_of_divide  = 100


def main():
    my_fig = ptl.figure()
    my_plot = my_fig.add_subplot(111)
    rtde_c = rtde_control.RTDEControlInterface("127.0.0.1")
    rtde_r = rtde_receive.RTDEReceiveInterface("127.0.0.1")
    rtde_c.moveJ([-0.143, -0.435, 0.20, -0.001, 3.12, 0])
    current_pos = rtde_r.getActualTCPPose()
    print("current pose", current_pos)
    point2 = array_sum(offset_from_init, current_pos)
    cord_array = divide_cord(current_pos, point2, count_of_divide)
    for i in range(count_of_divide):
        cord_array[i].append(current_pos[3])
        cord_array[i].append(current_pos[4])
        cord_array[i].append(current_pos[5])

    q_array = []
    a_1  = []
    a_2= []
    for i in range(count_of_divide):
        if i !=0: q_array.append(rtde_c.getInverseKinematics(cord_array[i], q_array[i-1])) 
        else: 
            q_array.append(rtde_c.getInverseKinematics(cord_array[i], rtde_r.getActualQ()))
        
        rtde_c.moveJ(q_array[i])
        a_1.append(rtde_r.getActualQ()[2])
        a_2.append(q_array[i][2])
        print(q_array[i])
    
    my_plot.plot(range(count_of_divide), a_1,linewidth=4.0, color = "red")
    my_plot.plot(range(count_of_divide), a_2,linewidth=2.0, color = "green")
    my_fig.savefig('{}.{}'.format("test", 'png'), fmt='png')
    

main()
