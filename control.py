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
    a1=3000*(q1_desired-q1)-200*w1
    a2=3000*(q2_desired-q2)-200*w2
    t1 =(2*(3000*(q1_desired-q1)-200*w1))+(math.cos(q2_desired-q1_desired)*(3000*(q2_desired-q2)-200*w1))
    t2 =(math.cos(q2_desired-q1_desired))*(3000*(q1_desired-q1)-200*w2)+(3000*(q2_desired-q2)-200*w2)
    return t1, t2