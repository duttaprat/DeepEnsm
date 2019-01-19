# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:01:37 2017

@author: Rajat
"""

from __future__ import division
import warnings
import numpy as np, pandas as pd
from scipy import stats
from scipy.stats import norm

m = input("Enter size of first class")
n = input("Enter size of second class")
l7 =[]
count  = 0
listofgenes = []
for d in range(54801) : #to account for index of genes in the actual dataset
    listofgenes.append(d + 60)
with open("GDS1388.soft") as fp:
    z = 0
    p = 0
    l4 = []
    thefile7 = open('variance_of_prefiltered_genes.txt', 'w+')
    thefile8 = open('prefiltered_genes_on_the_basis_of_variance.txt', 'w+')
    for i, line in enumerate(fp):
         
         if i >= 59 and i <= 12683:
            l1 = []
            l2 = []
            l3 = []
            l6 = []
            f = 0
            v = m + n - 2 #degree of freedom
            arr = line.split("\t")
            arr = arr[2:]
            for j, item in enumerate(arr) :
                arr[j] = float(item)
                l1 = arr[:m] #class 1 stable
                l2 = arr[m:] #class 2 progressive
            l3 = arr[0:]
            
            variance1 = np.var(l1)
            variance2 = np.var(l2)
            variance = (variance1 + variance2) / 2.0
            #print("variance is") 
            #print(variance)
            l4.append(variance)
            #print(l4)
    percentile = input("Enter threshold percentile")
    y = np.percentile(l4, percentile) #THRESHOLD
    #print(y)
    #print(l4)
    l5 = [] #A vector to show whether it is accepted or not

    for i, item in enumerate(l4):
        if l4[i] <= y :
            l6.append(l4[i]) #L6[] IS TO GET THE VARIANCE OF THE GENE THAT IS ACCEPTED
            z = z + 1 #TO ACCOUNT FOR NUMBER OF GENES TO BE ACCEPTED
            l5.append(1)
        else:
            l5.append(0)
    #thefile7 = open('variance_of_prefiltered_genes.txt', 'a')
    thefile7.write("variance of filtered genes")
    thefile7.write("\n")
    thefile7.write("THRESHOLD VALUE IS")
    thefile7.write("\t")
    thefile7.write(str(y))
    thefile7.write("\n")
    thefile7.write(str(l6))
    thefile7.write("\t")
    thefile7.write("\n")
    #thefile7.close()
    #print(l6)
    #print(l5)
    print("NUMBER OF GENES WHICH ARE ACCEPTED BY THE THRESHOLD VALUE")
    print(z) # NUMBER OF GENES WHICH ARE ACCEPTED BY THE THRESHOLD VALUE
    
    
    new = ((zip(l5, listofgenes)))
    print((zip(l5, listofgenes))) 
    list_1_sorted = [x[0] for x in new]
    list_2_sorted = [x[1] for x in new]
    #thefile8 = open('prefiltered_genes_on_the_basis_of_variance.txt', 'a')
    thefile8.write("prefiltered genes on the basis of variance")
    thefile8.write("\t")
    thefile8.write("\n")
    for i in range (len(l5)):
        if l5[i] == 1:
            count = count + 1
            l7.append(list_2_sorted[i])
            with open("GDS1388.soft") as f:
                for linenum,line in enumerate (f):
                    if linenum+1==list_2_sorted[i]:
                        gene = line.rstrip()
                        print(line.rstrip())
                        thefile8.write(str(gene))
                        thefile8.write("\t")
                        thefile8.write("\n")
       

                        
    print(l7) #LIST OF INDEXES OF THE GENES WHICH ARE ACCEPTED
    thefile7.close()
    thefile8.close()
    print("Number of genes after prefiltering")
    print(count)
    
    
    ###########################################################
    


def bootstrap_resample(X):
    """Bootstrap resample an array_like
    Parameters
    ----------
    X : array_like
      data to resample
    ki : int, optional
      length of resampled array, equal to len(X) if ki==None
    Results
    -------
    returns X_resamples"""
    
    
    #if ki == None:
    ki = len(X)
        
    resample_i = np.floor(np.random.rand(ki)*len(X)).astype(int)
    X_resample = X[resample_i]
    return X_resample
    
    
def c_functions(l1, l2):
    
    m1 = np.mean(l1)
    m2 = np.mean(l2)
    sd1 = np.std(l1)
    sd2 = np.std(l2)
    warnings.simplefilter("ignore")
    parameter = ((1.0 / m) + (1.0 / n))**(1 / 2.0)
    tt = (m1 - m2) / (parameter * (((sd1 * (m - 1)) + (sd2 * (n - 1))) / v)**(1 / 2.0))
    c1 = norm.cdf(tt)
    cn = 2.0 * (1.0 - c1)
    #print("P-VALUE")
    #print(cn)   
    l3.append(cn)
    #print(l3) #each appended p-value
    
    #print(o)
    """
  
    #####thefile1 = open('testk.txt', 'a')
    thefile1.write(str(cn))
    thefile1.write("\t")
    thefile1.write("\n")
    thefile1.close()
    print "List of Stable values ::"
    print (l1)
    print "List of Progressive values ::"
    print(l2) 
    print "Mean of stable values ::"
    print(m1)
    print " Mean of Progressive values ::"
    print(m2)
    print "Standard  Deviation of Stable values:: "
    print(sd1)
    print "Standard Deviation of Progressive values::"
    print(sd2)
    print "T-score"
    print(tt)######
    """
    return l3
    
    
listofgenes1 = []    
for d in range(12368) : #to account for index of genes in the prefiltered genes
    listofgenes1.append(d + 1)
l11 = []
with open("prefiltered_genes_on_the_basis_of_variance.txt") as fp:
    thefile5 = open('test_p.txt', 'w+')
    l_average = []
    m = input("Enter size of first class")
    n = input("Enter size of second class")
    #print (l3)
    count = 0
    l4 = []
    l9 = []
    l11 = []
    for i, line in enumerate(fp):
         
         cn = 0
         
         if i >= 1 and i <= 11363:
            l1 = []
            l2 = []
            f = 0
            v = m + n - 2 #degree of freedom
            arr = line.split("\t")
            arr = arr[2:-1]
            for j, item in enumerate(arr):
                arr[j] = float(item)
            l1 = arr[:m]
            l2 = arr[m:]
            #print("before resample ::")
            #print(l1)
            #print(l2)
            l3 = []
            t = c_functions(l1, l2)
            #print("no resampling")
            #thefile = open('test.txt', 'w')
            #print(l3)
            #print(t)
            for j in range(499) :
                
                X = np.asarray(l1)
                #print(X)
                X_resample = bootstrap_resample(X)
                #print(X_resample)
                #.print(j)
                #print("resampled first class")
                l1 = X_resample.tolist()
                #print(l1)
                #print("resampled second class")
                X = np.asarray(l2)
                X_resample = bootstrap_resample(X)
                l2 = X_resample.tolist()
                #print(l2)
                merged_list = l1 + l2
                #print(merged_list)
                
                t = c_functions(l1, l2)
                #print(l3)
            #print(t)
            #print("sum")
            sum_p = sum(t)
            #print("sum")
            #print(sum_p)
            sum_p1 = sum_p / 500.0
            l_average.append(sum_p1)
            print(i)
            
            
            
    print(l_average)        
    for i, item in enumerate(l_average):
            if l_average[i] <= 0.05 :
                #print(sum_p1)
                #print("actual p-value of a gene when it is bootstrapped")
                #print(sum_p1)
                
                l9.append(1)
                t = []
                #thefile5 = open('test_p.txt', 'a')
                thefile5.write(str(sum_p1))
                thefile5.write("\t")
                thefile5.write("\n")
                #thefile5.close()
                #l4.append(t)
                #thefile.close()
                #print(sum_p1)
                count = count + 1
                #print("valuesssss offff o")
                #print(t)
                #print(count)
            else :
                l9.append(0)
         
    thefile5.close()
    new1 = ((zip(l9, listofgenes1)))
    print("zipped")
    print((zip(l9, listofgenes1))) 
    list_1_sorted1 = [x[0] for x in new1]
    list_2_sorted2 = [x[1] for x in new1]
    thefile8 = open('genes_on_the_basis_of_p-values.txt', 'w+')
    thefile8.write("genes on the basis of p-values")
    thefile8.write("\t")
    thefile8.write("\n")
    for i in range (len(l9)):
        if l9[i] == 1:
            count = count + 1
            l11.append(list_2_sorted2[i])
            with open("prefiltered_genes_on_the_basis_of_variance.txt") as f:
                for linenum,line in enumerate (f):
                    if linenum == list_2_sorted2[i]:
                        gene = line.rstrip()
                        print(line.rstrip())
                        thefile8.write(str(gene))
                        thefile8.write("\t")
                        thefile8.write("\n")
       

                        
    #print(l7) #LIST OF INDEXES OF THE GENES WHICH ARE ACCEPTED
    thefile8.close()
    #print(count)
    
    

        