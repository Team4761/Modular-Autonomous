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
	robot = ['', 'Robot']
	configmode = True
	lastrobotbutton = None
	
	b2index=0
	b3index=0
	b4index=0
	b5index=0
	b7index=0
	b8index=0
	b9index=0
	b10index=0
	b11index=0
	
	b1 = None
	b2 = None
	b3 = None
	b4 = None
	b5 = None
	b6 = None
	b7 = None
	b8 = None
	b9 = None
	b10 = None
	b11 = None
	
	#Puts together the window, and the widgets in it
	def build(self):
		parent = Image(source ='/home/dev2/dev/kivy/redside480.png')
		
		self.b1 = Button(text='Low Bar', pos=(480, 28), size=(100, 75))
		
		self.b2 = Button(text='B2', pos=(480, 95), size=(100, 75) )
		self.b2.bind(on_release=self.b2_callback)

		self.b3 = Button(text='B3', pos=(480, 168), size=(100, 75)) 
		self.b3.bind(on_release=self.b3_callback)
		
		self.b4 = Button(text='B4', pos=(480, 240), size=(100, 75))
		self.b4.bind(on_release=self.b4_callback)

		self.b5 = Button(text='B5', pos=(480, 313), size=(100, 75)) 
		self.b5.bind(on_release=self.b5_callback)
		
		self.b6 = Button(text='Config Mode', pos=(0,300), size=(100, 100)) 
		self.b6.bind(on_release=self.b6_callback)
		
		self.b7 = Button(text='', pos=(578,95), size=(100, 75)) 
		self.b7.bind(on_release=self.b7_callback)
		
		self.b8 = Button(text=' ', pos=(578,168), size=(100, 75)) 
		self.b8.bind(on_release=self.b8_callback)
		
		self.b9 = Button(text=' ', pos=(578,240), size=(100, 75)) 
		self.b9.bind(on_release=self.b9_callback)
		
		self.b10 = Button(text='', pos=(578,313), size=(100, 75)) 
		self.b10.bind(on_release=self.b10_callback)
		
		self.b11 = Button(text=' ', pos=(578,28), size=(100, 69)) 
		self.b11.bind(on_release=self.b11_callback)
		
		parent.add_widget(self.b1)
		parent.add_widget(self.b2)
		parent.add_widget(self.b3)
		parent.add_widget(self.b4)
		parent.add_widget(self.b5)
		parent.add_widget(self.b6)
		parent.add_widget(self.b7)
		parent.add_widget(self.b8)
		parent.add_widget(self.b9)
		parent.add_widget(self.b10)
		parent.add_widget(self.b11)
		return parent
		
	def b2_callback(self, obj):
		if self.configmode == True:
			self.b2index = self.b2index + 1
			if self.b2index > 7:
				self.b2index = 0
			obj.text=self.defenses[self.b2index]
			print 'configMode Button2'
		
	def b3_callback(self, obj):
		if self.configmode == True:
			self.b3index = self.b3index + 1
			if self.b3index > 7:
				self.b3index = 0
			obj.text=self.defenses[self.b3index]
			print 'Button3'
		
	def b4_callback(self, obj):
		if self.configmode == True:
			self.b4index = self.b4index + 1
			if self.b4index > 7:
				self.b4index = 0
			obj.text=self.defenses[self.b4index]
			print 'Button4'
		
	def b5_callback(self, obj):
		if self.configmode == True:
			self.b5index = self.b5index + 1
			if self.b5index > 7:
				self.b5index = 0
			obj.text=self.defenses[self.b5index]
			print 'Button5'
			
	def b6_callback(self, obj):
		if self.configmode == True:
			self.configmode = False 
			obj.text = 'Operation\n Mode'
		else:
			self.configmode = True
			obj.text = 'ConfigMode'
		print 'Button6'
		
	def b7_callback(self, obj):
		if self.configmode == True:
			self.b7index = self.b7index + 1
			if self.b7index > 1:
				self.b7index = 0
			obj.text=self.robot[self.b7index]
			if self.b7index == 1 and obj != self.lastrobotbutton:
				if self.lastrobotbutton is not None:
					self.lastrobotbutton.text = self.robot[0]
				self.set_text_index(self.lastrobotbutton, 0)
				self.lastrobotbutton = obj
		print '7'
			
	def b8_callback(self, obj):
		if self.configmode == True:
			self.b8index = self.b8index + 1
			if self.b8index > 1:
				self.b8index = 0
			obj.text=self.robot[self.b8index]
			if self.b8index == 1 and obj != self.lastrobotbutton:
				if self.lastrobotbutton is not None:
					self.lastrobotbutton.text = self.robot[0]
				self.set_text_index(self.lastrobotbutton, 0)
				self.lastrobotbutton = obj
		print '8'
		
	def b9_callback(self, obj):
		if self.configmode == True:
			self.b9index = self.b9index + 1
			if self.b9index > 1:
				self.b9index = 0
			obj.text=self.robot[self.b9index]
			if self.b9index == 1 and obj != self.lastrobotbutton:
				if self.lastrobotbutton is not None:
					self.set_text_index(self.lastrobotbutton, 0)
				self.lastrobotbutton.text = self.robot[0]
				self.lastrobotbutton = obj
		print '9'
			
	def b10_callback(self, obj):
		if self.configmode == True:
			self.b10index = self.b10index + 1
			if self.b10index > 1:
				self.b10index = 0				
			obj.text=self.robot[self.b10index]
			if self.b10index == 1 and obj != self.lastrobotbutton:
				if self.lastrobotbutton is not None:
					self.lastrobotbutton.text = self.robot[0]
				self.set_text_index(self.lastrobotbutton, 0)
				self.lastrobotbutton = obj
		print '10'
			
	def b11_callback(self, obj):
		if self.configmode == True:
			self.b11index = self.b11index + 1
			if self.b11index > 1:
				self.b11index = 0
			obj.text=self.robot[self.b11index]
			if self.b11index == 1 and obj != self.lastrobotbutton:
				if self.lastrobotbutton is not None:
					self.lastrobotbutton.text = self.robot[0]
				self.set_text_index(self.lastrobotbutton, 0)
				self.lastrobotbutton = obj
		print '11'
			
	def set_text_index(self, obj, list_index):
		print "checking for object"
		print obj
		print self.b11
		if self.b11 is obj:
			self.b11index = list_index
		if self.b10 is obj:
			self.b10index = list_index
		if self.b9 is obj:
			self.b9index = list_index
		if self.b8 is obj:
			self.b8index = list_index		
		if self.b7 is obj:
			self.b7index = list_index	
if __name__ == '__main__':
	MyPaintApp().run()
