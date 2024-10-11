# You can import matplotlib or numpy, if needed.
# You can also import any module included in Python 3.10, for example "random".
# See https://docs.python.org/3.10/py-modindex.html for included modules.
from random import randint


class Robot:

    def __init__(self):
        # Define R- and Q-matrices here.
        self.reward_matrix = [[[-5000, -5000, -100, -50],
                              [-5000, -50, -100, -50],
                              [-5000, -100, 0, 0],
                              [-5000, -100, 0, -100],
                              [-5000, 0, 0, -50],
                              [-5000, 0, -5000, 0]],

                              [[-50, -5000, -50, -100], 
                              [-100, -50, 0, 0],
                              [-100, -50, -100, 0],
                              [0, 0, 0, -100],
                              [0, -100, 0, 0],
                              [-50, 0, -5000, -100]],

                              [[-50, -5000, 0, -100],
                              [-50, -100, 0, 0],
                              [0, 0, -100, 0],
                              [-100, 0, 0, 0],
                              [0, -100, -100, 0],
                              [0, 0, -5000, 0]],

                              [[-100, -5000, 0, -100],
                              [0, -100, 0, 0],
                              [0, 0, 0, -100],
                              [-100, 0, 0, 0],
                              [0, 0, 0, -100] ,
                              [-100, 0, -5000, -50]],

                              [[-100, -5000, 0, 500],
                              [0, -100, -100, -50],
                              [0, 0, 0, -50],
                              [0, -100, -100, -50],
                              [0, 0, 0, -50],
                              [0, -100, -5000, -50]],

                              [[-100, -5000, -50, -5000],
                              [0, 500, -50, -5000],
                              [-100, -50, -50, -5000],
                              [0, -50, -50, -5000],
                              [-100, -50, -50, -5000],
                              [0, -50, -5000, -5000]]]
        
        self.q_matrix = [[0] * 6 for _ in range(6)]

        # går til en gitt start, A4
        self.row = 0
        self.column = 3
        self.position = (self.row, self.column)

    def get_column(self):
        # Return the current column of the robot, should be in the range 0-5.
        return self.column

    def get_row(self):
        # Return the current row of the robot, should be in the range 0-5.
        return self.row

    def get_next_state_mc(self):
        # Return the next state based on Monte Carlo.
        """
        north = 0
        west = 1
        east = 2
        south = 3
        """

        direction = randint(0,3)
        if direction == 0:
            if self.row == 0:
                pass
            else: 
                self.row -= 1
        elif direction == 1:
            if self.column == 0:
                pass
            else: 
                self.column -= 1
        elif direction == 2:
            if self.column == 5:
                pass
            else:
                self.column += 1
        else:
            if self.row == 5:
                pass
            else:
                self.row += 1

        return direction
        

    def get_next_state_eg(self):
        # Return the next state based on Epsilon-greedy.
        pass

    def monte_carlo_exploration(self, trials):
        routes = []
        rewards = []
        for _ in range(trials):
            self.column = 3
            self.row = 0
            route = []
            reward = []
            done = False
            while not done:
                direction = self.get_next_state_mc()
                new_reward = self.reward_matrix[self.row][self.column][direction]
                route.append(tuple((self.row, self.column)))
                reward.append(new_reward)
                done = (self.row == 5 and self.column == 0)
            routes.append(route)
            rewards.append(sum(reward))
        maximum_reward = max(rewards)
        index = rewards.index(maximum_reward)
        return f'Highest reward: {maximum_reward}\
                Route: {routes[index]}'
        
                

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