import numpy as np
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it
#import LinRegLearner as lrl

class BagLearner(object):
    def __init__(self, learner = dt, kwargs = {"leaf_size":1}, bags = 20, boost = False, verbose = False):
        self.learner = learner
        self.bags = bags
        self.kwargs = kwargs
        self.learners = []
        for i in range(self.bags):
            self.learners.append(learner(**kwargs))  
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
  		  	   		  	  			  		 			     			  	 
        for learner in self.learners: #create matrix
            dim = data_x.shape[0]
            samp = np.random.choice(dim, dim) #random sample
            learner.addEvidence(data_x[samp], data_y[samp])

    def query(self, points):
        """  		  	   		  	  			  		 			     			  	 
        Estimate a set of test points given the model we built.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		  	  			  		 			     			  	 
        :type points: numpy.ndarray  		  	   		  	  			  		 			     			  	 
        :return: The predicted result of the input data according to the trained model  		  	   		  	  			  		 			     			  	 
        :rtype: numpy.ndarray  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        vals = []
        for learner in self.learners:
            valsLearned = self.learners[learner].query(points)
            vals.append(valsLearned)
        mean = np.mean(vals, axis=0)
        return mean #mean of results
  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    print("the secret clue is 'zzyzx'")  	
