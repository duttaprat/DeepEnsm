# DeepEnsm


## This is the readme file that contains the guidelines and information about the compilation the code of the following paper

**Paper Name:-** Ensembling of Gene Clusters utilizing Deep Learning and Protein-protein Interaction Information
* **Authors:** Pratik Dutta<sup>1</sup>, Sriparna Saha<sup>1</sup>, Sraansh Chopra<sup>1</sup> and Varnika Miglani<sup>2</sup>
* **Affiliation:** <sup>1</sup>Indian Institute of Technology Patna, India, <sup>2</sup>Samsung R&D Institute India-Noida
* **Corresponding Author:** [Pratik Dutta](http://www.iitp.ac.in/~pratik.pcs16/) (pratik.pcs16@iitp.ac.in ) 




## Prerequisities
* **[Python 2.7+](https://www.python.org/downloads/release/python-2713/)**
* **[sklearn](https://scikit-learn.org/stable/install.html)**
* **[matplotlib 2.0+](https://matplotlib.org/users/installing.html)**
* **[mpl_toolkits](https://matplotlib.org/2.0.2/mpl_toolkits/index.html)**
* **[numpy 1.10+](https://pypi.org/project/numpy/)**

# **Preprocessed_dataset**: 
This folder contains preprocessed datasets which are used as the input of the proposed MOO-based clustering algorithm.   


## MOO

This folder contains the python code of the proposed MOO-based clustering. Use `terminal`(for linux users) and goto the '1. MOO-based clustering' folder. Then complie the code by following commands

```bash
cd examples
```
Write the **_PATH DESCRIPTION_** of the `dataset` in line number **27** of the **`main.py`**


```bash
python main.py <initial_population_size> <number_of_generation>
```

**Output:** Generate a file named **`non_dominated_solutions.txt`** that contains all the cluster information.


## 2. Algorithm -1 

## NN
This folder contains `.ipynb` files for training model which are used to generate final consensus partitionings for approach 2. For better use you can use `jupyter notebook` to run the files.

**NN Model.ipynb**

## Contribution

This work currently under major revision in IEEE/ACM TCBB. For use the code or the preprocessed dataset, please open an issue first to discuss what you would like to do. Also you can contact to the corresponding author [Pratik Dutta](http://www.iitp.ac.in/~pratik.pcs16/) (pratik.pcs16@iitp.ac.in ) 
