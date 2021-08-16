def simpleRNN(x_train):
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, SimpleRNN, BatchNormalization
    model = Sequential()
    model.add(SimpleRNN(32))    
    model.add(Dense(2, activation="softmax"))
    return model

