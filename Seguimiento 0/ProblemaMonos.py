def problemamonos(a_sonrie, b_sonrie):
    problema = False
    if a_sonrie == True and b_sonrie == True:
        problema = True
    elif a_sonrie != True and b_sonrie != True:
        problema = True
    return problema