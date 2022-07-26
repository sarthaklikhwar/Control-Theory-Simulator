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
    a1=7000*(q1_desired-q1)-200*w1
    a2=7000*(q2_desired-q2)-200*w2
    t1 = (3+2*math.cos(q2))*a1+(1+math.cos(q2)*a2+0.5*(2*math.sin(q2)*w1*w2+math.sin(q2)*w2*w2)+0.5*9.8*(2*math.sin(q1))+math.sin(q1+q2))
    t2 = (1+math.cos(q2))*a1+a2-0.5*math.sin(q2)*w1*w1+0.5*9.8*math.sin(q1+q2)
    return t1,t2