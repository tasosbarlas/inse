import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior, DragBehavior
from kivy.uix.popup import Popup
from kivy.graphics import Color, Ellipse
import baseComponents
import uiComponents

class PertBoard(AnchorLayout):
	pass

class GanttBoard(AnchorLayout):
	pass

class WbtBoard(AnchorLayout):
	pass

class DataInput(Popup):
	pass

class Dummy(Ellipse):
	pass

class PertWidget(DragBehavior, Widget):
	 def __init__(self, **kwargs):
	 	super(PertWidget, self).__init__(**kwargs)
		with self.canvas:
			Color(1, 1, 0)
			d = 30.
			Ellipse(pos=(100 - d / 2, 100 - d / 2), size=(d, d))

class MainWindow(BoxLayout):
	def addPressed(self):
		print 'This is a callback, instantiating popup\n'
		

class ChartedApp(App):

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    ChartedApp().run()