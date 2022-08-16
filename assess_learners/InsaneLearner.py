import numpy as np
import BagLearner as bl
import LinRegLearner as lrl

class InsaneLearner(object):
    def __init__(self, verbose = False):
        self.learner = bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {"leaf_size":1}, bags = 20, boost = False, verbose = False)
    def author(self):  
        return 'Honya Elfayoumy'
    def add_evidence(self, data_x, data_y):  		  	   		  	  			  		 			     			  	 		  	   		  	  	
        for i in range(20):
            self.learner.addEvidence(data_x, data_y)		  		 			     			  	 		  	   		  	  			  		 			     			  	 
    def query(self, points):	  	   		  	  			  		 			     			  	 
        vals = []
        for learner in self.learners:
            vals.append(self.learner.query(points))
            mean = np.mean(vals, axis=0)
        return mean
  			  		 			     			  	  		  	   		  	  			  		 			     			