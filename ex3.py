def quater(xcoord,ycoord):
    if xcoord > 0 and ycoord > 0:
        return 'I'
    elif xcoord < 0 and ycoord > 0:
        return 'II'
    elif xcoord < 0 and ycoord < 0:
        return 'III'
    elif xcoord > 0 and ycoord < 0:
        return 'IV'

quater(3,-4)