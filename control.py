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
    a=math.cos(q1-q1_desired)
    b=math.cos(q1-q1_desired+q2-q2_desired)
    c=math.sin(q2-q2_desired)
    d=math.sin(q2-q2_desired)
    e=math.cos(q1-q1_desired+q2-q2_desired)
    # edit the code given below
    t1 =(-math.sin(q2_desired)*w2*w2)-2*math.sin(q2_desired)*w1*w2+math.sin(q1_desired+q2_desired)+2*9.8*math.sin(q2_desired)
    t2 =9.8*math.sin(q1_desired+q2_desired)
    ##print(a,b,c,d,e)
    return t1, t2
##g=-(math.pi/2)
##h=-(math.pi/2)
##q=(math.pi/2)
##print(controller(g,h,1,1,q,0))