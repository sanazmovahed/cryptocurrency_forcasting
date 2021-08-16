def rnn(x_train):
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, SimpleRNN, BatchNormalization
    
    model = Sequential()
    model.add(SimpleRNN(
        64, input_shape=(x_train.shape[1:]),
        activation='tanh',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros', 
        kernel_regularizer=None,
        recurrent_regularizer=None, 
        bias_regularizer=None, 
        activity_regularizer=None,
        kernel_constraint=None, 
        recurrent_constraint=None, 
        bias_constraint=None,
        dropout=0.0, 
        recurrent_dropout=0.0, 
        return_sequences=True, 
        return_state=False,
        go_backwards=False, 
        stateful=False, 
        unroll=False
    ))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(SimpleRNN(
        128, activation='tanh',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros', 
        kernel_regularizer=None,
        recurrent_regularizer=None, 
        bias_regularizer=None, 
        activity_regularizer=None,
        kernel_constraint=None, 
        recurrent_constraint=None, 
        bias_constraint=None,
        dropout=0.0, 
        recurrent_dropout=0.0, 
        return_sequences=True, 
        return_state=False,
        go_backwards=False, 
        stateful=False, 
        unroll=False
    ))
    model.add(Dropout(0.1))
    model.add(BatchNormalization())

    model.add(SimpleRNN(
        64,
        activation='tanh',
        use_bias=True,
        kernel_initializer='glorot_uniform',
        recurrent_initializer='orthogonal',
        bias_initializer='zeros', 
        kernel_regularizer=None,
        recurrent_regularizer=None, 
        bias_regularizer=None, 
        activity_regularizer=None,
        kernel_constraint=None, 
        recurrent_constraint=None, 
        bias_constraint=None,
        dropout=0.0, 
        recurrent_dropout=0.0, 
        return_sequences=True, 
        return_state=False,
        go_backwards=False, 
        stateful=False, 
        unroll=False
    ))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(32, activation="relu"))
    model.add(Dropout(0.2))

    model.add(Dense(2, activation="softmax"))
    
    return model
    
    

