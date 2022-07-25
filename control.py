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
    t1=2*(40*(q1_desired-q1)-(13*w1))+math.cos(q1_desired-q2_desired)*(40*(q2_desired-q2)-(11*w2))
    t2=math.cos(q1_desired-q2_desired)*(40*(q1_desired-q1)-(13*w1))+(40*(q2_desired-q2))-11*w2
    return t1, t2
g=-(math.pi/2)
h=-(math.pi/2)
q=(math.pi/2)
print(controller(g,h,1,1,q,0))