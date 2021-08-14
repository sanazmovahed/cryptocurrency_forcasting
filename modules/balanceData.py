def balance_data(data, SEQ_LEN):
    from collections import deque
    import numpy as np
    import random
    
    # Sequencing data in the order
    sequential_data = []
    prev_days = deque(maxlen=SEQ_LEN)
    print("prev_days: {}".format(prev_days))
    
    # create an array of x and y for all sequential data
    for i in data:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == SEQ_LEN:
            sequential_data.append([np.array(prev_days), i[-1]])
            
    # shuffle the sequences        
    random.shuffle(sequential_data) 
    
    # Count the times market is bullish or bearish as signals of buy/sell
    buys = []
    sells = []
    for seq, target in sequential_data:
        if target == 0:
            sells.append([seq, target])
        elif target == 1:
            buys.append([seq, target])
    
    # Shuffle buys and sells seperately
    random.shuffle(buys)
    random.shuffle(sells)
    
    # Get the lowest count of buy or sell signals to select equal data count for two classes
    lower = min(len(buys), len(sells))
    buys = buys[:lower]
    sells = sells[:lower]
    
    # Gathering two classes samples to create all dataset
    sequential_data = buys + sells
    random.shuffle(sequential_data)
    
    x = []
    y = []
    for seq, target in sequential_data:
        x.append(seq)
        y.append(target)
        
    return np.array(x), y    
    
#     return sequential_data

