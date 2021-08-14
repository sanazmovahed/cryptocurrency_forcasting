def readData(dataset_file_name, FUTURE_PERIOD_PREDICT):
    
    # Import nesessary libraries
    import numpy as np
    import pandas as pd  
    import time
    from classify import classify
    from normalization import normalize
    from sklearn import preprocessing  # for normalization of data
    
    
    x_train, y_train, x_validation, y_validation, x_test, y_test = ([] for i in range(6))
    
    data = pd.read_csv(dataset_file_name, delimiter=',')[1:]
    
    # Sort data in Desc order from old to new
    data = data.iloc[::-1]
    
    # Create binary targets targets
    data['future'] = data['close'].shift(-FUTURE_PERIOD_PREDICT)
    data['target'] = list(map(classify, data['close'], data['future']))
    # print(data[['close', 'future', 'target']].head(10))
    
    # Add day of week as a field
    date_time = pd.Series(data['unix'])
    temp = []
    for num in date_time:
        if len(str(num)) > 10:
            b = int(num) / 1000
        else:
            b = int(num)
        temp.append(time.ctime(b))
    data['unix'] = temp
    
    data['unix'] = pd.to_datetime(data['unix'], format='%Y/%m/%d-%H' , infer_datetime_format=True) # , errors='coerce'
    
    data['Day of Week'] = data['unix'].dt.weekday
    data['Hour of Day'] = data['unix'].dt.hour
    
    print(data, data.info())    
    
    # Drop the columns should not include in dataset
    data = data.drop(['unix', 'date', 'tradecount', 'symbol', 'Volume BTC', 'Volume USDT', 'future'], axis=1)
    
    # Normalization stage of features
    data = normalize(data)   
           
    return data

