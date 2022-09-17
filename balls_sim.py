import numpy as np
import random

B = 18
W = 9
N = 1000

def ball_sim(B, W):
    '''
    Urn problem where remove two balls, if color is the same, add a black ball, else add a white ball.

    The thing to notice about is that the white balls can only decrease by two at a time, while black
    balls can increase or decrease by increments of 1.

    We seek the probability that the last ball in the urn is white.

    :param B: Number of Black Balls
    :param W: Number of White Balls
    :param N: Number of trials
    :return: Probability last ball is White
    '''

    balls = list(np.repeat(['B'], B)) + list(np.repeat(['W'], W))

    while len(balls) > 1:
        print(balls)
        random.shuffle(balls)
        pick = balls[:2]
        balls = balls[2:]

        if pick[0] == pick [1]:
            balls += ['B']
        else:
            balls += ['W']

    print(balls)
    out = balls[0] == 'W'
    return out

result = np.mean(list(map(lambda x: ball_sim(B, W), range(N))))
print(result)


