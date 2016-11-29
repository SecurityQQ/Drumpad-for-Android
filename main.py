# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.properties import ListProperty, VariableListProperty


Window.clearcolor = (0, 0, 0, 1)

# берет значения каждой кнопки из drum.kv,
# привязывает строковое значние и подставляет его в строку имени файла
class ButtonMaker(GridLayout):

    buttons = {str(i): str(i) for i in range(1, 17)}
    my_color = ListProperty([1, 0, 0, 1])
    
    def do_press(self, num):
        filename = 'music/song' + self.buttons[num] + '.wav'
        sound = SoundLoader.load(filename)
        sound.play()

        
class MainApp(App):  
    
    def build(self):
        return ButtonMaker()


if __name__ == "__main__":
    MainApp().run()

    
