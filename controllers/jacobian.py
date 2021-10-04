import numpy as np

MAX_STEP = 10

class JacobianController:
    def __init__(self, arm):
        # the controller should save a reference to the arm it's controlling
        self.arm = arm

    def control(self, target):
        if self.arm.get_num_joints() == 2:
            # if arm has 2 joints
            self.control2J2D(target)
        elif self.arm.get_num_joints() == 3:
            # if arm has 3 joints
            self.control3J2D(target)
        else:
            raise Exception("JacobianController.control(target): Can't control an arm with this amount joints.")

    def control2J2D(self, target):
        # the control method receives a target
        pass


    def control3J2D(self, target):
        # the control method receives a target
        pass
