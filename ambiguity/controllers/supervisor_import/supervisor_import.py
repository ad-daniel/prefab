"""my_controller2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
rootNode = robot.getRoot()  # get root of the scene tree
rootChildrenField = rootNode.getField('children')

# Main loop:
# - perform simulation steps until Webots is stopping the controller
i = 0
while robot.step(timestep) != -1:
    #if i == 2:
    #    rootChildrenField.importMFNodeFromString(-1, 'DEF AA Group { children [ Nao{} ] }')
    #if i == 5:
    #    node = robot.getFromDef('AA')
    #    node.remove();
    #if i == 10:    
    #    rootChildrenField.importMFNodeFromString(-1, 'Nao{ translation -1 0 0 }')    

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    if i == 2:
        rootChildrenField.importMFNodeFromString(-1, 'Ball{ translation 0 0 .1}')

    i += 1

# Enter here exit cleanup code.
