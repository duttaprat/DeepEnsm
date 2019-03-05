1. preprocessed_BCLL.txt is the dataset derived from Multi Objective Optimization. It consists of 4636 labeled genes (128 classes - labeled 0 to 127) and 19 unlabeled gene expressions that could not be assigned to any class.

2. labeled_file.txt and unlabeled_file.txt is just a partitioning of the preprocessed_BCLL.txt dataset into labeled and unlabeled gene expression data.

3. The "NN Model.ipynb" is a jupyter notebook which is used to train a model on the labeled gene expressions. The neural network used consists of 2 hidden layers. After each layer, a dropout (40% of nodes are zeroed out) and non-linear activation ReLU is applied to the outputs. At the last layer, a softmax function is used to classify the input into 128 classes. A validation set is used by splitting the labeled dataset into a training dataset and validation dataset (split ratio is 0.2-0.4). An Adam optimizer is used with a learning rate varying from 0.001 to 0.1. After training the model, the unlabeled dataset is fed into the neural network to generate class probabilities and thus label the unlabeled genes.

4. The "CNN Model.ipynb" is a jupyter notebook which is used to train a model on the labeled gene expressions. On the input layer, a convolutional layer is applied. The output from convolutional layer is pooled. At this point, there are multiple output channels and they need to be aggregated into a single channel. This is basically converting a 3D array into a 2D array by flattening across the 3rd dimension. After flattening, the output is passed through a hidden layer, after which a dropout and non-linear activation ReLU is applied. Finally, a softmax function is used to classify the input into 128 classes with different probabilities. A validation set is used by splitting the labeled dataset into a training and validation set (split ratio varies from 0.2-0.4). An adam optimizer is used with a learning rate varying from 0.001 to 0.1. After training, the unlabeled dataset is fed into the neural network to generate class probabilities and label the unlabeled genes.

5. The "LSTM.ipynb" is a jupyter notebook which trains a Recurrent Neural Network on the labeled gene expressions.

6. The "Label Script.ipynb" is used to combine the originally labeled gene expressions and model labeled gene expressions into 1 file for further metric evaluations. 

7. The "BHI_labels_CNN.txt" and "BHI_labels_NN_2Hidden.txt" are the labels assigned to the unlabeled gene expressions by the trained models plus the originally labeled gene expression profiles. The "trained_model_...." files are the weights and bias matrices that are obtained after training the above models.

