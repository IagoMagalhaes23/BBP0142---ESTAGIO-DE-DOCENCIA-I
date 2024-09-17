"""
    Autor: Iago Magalhães
    Descrição:
        - Cria páginas 1 e 2
        - Funcionalidade de abrir porta serial
        - Funcionalidade de fechar porta serial
        - Funcionalidade de ativar e desativar led
        - Funcionalidade de leitura da porta serial
        - Funcionalidade de navegação entre telas
"""
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.clock import Clock
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np

class Pagina1(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.txtPort.text = "COM1"
        self.ids.txtBaud.text = "9600"

class Pagina2(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cont = 0
        x = [1,2,3,4]
        y = [10,7,8,5]
        plt.plot(y,x)
        boxGraf = self.ids.boxGraf
        boxGraf.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    
    def retornar(self):
        self.manager.current = "pagina1"
    
class MyApp(MDApp):
    def build(self):
        Window.size = (300,500)
        self.title = "Supervisório - Serial"
        self.icon = "assets/img/icone.png"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Red"
        sm = MDScreenManager()
        sm.add_widget(Pagina1(name="pagina1"))
        sm.add_widget(Pagina2(name="pagina2"))
        return sm

if __name__=="__main__":
    MyApp().run()