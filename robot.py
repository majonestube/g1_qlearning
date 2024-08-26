# You can import matplotlib or numpy, if needed.
# You can also import any module included in Python 3.10, for example "random".
# See https://docs.python.org/3.10/py-modindex.html for included modules.

class Robot:

    def __init__(self):
        # Define R- and Q-matrices here.
        pass

    # Returns the current column of the robot (0-5).
    def get_x(self):
        return 3

    # Returns the current row of the robot (0-5).
    def get_y(self):
        return 0

    def get_next_state_mc(self):
        pass

    def get_next_state_eg(self): # Only implement this if using "epsilon-greedy" policy.
        pass

    def monte_carlo_exploration(self):
        pass

    def q_learning(self):
        pass
        
    def one_step_q_learning(self):
        # Get action based on policy
        # Get the next state based on the action
        # Get the reward for going to this state
        # Update the Q-matrix
        # Go to the next state
        pass
    
    def has_reached_goal(self):
        # Return 'True' if the robot is in the goal state.
        pass
        
    def reset_random(self):
        # Place the robot in a new random state.
        pass

    def greedy_path(self):
        pass

# Feel free to add additional classes / methods / functions to solve the assignment...