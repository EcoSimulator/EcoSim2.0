from widgets import widget___button
# array of buttons with monitor loop


class ButtonGroup:
    def __init__(self):
        self.arr = list()

    def append(self, button):
        self.arr.append(button)

    def monitor(self):
        for button in self.arr:
            if button.is_pressed():
                button.activate()