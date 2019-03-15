# DeepEnsm


## This is the readme file that contains the guidelines and information about the compilation the code of the following paper

**Paper Name:-** Ensembling of Gene Clusters utilizing Deep Learning and Protein-protein Interaction Information
* **Authors:** Pratik Dutta<sup>1</sup>, Sriparna Saha, Sraansh Chopra and Varnika Miglani
* **Affiliation:** Indian Institute of Technology Patna, India
* **Corresponding Author:** [Pratik Dutta](http://www.iitp.ac.in/~pratik.pcs16/) (pratik.pcs16@iitp.ac.in ) 




## Prerequisities
* **[Python 2.7+](https://www.python.org/downloads/release/python-2713/)**
* **[sklearn](https://scikit-learn.org/stable/install.html)**
* **[matplotlib 2.0+](https://matplotlib.org/users/installing.html)**
* **[mpl_toolkits](https://matplotlib.org/2.0.2/mpl_toolkits/index.html)**
* **[numpy 1.10+](https://pypi.org/project/numpy/)**

# **Preprocessed_dataset**

This Folder contains python file for Preprocessing of datasets. 

**Need of preprocessing** : All the genes of microarray dataset, are not differentially expressed over the two sample classes. Differentially expressed (DE) genes are relevant enough for clinical purpose which are very useful for diagnosis and prognosis of a particular disease. 

For this purpose, We have filtered genes which had variances greater than 10 percentile. We have calculated the t-statistic , which compares the difference between two sample means, in relation to variation in the data.

# **NN**
This folder contains py files for training model which are used to generate final consensus partitionings.
