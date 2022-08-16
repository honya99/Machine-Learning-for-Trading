import numpy as np
import random
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it

class RTLearner(object):

    def __init__(self, leaf_size = 1, verbose = False):
        self.leaf_size = leaf_size
        pass

    def author(self):  
        return 'Honya Elfayoumy'

    def add_evidence(self, data_x, data_y):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Add training data to learner  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param data_x: A set of feature values used to train the learner  		  	   		  	  			  		 			     			  	 
        :type data_x: numpy.ndarray  		  	   		  	  			  		 			     			  	 
        :param data_y: The value we are attempting to predict given the X data  		  	   		  	  			  		 			     			  	 
        :type data_y: numpy.ndarray  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        # slap on 1s column so linear regression finds a constant term  		  	   		  	  			  		 			     			  	 
        new_data_x = np.ones([data_x.shape[0], data_x.shape[1] + 1])  		  	   		  	  			  		 			     			  	 
        new_data_x[:, 0 : data_x.shape[1]] = data_x
        new_data_x[:,-1] = data_y
        self.tree = self.buildRT(new_data_x) 		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    def buildRT(self, data):
        randFeat = np.random.randit(0, data.shape[1]-1)
        splitVal = np.median(data[:, randFeat]) #Use the median to keep tree balanced

        if data.shape[0] <= self.leaf_size: #create a leaf
            return np.array([np.nan, np.mean(data[:,-1]), 1, 1], dtype=object)
        if np.unique(data[:, -1]).shape[0] == 1: #if all labels are te same
            return np.array([np.nan, data[0,-1], 1, 1], dtype = object)
        else:
            leftTree = (data[data[:,randFeat] <= splitVal]) #used to build tree
            rightTree = (data[data[:, randFeat] > splitVal]) #used to build tree
            root = np.array([[randFeat, splitVal, 1, leftTree.shape[0] + 1]], dtype = object) # left tree will begin at next row and the next row after, the right tree begins
            tree = np.append(leftTree, rightTree, axis = 0)
            return np.append(root, tree, axis = 0) 
    
    def query(self, points):
        #pred = np.zeros(points.shape[0])
        predY = []
        for i in range(0, points.shape[0]): #go through all data points
            node = 0 #start at top  of regression tree
            feat = (self.tree[node,0]) #feature
            while (feat >= 0): #if not a leaf node
                if i(feat <= self.tree[node, 1]): #if feature is less than or equal to split val
                    node = node + self.tree[node, 2] #left index
                else:
                    node = node + self.tree[node, 3] #right index
            return predY.append(self.tree[node, 1])
            


        # if data.shape[0] == 1:
        #     return np.array([-1, data[0,-1], np.nan, np.nan], dtype = object)
        
    
        