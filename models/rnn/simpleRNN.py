def simpleRNN(x_train):
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, SimpleRNN, BatchNormalization
    model = Sequential()
    model.add(SimpleRNN(128, input_shape=(x_train.shape[1:]), return_sequences=True))   
    
    model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(SimpleRNN(32))   

    model.add(Dense(1, activation="sigmoid"))
    return model

