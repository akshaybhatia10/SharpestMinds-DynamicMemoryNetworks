# SharpestMinds-DynamicMemoryNetworks

Project work for SharpestMinds application(In Progress)

### About 

Implementing Dynamic Memory Network on BabI Question Answering Dataset. 

### Install 

This project requires **Python 3.6** and the following Python libraries installed:

- [Tensorflow](http://tensorflow.org/)
- [Numpy](http://numpy.org/)
- [Keras](https://keras.io/) 

### Run

Before running the Jupyter notebook, make sure to download the dataset from [here](http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2.tar.gz) and Glove Pre-trained word embedding from [here](http://nlp.stanford.edu/data/wordvecs/glove.6B.zip). Alternatively, run the following command. This will setup all the required files in the 'data' diretory. 

```bash
python download_data.py
``` 

In a terminal or command window, navigate to the top-level project directory  (that contains this README) and run the following command:

```bash
jupyter notebook BabI\ Exploration\ and\ Simple\ Baseline.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.
