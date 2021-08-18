def plotter(history):
    import matplotlib.pyplot as plt
    
    history_dict = history.history
    acc = history_dict['accuracy']
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    acc_values = history_dict['accuracy']
    val_acc_values = history_dict['val_accuracy']

    epochs = range(1, len(acc) + 1)
    
    plt.subplots(figsize=(15, 7))
    plt.plot(epochs, loss_values, label='Loss')
    plt.plot(epochs, val_loss_values, 'r', label='Validation Loss')
    plt.legend()
    plt.show()

    plt.subplots(figsize=(15, 7))
    plt.plot(epochs,acc_values, label='Accuracu')
    plt.plot(epochs, val_acc_values, 'r', label='Validation Accuracy')
    plt.legend()

    return True