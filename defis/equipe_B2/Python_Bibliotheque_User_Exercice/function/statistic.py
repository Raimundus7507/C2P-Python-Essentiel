import statistics

def DonneesStat (data = (2, 5, 8, 6, 2, 3, 8, 6, 2, 2)):
    mode = statistics.mode(data)
    eqType = statistics.stdev(data)
    print(f'Mode : {mode}  \n Equart type : {eqType}')