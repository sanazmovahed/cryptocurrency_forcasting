def divide_data(data, validation_percent, test_percent):
    import numpy as np
    
    train_data = []
    validation_data = []
    test_data = []
    test_percent /= 100
    validation_percent /= 100

    times = sorted(data.index.values)
    
    # Seperate test data
    test_start_index = times[-int(test_percent * len(times))]
    test = data[(data.index >= test_start_index)]
    for i in test.values:
#         x_test.append(i[:-1])
#         y_test.append(i[-1])
        test_data.append(i)
    
    # Seperate validation data
    val_index_before_test = times[-int((validation_percent +  test_percent) * len(times)) : -int(test_percent * len(times))]
    validation = data[((data.index >= val_index_before_test[0]) & (data.index <= val_index_before_test[-1]))]
    for i in validation.values:
#         x_validation.append(i[:-1])
#         y_validation.append(i[-1])
        validation_data.append(i)
    
    # Seperate train data
    training = data[(data.index < val_index_before_test[0])]
    for i in training.values:
#         x_train.append(i[:-1])
#         y_train.append(i[-1])
        train_data.append(i)
    
#     return [x_train, y_train, x_validation, y_validation, x_test, y_test]    
    return [train_data, validation_data, test_data]

