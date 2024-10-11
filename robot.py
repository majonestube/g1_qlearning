# You can import matplotlib or numpy, if needed.
# You can also import any module included in Python 3.10, for example "random".
# See https://docs.python.org/3.10/py-modindex.html for included modules.
from random import randint


class Robot:

    def __init__(self):
        # Define R- and Q-matrices here.
        self.reward_matrix = [[-50, -100, -100, 0, 0, -50],
                              [-50, -50, 0, 100, 0, 0],
                              [-100, 0, 0, -100, 0, -100],
                              [-100, 0, 0, 0, 0, 0],
                              [-100, 0, -100, 0, -100, 0],
                              [500, -50, -50, -50, -50, -50]]
        self.q_matrix = [[0] * 6 for _ in range(6)]

        # går til en gitt start, A4
        self.row = 1
        self.column = 4
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
        north = 1
        west = 2
        east = 3
        south = 4
        """

        direction = randint(1,4)
        if direction == 1:
            if self.row == 1:
                pass
            else: 
                self.row -= 1
        elif direction == 2:
            if self.column == 1:
                pass
            else: 
                self.column -= 1
        elif direction == 3:
            if self.column == 6:
                pass
            else:
                self.column += 1
        else:
            if self.row == 6:
                pass
            else:
                self.row += 1

        return self.position
        

    def get_next_state_eg(self):
        # Return the next state based on Epsilon-greedy.
        pass

    def monte_carlo_exploration(self, trials):
        routes = []
        rewards = []
        for trial in range(trials):
            robot = Robot()
            route = []
            reward = []
            done = False
            while not done:
                current_position = (robot.get_row(), robot.get_column())
                print('current position: ', current_position)
                current_reward = robot.reward_matrix[robot.get_row()][robot.get_column()]
                route.append(current_position)
                reward.append(current_reward)
                current_position = robot.get_next_state_mc()
                done = current_position == (6,1)
            routes.append(route)
            rewards.append(sum(reward))
            print(routes, rewards)
        
                

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