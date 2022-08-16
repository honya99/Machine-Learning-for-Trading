from turtle import left, right
import numpy as np
import random
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it

class DTLearner(object):

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
  		  	   		  	  			  		 			     			  	 
        #slap on 1s column so linear regression finds a constant term  
        new_data_x = np.ones([data_x.shape[0], data_x.shape[1] + 1])  		  	   		  	  			  		 			     			  	 
        new_data_x[:, 0 : data_x.shape[1]] = data_x
        new_data_x[:,-1] = data_y
        self.tree = self.buildDT(new_data_x)
        print("Tree", self.tree)

    def correlationFeature(self, data):
        index = 0
        maxCorrel = 0
        for i in range(data.shape[1]-1):
            col= data[:,i]
            correlation = abs(np.corrcoef(data[:,i], data[:,-1])[0,1])
            if (correlation > maxCorrel):
                maxCorrel = correlation
                index = i
        
        # print(maxCorrel, "maxCorrel")
        return index	     			  	 
  		  	   		  	  			  		 			     			  	 
    def buildDT(self, data):
        #print(data)
        correlFeat = self.correlationFeature(data)
        splitVal = np.median(data[:, correlFeat]) #Use the median to keep tree balanced
        # print(len(np.unique(data[:, -1])))

        if data.shape[0] == self.leaf_size: #create a leaf
            return np.array([correlFeat, data[:,-1][0], 1, 0], dtype=object)

        if len(np.unique(data[:, -1])) == 1: #if all labels are the same
            return np.array([correlFeat, data[:,-1][0], 1, 0], dtype=object)
        
        if splitVal == np.amax(data[:, correlFeat]):
            return np.array([correlFeat, data[:,-1][0], 1, 0], dtype=object)

        if splitVal == np.amin(data[:, correlFeat]):
            return np.array([correlFeat, data[:,-1][0], 1, 0], dtype=object)

        else:
            print(data[data[:,correlFeat] <= splitVal], data[:,correlFeat])
            leftTree = self.buildDT(data[data[:,correlFeat] <= splitVal]) #used to build tree
            rightTree = self.buildDT(data[data[:,correlFeat] > splitVal]) #used to build tree
            # print("LeftTree:", leftTree)

            root = np.array([correlFeat, splitVal, 1, np.atleast_2d(leftTree).shape[0] + 1], dtype = object) # left tree will begin at next row and the next row after, the right tree begins
            # print(root)
            tree = np.vstack((leftTree, rightTree)) #https://stackoverflow.com/questions/3881453/numpy-add-row-to-array

            # print(tree)
            
            return np.vstack((root, tree)) #https://stackoverflow.com/questions/3881453/numpy-add-row-to-array
            # print(np.concatenate(root.reshape(0, -1), leftTree, rightTree, axis=1))
            # return np.concatenate(root.reshape(0, -1), leftTree, rightTree, axis=1) #https://stackoverflow.com/questions/41989950/numpy-array-concatenate-valueerror-all-the-input-arrays-must-have-same-number 
    
    def query(self, points):
        #pred = np.zeros(points.shape[0])
        predY = np.array([])
        time = 0
        #feat = []
        for i in range(0, np.size(points, 0)): #go through all data points
            node = 0 #start at top  of regression tree
            isLeaf = self.tree[node, 3] #feature
            while (isLeaf != 0): #if not a leaf node
                
                if points[i, self.tree[node, 0]] <= self.tree[node, 1]:
                    node += self.tree[node, 2]
                else:
                    node += self.tree[node, 3]
                
                isLeaf = self.tree[node, 3]
                print("node:", node, "isLeaf:", isLeaf)

                # if isLeaf <= self.tree[node, 1]: #if feature is less than or equal to split val
                #     node += self.tree[node, 2] #left index
                # else:
                #     node += self.tree[node, 3] #right index
            if predY.size == 0:
                predY = np.append(predY, self.tree[node, 1])
            else:
                predY = np.vstack((predY, self.tree[node, 1]))
        
        print("predY:", predY)
        return predY
            
        # if data.shape[0] == 1:
        #     return np.array([-1, data[0,-1], np.nan, np.nan], dtype = object)
        
    
        