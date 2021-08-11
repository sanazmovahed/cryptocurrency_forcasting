def readData(dataset_file_name, validation_percent, test_percent, FUTURE_PERIOD_PREDICT):
    
    # Import nesessary libraries
    import numpy as np
    import pandas as pd  
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
#     data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True) # , format='%Y/%m/%d-%H' 
    data['unix'] = pd.to_datetime(data['unix'], format='%Y/%m/%d-%H', infer_datetime_format=True) # , errors='coerce'
    
    data['Day of Week'] = data['unix'].dt.day_name()
    data['Hour of Day'] = data['unix'].dt.hour

    print(data)
    
    # Drop the columns should not include in dataset
    data = data.drop(['unix', 'date', 'tradecount', 'symbol', 'Volume BTC', 'Volume USDT', 'future'], axis=1)
    
    # Normalization stage of features
    data = normalize(data)   
   
    test_percent /= 100
    validation_percent /= 100
    times = sorted(data.index.values)
    
    # Seperate test data
    test_start_index = times[-int(test_percent * len(times))]
    test = data[(data.index >= test_start_index)]
    for i in test.values:
        x_test.append(i[:-1])
        y_test.append(i[-1])
    
    # Seperate validation data
    val_index_before_test = times[-int((validation_percent +  test_percent) * len(times)) : -int(test_percent * len(times))]
    validation = data[((data.index >= val_index_before_test[0]) & (data.index <= val_index_before_test[-1]))]
    for i in validation.values:
        x_validation.append(i[:-1])
        y_validation.append(i[-1])
    
    # Seperate train data
    training = data[(data.index < val_index_before_test[0])]
    for i in training.values:
        x_train.append(i[:-1])
        y_train.append(i[-1])
        
    return [x_train, y_train, x_validation, y_validation, x_test, y_test]

