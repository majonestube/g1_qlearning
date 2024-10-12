from robot import Robot

robot = Robot()

robot.q_learning(1000)
robot.reset()
while not robot.has_reached_goal():
  print(robot.one_step_q_learning())