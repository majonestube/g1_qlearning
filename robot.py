# You can import matplotlib or numpy, if needed.
# You can also import any module included in Python 3.10, for example "random".
# See https://docs.python.org/3.10/py-modindex.html for included modules.
import random
import time

class Robot:

    def __init__(self):
        # Define R- and Q-matrices here.
        self.reward_matrix = [[[-500, -500, -100, -50],
                              [-500, -50, -100, -50],
                              [-500, -100, 0, 0],
                              [-500, -100, 0, -100],
                              [-500, 0, 0, -50],
                              [-500, 0, -500, 0]],

                              [[-50, -500, -50, -100], 
                              [-100, -50, 0, 0],
                              [-100, -50, -100, 0],
                              [0, 0, 0, -100],
                              [0, -100, 0, 0],
                              [-50, 0, -500, -100]],

                              [[-50, -500, 0, -100],
                              [-50, -100, 0, 0],
                              [0, 0, -100, 0],
                              [-100, 0, 0, 0],
                              [0, -100, -100, 0],
                              [0, 0, -500, 0]],

                              [[-100, -500, 0, -100],
                              [0, -100, 0, 0],
                              [0, 0, 0, -100],
                              [-100, 0, 0, 0],
                              [0, 0, 0, -100] ,
                              [-100, 0, -500, -50]],

                              [[-100, -500, 0, 1500],
                              [0, -100, -100, -50],
                              [0, 0, 0, -50],
                              [0, -100, -100, -50],
                              [0, 0, 0, -50],
                              [0, -100, -500, -50]],

                              [[-100, -500, -50, -500],
                              [0, 1500, -50, -500],
                              [-100, -50, -50, -500],
                              [0, -50, -50, -500],
                              [-100, -50, -50, -500],
                              [0, -50, -500, -500]]]
        
        self.q_matrix = [[[0] * 4 for _ in range(6)] for x in range(6)]

        # går til en gitt start, A4
        # self.position = tuple((0, 3))
        self.row = 0
        self.column = 3

    def get_column(self):
        # Return the current column of the robot, should be in the range 0-5.
        return self.column

    def get_row(self):
        # Return the current row of the robot, should be in the range 0-5.
        return self.row

    def get_next_state_mc(self):
        # Return the next state based on Monte Carlo.
        direction = random.randint(0,3)

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
        

    def get_next_state_eg(self, e):
        # Return the next state based on Epsilon-greedy.
        n = random.randint(1,100)
        if n < e:
            direction = random.randint(0,3)
        else: 
            optimal_action = max(self.q_matrix[self.row][self.column])
            possible_indexes = [x for x in range(len(self.q_matrix[self.row][self.column])) if self.q_matrix[self.row][self.column][x] == optimal_action]
            direction = random.choice(possible_indexes)
        return direction 
    
    def move(self, direction):
        if direction == 0:
            if self.row == 0:
                return False
            else: 
                self.row -= 1
                return True
        elif direction == 1:
            if self.column == 0:
                return False
            else: 
                self.column -= 1
                return True
        elif direction == 2:
            if self.column == 5:
                return False
            else:
                self.column += 1
                return True
        else:
            if self.row == 5:
                return False
            else:
                self.row += 1
                return True
    

    def monte_carlo_exploration(self, trials):
        routes = []
        rewards = []
        for _ in range(trials):
            self.column = 3
            self.row = 0
            route = []
            reward = 0
            done = False
            while not done:
                direction = self.get_next_state_mc()
                new_reward = self.reward_matrix[self.row][self.column][direction]
                route.append(tuple((self.row, self.column)))
                reward += new_reward
                done = (self.row == 5 and self.column == 0)
            routes.append(route)
            rewards.append(reward)
        maximum_reward = max(rewards)
        index = rewards.index(maximum_reward)
        return f'Highest reward: {maximum_reward}\
                Route: {routes[index]}'
        
                

    def q_learning(self, epochs):
        alpha = 0.3
        gamma = 0.8
        for _ in range(epochs):
            self.reset()
            done = False
            while not done:
                current_row = self.row
                current_column = self.column
                direction = self.get_next_state_eg(50)
                current_reward = self.reward_matrix[current_row][current_column][direction]
                self.move(direction)
                q = max(self.q_matrix[self.row][self.column])
                self.q_matrix[current_row][current_column][direction] = (1 - alpha) \
                    * self.q_matrix[current_row][current_column][direction] \
                        + alpha * (current_reward + gamma * q)
                done = self.has_reached_goal()
        return self.q_matrix
        
    def one_step_q_learning(self):
        # Get action based on policy
        # Get the next state based on the action
        # Get the reward for going to this state
        # Update the Q-matrix
        # Go to the next state
        alpha = 0.3
        gamma = 0.8
        current_row = self.row
        current_column = self.column
        direction = self.get_next_state_eg(10)
        current_reward = self.reward_matrix[current_row][current_column][direction]
        self.move(direction)
        q = max(self.q_matrix[self.row][self.column])
        self.q_matrix[current_row][current_column][direction] = (1 - alpha) \
            * self.q_matrix[current_row][current_column][direction] \
                + alpha * (current_reward + gamma * q)
        return tuple((self.row, self.column))


        
    
    def has_reached_goal(self):
        # Return 'True' if the robot is in the goal state.
        return (self.row == 5 and self.column == 0)
        
    def reset(self):
        # Place the robot in a new initial state.
        self.row = 0
        self.column = 3

    def greedy_path(self):
        pass

# Feel free to add additional classes / methods / functions to solve the assignment...