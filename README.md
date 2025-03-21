# Handwritten-English-Word-Recognition


The implementation consists of 4 modules: 
1. SamplePreprocessor.py: It train the images from the IAM dataset for neural network.
2. DataLoader.py: DataLoader module reads the sample of image, place them into group and offers an iterator interface to travel through the image. 
3. Model.py: Model module creates the implementation for CNN, RNN and CTC as described above, also provide GUI, manages the Tensorflow and provides an interface for training and inference.
4. Main.py: Main module implements the GUI which makes it easy for user to work with the software and also puts all the modules that are created above together for the recognition.
