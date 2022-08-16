""""""  		  	   		  	  			  		 			     			  	 
"""Assess a betting strategy.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			     			  	 
All Rights Reserved  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			     			  	 
or edited.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			     			  	 
GT honor code violation.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Student Name: Honya Elfayoumy 		  	   		  	  			  		 			     			  	 
GT User ID: helfayoumy3 		  	   		  	  			  		 			     			  	 
GT ID: 903626029 		  	   		  	  			  		 			     			  	 
"""  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "helfayoumy3"  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def gtid():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT ID of the student  		  	   		  	  			  		 			     			  	 
    :rtype: int  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return 903626029 		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		  	  			  		 			     			  	 
    :type win_prob: float  		  	   		  	  			  		 			     			  	 
    :return: The result of the spin.  		  	   		  	  			  		 			     			  	 
    :rtype: bool  		  	   		  	  			  		 			     			  	 
    """  	  		  	  			  		 			     			  	 
    result = False  		  	   		  	  			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		  	  			  		 			     			  	 
        result = True
    # prob = np.random.random()   		  	  			  		 			     			  	 
    # result = False  		  	   		  	  			  		 			     			  	 
    # if prob <= win_prob:  		  	   		  	  			  		 			     			  	 
    #     result = True
    # print(prob, '<=', win_prob, result) 	   		  	  			  		 			     			  	 
    return result  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def test_code():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    Method to test your code  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    win_prob = 18.0/38.0 # set appropriately to the probability of a win  		  	   		  	  			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		  	  			  		 			     			  	 
    #print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  	  			  		 			     			  	 
    # add your code here to implement the experiments

    figure1 = np.zeros([0,1000])
    plt.figure(0)
    for i in range(10):
            run1 = exp1_spin(win_prob)
            plt.plot(run1, label = i)
        #   figure1 = np.append(figure1, [run1], axis = 0)
    plt.title('Experiment 1 - Figure 1')
    plt.legend(loc = "lower right")
    # plt.plot(spins,winnings)
    plt.xlabel('Number of Spins')
    plt.ylabel('Number of Wins')
    plt.xlim([0,300])
    plt.ylim([-256,100])
    plt.savefig('exp1fig1.png')
    # exp1_spin(win_prob) #run experiment 1 figure 1


    figure2_3 = np.zeros([0,1000])
    for i in range(1000):
            run2 = exp1_spin(win_prob)
          #  plt.plot(run2, label = i)
            figure2_3 = np.append(figure2_3, [run2], axis = 0)
    mean = np.mean(figure2_3, axis = 0)
    std = np.std(figure2_3, axis = 0)

    above = mean + std
    below = mean - std

    plt.figure(1)
    plt.title('Experiment 1 - Figure 2')
    plt.plot(mean, label='Mean')
    plt.plot(above, label="Mean + std")
    plt.plot(below, label="Mean - std")
    plt.legend(loc="lower right")
    plt.xlabel('Number of Spins')
    plt.ylabel('Number of Wins')
    plt.xlim([0,300])
    plt.ylim([-256,100])
    plt.savefig('exp1fig2.png')


    #figure3 = np.zeros([0,1000])
    #for i in range(1000):
            #run3 = exp1_spin(win_prob)
          #  plt.plot(run2, label = i)
            #figure3 = np.append(figure3, [run3], axis = 0)
    median = np.median(figure2_3, axis = 0)
    #std = np.std(figure3, axis = 0)

    above_2 = median + std
    below_2 = median - std

    plt.figure(2)
    plt.title('Experiment 1 - Figure 3')
    plt.plot(median, label='Median')
    plt.plot(above_2, label="Median + std")
    plt.plot(below_2, label="Median - std")
    plt.legend(loc="lower right")
    plt.xlabel('Number of Spins')
    plt.ylabel('Number of Wins')
    plt.xlim([0,300])
    plt.ylim([-256,100])
    plt.savefig('exp1fig3.png')


    # Experiment 2

    figure4_5 = np.zeros([0,1000])
    plt.figure(3)
    win = 0
    loss = 0
    for i in range(1000):
            run4_5 = exp2_spin(win_prob)
            # if run4_5[-1] == 80:
            #     win += 1
            # else:
            #     loss += 1
            figure4_5 = np.append(figure4_5, [run4_5], axis = 0)
    mean = np.mean(figure4_5, axis = 0)
    std = np.std(figure4_5, axis = 0)

    #print(win,loss)
    above_4 = mean + std
    below_4 = mean - std
    #print(mean)

    plt.title('Experiment 2 - Figure 4')
    plt.plot(mean, label='Mean')
    plt.plot(above_4, label="Mean + std")
    plt.plot(below_4, label="Mean - std")
    plt.legend(loc="lower right")
    plt.xlabel('Number of Spins')
    plt.ylabel('Number of Wins')
    plt.xlim([0,300])
    plt.ylim([-256,100])
    plt.savefig('exp2fig4.png')

    # Figure 5
    
    median = np.median(figure4_5, axis = 0)

    above_5 = median + std
    below_5 = median - std

    plt.figure(4)
    plt.title('Experiment 2 - Figure 5')
    plt.plot(median, label='Median')
    plt.plot(above_5, label="Median + std")
    plt.plot(below_5, label="Median - std")
    plt.legend(loc="lower right")
    plt.xlabel('Number of Spins')
    plt.ylabel('Number of Wins')
    plt.xlim([0,300])
    plt.ylim([-256,100])
    plt.savefig('exp2fig5.png')


# Experiment 1
# Run a simulator repeatedly with randomized inputs and assess the results in aggregate

# Run your simple simulator 10 episodes and track the winnings, starting from 0 each time.

def exp1_spin(win_prob):

    winnings = np.zeros([1000])
    episode_winnings = 0
    bet = 1
    spins = 0

    while episode_winnings < 80 and spins < 1000:
        won = get_spin_result(win_prob)
        if won:
            episode_winnings += bet 
            bet = 1 # the bet amount restarts at $1 after winning spin
        else:
            episode_winnings -= bet
            bet *= 2
    # once it hits 80, go to second while loop

        winnings[spins] = episode_winnings # spins is 0-999
        spins += 1 # keeps track of the number of spins 

    # if the target of $80 winnings is reached, stop betting, and allow the $80 value to persist from spin to spin
    while spins < 1000:
        winnings[spins] = 80 
        spins += 1 
    
    # print(winnings)
    return winnings


def exp2_spin(win_prob):

    winnings = np.zeros([1000])
    episode_winnings = 0
    bet = 1
    spins = 0
    bank_roll = 256

    while episode_winnings < 80 and spins < 1000 and bank_roll > 0:
        won = get_spin_result(win_prob)
        if won:
            episode_winnings += bet
            bank_roll += bet
            bet = 1 # the bet amount restarts at $1 after winning spin

        else:
            episode_winnings -= bet
            bank_roll -= bet
            bet *= 2

    # once it hits 80, go to second while loop

        winnings[spins] = episode_winnings # spins is 0-999
        spins += 1 # keeps track of the number of spins

        # since you can't bet more than you have
        #print(bet,">",bank_roll)
        if bet > bank_roll:
            bet = bank_roll

        # if bank_roll <= 0:
        #     break

    #print(bank_roll, episode_winnings)
    if bank_roll == 0:
    # once the player has lost their money, stop betting and fill the number -256 forward
        while spins < 1000:
            winnings[spins] = -256 
            spins += 1
    else:
        while spins < 1000:
            winnings[spins] = 80 
            spins += 1
    
    #print(winnings)

    #print(winnings)
    return winnings
  		  	   		  	  			  		 			     			  	 	  	   		  	  			  		 			     			  	 
if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    test_code()  		  	   		  	  			  		 			     			  	 

