from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Calcular(GridLayout):
    def converter(self):

        if (self.ids.entry2.text == ''):
            pass
        else:
            self.ids.lbl.text = str(float(self.ids.entry2.text)*3.78)

    def lbl(self):
        self.ids.lbl.text = 'Valor em Real'

class Conversor(App):
    def build(self):
        return Calcular()

if __name__ == '__main__':
    Conversor().run()