class PDController:
    """PD depth controller that remembers the previous tracking error."""

    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute_action(self, target_depth, current_depth):
        """Calculate the control action for one simulation step."""
        error = target_depth - current_depth

        proportional = self.kp * error
        derivative = self.kd * (error - self.previous_error)
        action = proportional + derivative

        self.previous_error = error
        return action

    def reset(self):
        """Clear the controller's memory before a new simulation."""
        self.previous_error = 0.0