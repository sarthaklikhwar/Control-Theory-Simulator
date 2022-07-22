from cmath import sin
import math
def controller(q1, q2, w1, w2, q1_desired, q2_desired):
    '''
    input:->

    q1 is the angle of the first arm
    q2 is the angle of the second
    w1 is the angular velocity of the first arm
    w2 is the angular velocity of the second arm
    q1_desired is the desired angle of the first arm
    q2_desired is the desired angle of the second arm

    output->

    t1: The torques required for the motor 1 for the current state
    t2: The torques required for the motor 2 for the current state
    '''
    # edit the code given below
    t1 = (2*9.8*sin(q1_desired))+(9.8*sin(q1_desired+q2_desired))-(2*sin(q2_desired)*w1*w2)-(sin(q2_desired)*w2*w2)
    t2 = (9.8*sin(q1_desired+q2_desired))+(sin(q2_desired)*w1*w1)

    return t1, t2
