from random import random
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.image import Image


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

class MyPaintApp(App):
	
	defenses = ('Portcullis','Cheval\nde Frise','Moat','Ramparts','Drawbridge', 'Sally Port','Rock Wall', 'Rough Terrain')
	robot = ['', 'Robot']
	loop = ['1', '2', '3']
	Pickup_Drop = ['Pick Up', 'Drop']
	configmode = True
	last_robot_button = None
	button_index=[0,0,0,0]
	position_index=[0,0,0,0,0]

	loop_button1_index=0
	pick_drop_button1_index=0

	#Puts together the window, and the widgets in it
	def build(self):
		parent = Image(source ='/home/dev2/dev/kivy/redside480.png')
		
		self.defense_button1 = Button(text='Low Bar', pos=(480, 28), size=(100, 75))
		
		self.defense_button2 = Button(text= self.defenses[0], pos=(480, 95), size=(100, 75))
		self.defense_button2.bind(on_release=self.defense_button2_callback)

		self.defense_button3 = Button(text=self.defenses[0], pos=(480, 168), size=(100, 75)) 
		self.defense_button3.bind(on_release=self.defense_button3_callback)
		
		self.defense_button4 = Button(text=self.defenses[0], pos=(480, 240), size=(100, 75))
		self.defense_button4.bind(on_release=self.defense_button4_callback)

		self.defense_button5 = Button(text=self.defenses[0], pos=(480, 313), size=(100, 75)) 
		self.defense_button5.bind(on_release=self.defense_button5_callback)
		
		self.config_button = Button(text='Config Mode', pos=(0,300), size=(100, 100)) 
		self.config_button.bind(on_release=self.config_button_callback)
		
		self.position_button1 = Button(text='', pos=(578,95), size=(100, 75)) 
		self.position_button1.bind(on_release=self.position_button1_callback)
		
		self.position_button2 = Button(text=' ', pos=(578,168), size=(100, 75)) 
		self.position_button2.bind(on_release=self.position_button2_callback)
		
		self.position_button3 = Button(text=' ', pos=(578,240), size=(100, 75)) 
		self.position_button3.bind(on_release=self.position_button3_callback)
		
		self.position_button4 = Button(text='', pos=(578,313), size=(100, 75)) 
		self.position_button4.bind(on_release=self.position_button4_callback)
		
		self.position_button5 = Button(text=' ', pos=(578,28), size=(100, 69)) 
		self.position_button5.bind(on_release=self.position_button5_callback)
		
		self.loop_button1 = Button(text= self.loop[0], pos=(750, 430), size=(50, 50))
		self.loop_button1.bind(on_release=self.loop_button1_callback)
		
		self.pick_drop_button1 = Button(text= self.Pickup_Drop[0], pos=(0, 0), size=(100, 100))
		self.pick_drop_button1.bind(on_release=self.pick_drop_button1_callback)
		
		parent.add_widget(self.defense_button1)
		parent.add_widget(self.defense_button2)
		parent.add_widget(self.defense_button3)
		parent.add_widget(self.defense_button4)
		parent.add_widget(self.defense_button5)
		parent.add_widget(self.config_button)
		parent.add_widget(self.position_button1)
		parent.add_widget(self.position_button2)
		parent.add_widget(self.position_button3)
		parent.add_widget(self.position_button4)
		parent.add_widget(self.position_button5)
		parent.add_widget(self.loop_button1)
		parent.add_widget(self.pick_drop_button1)
		return parent
			
	def defense_callback(self, obj, index):
		if self.configmode == True:
			self.button_index[index] = self.button_index[index] + 1
			if self.button_index[index] > 7:
				self.button_index[index] = 0
			obj.text=self.defenses[self.button_index[index]]

	def defense_button2_callback(self, obj):
		self.defense_callback(obj, 0)
		
	def defense_button3_callback(self, obj):
		self.defense_callback(obj, 1)
		
	def defense_button4_callback(self, obj):
		self.defense_callback(obj, 2)
		
	def defense_button5_callback(self, obj):
		self.defense_callback(obj, 3)
			
	def config_button_callback(self, obj):
		if self.configmode == True:
			self.configmode = False 
			obj.text = 'Operation\n Mode'
		else:
			self.configmode = True
			obj.text = 'ConfigMode'
		#print 'Button6'
		
	def robot_start_position_callback(self, obj, index):
		if self.configmode == True:
			self.position_index[index] = self.position_index[index] + 1
			if self.position_index[index] > 1:
				self.position_index[index] = 0
			obj.text=self.robot[self.position_index[index]]
			if self.position_index[index] == 1 and obj != self.last_robot_button:
				if self.last_robot_button is not None:
					self.last_robot_button.text = self.robot[0]
				self.set_text_index(self.last_robot_button, 0)
				self.last_robot_button = obj
			
	def position_button1_callback(self, obj):
		self.robot_start_position_callback(obj, 0) 
		
			
	def position_button2_callback(self, obj):
		self.robot_start_position_callback(obj, 1)
		
	def position_button3_callback(self, obj):
		self.robot_start_position_callback(obj, 2)
			
	def position_button4_callback(self, obj):
		self.robot_start_position_callback(obj, 3)
			
	def position_button5_callback(self, obj):
		self.robot_start_position_callback(obj, 4)

	def loop_button1_callback(self, obj):
		if self.configmode == True:
			self.loop_button1_index = self.loop_button1_index + 1
			if self.loop_button1_index > 2:
				self.loop_button1_index = 0
			obj.text=self.loop[self.loop_button1_index]
			#print 'loop_button1'
	def pick_drop_button1_callback(self, obj):
		if self.configmode == True:
			self.pick_drop_button1_index = self.pick_drop_button1_index + 1
			if self.pick_drop_button1_index > 1:
				self.pick_drop_button1_index = 0
			obj.text=self.Pickup_Drop[self.pick_drop_button1_index]
			#print 'pick_drop_button1'
			
	def set_text_index(self, obj, list_index):
		#print "checking for object"
		
		#print obj
		#print self.position_button5
		if self.position_button5 is obj:
			self.position_button5index = list_index
		if self.position_button4 is obj:
			self.position_button4index = list_index
		if self.position_button3 is obj:
			self.position_button3index = list_index
		if self.position_button2 is obj:
			self.position_button2index = list_index		
		if self.position_button1 is obj:
			self.position_button1index = list_index	
if __name__ == '__main__':
	MyPaintApp().run()
