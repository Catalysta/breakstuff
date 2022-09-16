import numpy as np
np.random.seed(91622)

def airplane_sim(N):
    '''
    This function simulates the famous airplane problem, where the first passenger is drunk
    and takes a random seat. Each successive passenger takes their seat if open, otherwise they
    choose from the remaining seats at random.

    The probability that the last passenger gets their own seat is always 1/2, due to the fact
    that the passengers choosing randomly showed no preference for the last passenger's seat
    over any other.
    '''
    seats = list(range(1, (N+1)))
    seat_taken = int(np.random.randint(1, len(seats) + 1))
    seats.pop(seat_taken - 1)
    # print(seats)
    for pxr in range(2,N):
        if pxr not in seats:
            seat_taken = int(np.random.randint(1, len(seats) + 1))
            seats.pop(seat_taken - 1)
        else:
            seats.pop(seats.index(pxr))
        # print(seats)
    out = N in seats
    return(out)

result = np.mean(list(map(lambda x: airplane_sim(100), range(10000))))
print(result)
