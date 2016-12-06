from widgets import widget___button

# array of buttons with monitor loop


class ButtonGroup:

    def __init__(self):
        self.arr = list()

    def add_button(self, button):
        self.arr.append(button)

    def monitor_buttons(self):
        for button in self.arr:
            if button.isPressed():
                return button.getFunction()