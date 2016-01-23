from random import random
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.image import Image

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

class MyPaintApp(App):
	
	defenses = ['Portcullis','Cheval\nde Frise','Moat','Ramparts','Drawbridge', 'Sally Port','Rock Wall', 'Rough Terrain']
	
	configmode = True
	
	b2index=0
	b3index=0
	b4index=0
	b5index=0

	
	#Puts together the window, and the widgets in it
	def build(self):
		parent = Image(source ='/home/dev2/dev/kivy/redside480.png')
   
	
		
		b1 = Button(text='Low Bar', pos=(480, 28), size=(100, 75))
		
		b2 = Button(text='B2', pos=(480, 95), size=(100, 75) )
		b2.bind(on_release=self.b2)

		b3 = Button(text='B3', pos=(480, 168), size=(100, 75)) 
		b3.bind(on_release=self.b3)
		
		b4 = Button(text='B4', pos=(480, 240), size=(100, 75))
		b4.bind(on_release=self.b4)

		b5 = Button(text='B5', pos=(480, 313), size=(100, 75)) 
		b5.bind(on_release=self.b5)
		
		b6 = Button(text='Config Mode', pos=(0,300), size=(100, 100)) 
		b6.bind(on_release=self.b6)
		
		parent.add_widget(b1)
		parent.add_widget(b2)
		parent.add_widget(b3)
		parent.add_widget(b4)
		parent.add_widget(b5)
		parent.add_widget(b6)
		return parent
		
	def b2(self, obj):
		if self.configmode == True:
			self.b2index = self.b2index + 1
			if self.b2index > 7:
				self.b2index = 0
			obj.text=self.defenses[self.b2index]
			print 'configMode Button2'
		
	def b3(self, obj):
		if self.configmode == True:
			self.b3index = self.b3index + 1
			if self.b3index > 7:
				self.b3index = 0
			obj.text=self.defenses[self.b3index]
			print 'Button3'
		
	def b4(self, obj):
		if self.configmode == True:
			self.b4index = self.b4index + 1
			if self.b4index > 7:
				self.b4index = 0
			obj.text=self.defenses[self.b4index]
			print 'Button4'
		
	def b5(self, obj):
		if self.configmode == True:
			self.b5index = self.b5index + 1
			if self.b5index > 7:
				self.b5index = 0
			obj.text=self.defenses[self.b5index]
			print 'Button5'
			
	def b6(self, obj):
		if self.configmode == True:
			self.configmode = False 
			obj.text = 'Operation\n Mode'
		else:
			self.configmode = True
			obj.text = 'ConfigMode'
		print 'Button6'

if __name__ == '__main__':
	MyPaintApp().run()

