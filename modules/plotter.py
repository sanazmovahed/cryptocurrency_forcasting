def plotter(history):
    import matplotlib.pyplot as plt
    
    history_dict = history.history
    acc = history_dict['accuracy']
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    acc_values = history_dict['accuracy']
    val_acc_values = history_dict['val_accuracy']

    epochs = range(1, len(acc) + 1)
    
    fig, axs = plt.subplots(2, 2, figsize=(12,12))
    axs[0, 0].plot(epochs, loss_values, 'bo', label='Train loss')
    axs[0, 0].plot(epochs, val_loss_values, 'b', label='Val loss')
    axs[0, 0].set_title('Train/val loss')
    axs[0, 0].set_xlabel('Epochs')
    axs[0, 0].set_ylabel('Loss')
    
    axs[0, 1].plot(epochs, acc, 'bo', label='Train Acc')
    axs[0, 1].plot(epochs, val_acc_values, 'b', label='Val Acc')
    axs[0, 1].set_title('Train/val Accuracy')
    axs[0, 1].set_xlabel('Epochs')
    axs[0, 1].set_ylabel('Accuracy')
    
    plt.legend()
    plt.show()

    return True