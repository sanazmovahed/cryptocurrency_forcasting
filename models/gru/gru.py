def gru(x_train):
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, GRU, BatchNormalization

    model = Sequential()
    model.add(GRU(128, input_shape=(x_train.shape[1:])))
#     model.add(Dropout(0.2))
#     model.add(BatchNormalization())

#     model.add(GRU(128, 
#                     return_sequences=True,
#                     activation="tanh",
#                     recurrent_activation="sigmoid",
#                     use_bias=True,
#                     kernel_initializer="glorot_uniform",
#                     recurrent_initializer="orthogonal",
#                     bias_initializer="zeros",
#                     kernel_regularizer=None,
#                     recurrent_regularizer=None,
#                     bias_regularizer=None,
#                     activity_regularizer=None,
#                     kernel_constraint=None,
#                     recurrent_constraint=None,
#                     bias_constraint=None,
#                     dropout=0.0,
#                     recurrent_dropout=0.0,
#                     return_state=False,
#                     go_backwards=False,
#                     stateful=False,
#                     unroll=False,
#                     time_major=False,
#                     reset_after=True,))
#     model.add(Dropout(0.1))
#     model.add(BatchNormalization())

#     model.add(GRU(128, return_sequences=True,
#                     activation="tanh",
#                     recurrent_activation="sigmoid",
#                     use_bias=True,
#                     kernel_initializer="glorot_uniform",
#                     recurrent_initializer="orthogonal",
#                     bias_initializer="zeros",
#                     kernel_regularizer=None,
#                     recurrent_regularizer=None,
#                     bias_regularizer=None,
#                     activity_regularizer=None,
#                     kernel_constraint=None,
#                     recurrent_constraint=None,
#                     bias_constraint=None,
#                     dropout=0.0,
#                     recurrent_dropout=0.0,
#                     return_state=False,
#                     go_backwards=False,
#                     stateful=False,
#                     unroll=False,
#                     time_major=False,
#                     reset_after=True,))
#     model.add(Dropout(0.2))
#     model.add(BatchNormalization())

#     model.add(Dense(32, activation="relu"))
#     model.add(Dropout(0.2))

    model.add(Dense(1, activation="sigmoid"))
    
    return model

