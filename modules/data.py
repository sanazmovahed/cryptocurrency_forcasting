def readData(dataSetFileName, validationPercent, testPercent):

    import pandas as pd   
    data = pd.read_csv(dataSetFileName, delimiter=',')[1:]
    
    # Sort data in Desc order from old to new
    data = data.iloc[::-1]
    testPercent /= 100
    validationPercent /= 100
    times = sorted(data.index.values)
    print(len(times))
    test_percent = times[-int(testPercent * len(times))]
    test = data[(data.index >= test_percent)]
    
    val_percent_before_test = times[-int((validationPercent +  testPercent) * len(times)) : -int(testPercent * len(times))]
    validation = data[((data.index >= val_percent_before_test[0]) & (data.index <= val_percent_before_test[-1]))]
    
    training = data[(data.index <= val_percent_before_test[0])]
    
    
    return [training, validation, test]

