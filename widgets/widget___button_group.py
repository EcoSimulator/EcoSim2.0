from widgets import widget___button

#array of buttons with monitor loop
class Button_Group:
    arr = list()

    def __init__(self):
        arr = list()

    def addButton(self, button):
        self.arr.append(button)

    def monitorButtons(self):
        for button in self.arr:
            if button.isPressed():
                return button.getFunction()