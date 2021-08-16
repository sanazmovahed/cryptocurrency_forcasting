def lstm(x_train):
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, LSTM, BatchNormalization
    
    model = Sequential()
    model.add(LSTM(128, input_shape=(x_train.shape[1:]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.1))
    model.add(BatchNormalization())

    model.add(LSTM(128))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(32, activation="relu"))
    model.add(Dropout(0.2))

    model.add(Dense(2, activation="softmax"))

    return model

