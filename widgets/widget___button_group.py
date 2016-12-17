from widgets import widget___button
# array of buttons with monitor loop


class ButtonGroup:
    def __init__(self):
        self.arr = list()

    def append(self, button):
        self.arr.append(button)

    def monitor(self):
        for button in self.arr:
            button.monitor()

    # Only for use with buttons that have an active/deactivated state.
    # At the moment, that just means SetupButtons.
    def deactivate_buttons(self):
        for button in self.arr:
            button.deactivate()
