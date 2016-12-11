# -----------------------------------------------------------------------------
# Author: Jasmine Oliveira
# Date:   12/2016
# -----------------------------------------------------------------------------
# health_bar.py
# -----------------------------------------------------------------------------
# Designed to represent a health bar
# *** More functions to be added ***
# *** May be helpful if wanting to add health_bar image ***
# -----------------------------------------------------------------------------
#       * Public Methods:
#           init(self, max_health, current_health=None)
#           decrease_health(self, val)
#           increase_health(self,val)
#           is_dead(self, val)
# -----------------------------------------------------------------------------


class HealthBar:

    def __init__(self, max_health, current_heath=None):
        """
        Initiate the HealthBar object
        :param max_health:
        :param current_heath:
        """
        self.max_health = max_health
        self.current_health = max_health if current_heath is None else current_heath

    def decrease_health(self, val):
        """
        Decreases current health by given value.
        If the value is greater than or equal to the current
        health, sets current_health to 0
        :param val:
        :return: True: If val < current health   (is alive)
                 False: If val >= current health (is dead)
        """

        if self.current_health <= val:
            self.current_health = 0
            return False
        else:
            self.current_health -= val
            return True

    def increase_health(self, val):
        """
        Raises the current health by the given value.
        If the value is above the max_health, then
        the current health is set to the max health.
        The health will not increase if the healthbar has
        reached 0.
        :param val: Value to increase health
        :return:
        """
        if self.is_dead() is False:
            self.current_health += val
            if self.current_health > self.max_health:
                self.current_health = self.max_health

    def is_dead(self):
        return self.max_health <= 0

