from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.image import Image
import joystick_protocol

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

class MyPaintApp(App):
	
	defenses = ('Portcullis','Cheval\nde Frise','Moat','Ramparts','Drawbridge', 'Sally Port','Rock Wall', 'Rough Terrain')
	abvr_defenses = ['po', 'fr', 'mo', 'ra', 'br','sa', 'rk', 'ro'] 
	robot = ['', 'Robot']
	robot_return = ['', 'Return']
	loop = ['1', '2', '3']
	Pickup_Drop = ['Pick Up', 'Drop']
	shot_index = ['Right', 'Middle', 'Left']
	configmode = True
	last_robot_button = None
	last_robot_button2 = None 
	button_index=[0,0,0,0]
	position_index = [0,0,0,0,0]
	position_index2 = [0,0,0,0,0]
	high_low_index = ['High', 'Low']
	spy_index=['Spy\n Position\n on','Spy\n Position\n off']
	return_index=['Return On', 'Return Off']
	send_list=['lb', '', '', '', '','','']
	
	high_low_buttonindex=0
	loop_button1_index=0
	pick_drop_button1_index=0
	shot_Button_index=0
	return_button_index=0
	spy_button_index=0
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
		
		self.send_button1 = Button(text='Send', pos=(0, 400), size=(100, 100)) 
		self.send_button1.bind(on_release=self.send_button1_callback)
		
		self.spy_position = Button(text='Spy Position', pos=(0, 100), size=(100, 100)) 
		self.spy_position.bind(on_release=self.spy_position_callback)
		
		self.shot_button = Button(text= self.shot_index[0], pos=(100, 200), size=(100, 100)) 
		self.shot_button.bind(on_release=self.shot_button_callback)
		
		self.shot_height_button = Button(text= self.high_low_index[0], pos=(200, 300), size=(100, 100)) 
		self.shot_height_button.bind(on_release=self.height_button_callback)
		
		self.return_button1 = Button(text= '', pos=(380, 28), size=(102, 75)) 
		self.return_button1.bind(on_release=self.return_button1_callback)
		
		self.return_button2 = Button(text= '', pos=(380, 95), size=(102, 75)) 
		self.return_button2.bind(on_release=self.return_button2_callback)
		
		self.return_button3 = Button(text= '', pos=(380, 168), size=(102, 75)) 
		self.return_button3.bind(on_release=self.return_button3_callback)
		
		self.return_button4 = Button(text= '', pos=(380, 240), size=(102, 75)) 
		self.return_button4.bind(on_release=self.return_button4_callback)
		
		self.return_button5 = Button(text= '', pos=(380, 313), size=(102, 75)) 
		self.return_button5.bind(on_release=self.return_button5_callback)
		
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
		parent.add_widget(self.send_button1)
		parent.add_widget(self.spy_position)
		parent.add_widget(self.shot_button)
		parent.add_widget(self.shot_height_button)
		parent.add_widget(self.return_button1)
		parent.add_widget(self.return_button2)
		parent.add_widget(self.return_button3)
		parent.add_widget(self.return_button4)
		parent.add_widget(self.return_button5)
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
	def pick_drop_button1_callback(self, obj):
		if self.configmode == True:
			self.pick_drop_button1_index = self.pick_drop_button1_index + 1
			if self.pick_drop_button1_index > 1:
				self.pick_drop_button1_index = 0
			obj.text=self.Pickup_Drop[self.pick_drop_button1_index]
			
	def spy_position_callback(self, obj):
		if self.configmode == True:
			self.spy_button_index = self.spy_button_index + 1
			if self.spy_button_index > 1:
				self.spy_button_index = 0
			obj.text=self.spy_index[self.spy_button_index]
			
	def shot_button_callback(self, obj):
		if self.configmode == True:
			self.shot_Button_index = self.shot_Button_index + 1
			if self.shot_Button_index > 2:
				self.shot_Button_index = 0
			obj.text=self.shot_index[self.shot_Button_index]
			
	def height_button_callback(self, obj):
		if self.configmode == True:
			self.high_low_buttonindex = self.high_low_buttonindex + 1
			if self.high_low_buttonindex > 1:
				self.high_low_buttonindex = 0
			obj.text=self.high_low_index[self.high_low_buttonindex]
			
	def send_button1_callback(self, obj):
		
		if self.configmode == True:
			abvr = self.abvr_defenses[self.button_index[3]]
			print abvr
			for c in list (abvr):
				joystick_protocol.send(c)
			abvr = self.abvr_defenses[self.button_index[2]]
			print abvr
			for c in list (abvr):
				joystick_protocol.send(c)
			abvr = self.abvr_defenses[self.button_index[1]]
			print abvr
			for c in list (abvr):
				joystick_protocol.send(c)
			abvr = self.abvr_defenses[self.button_index[0]]
			print abvr
			for c in list (abvr):
				joystick_protocol.send(c) 
			

			if self.position_index[0] == 1:
				joystick_protocol.send('r')
				joystick_protocol.send('1')
				joystick_protocol.send('0')
			if self.position_index[1] == 1:
				joystick_protocol.send('r')
				joystick_protocol.send('2')
				joystick_protocol.send('0')
			if self.position_index[2] == 1:
				joystick_protocol.send('r')
				joystick_protocol.send('3')
				joystick_protocol.send('0')
			if self.position_index[3] == 1:
				joystick_protocol.send('r')
				joystick_protocol.send('4')
				joystick_protocol.send('0')
			if self.position_index[4] == 1:
				joystick_protocol.send('r')
				joystick_protocol.send('5')
				joystick_protocol.send('0') 
			if self.position_index2[0] == 1:
				joystick_protocol.send('t')
				joystick_protocol.send('1')
				joystick_protocol.send('0')
			if self.position_index2[1] == 1:
				joystick_protocol.send('t')
				joystick_protocol.send('2')
				joystick_protocol.send('0')
			if self.position_index2[2] == 1:
				joystick_protocol.send('t')
				joystick_protocol.send('3')
				joystick_protocol.send('0')
			if self.position_index2[3] == 1:
				joystick_protocol.send('t')
				joystick_protocol.send('4')
				joystick_protocol.send('0')
			if self.position_index[4] == 1:
				joystick_protocol.send('t')
				joystick_protocol.send('5')
				joystick_protocol.send('0')
	def robot_start_position_callback2(self, obj, index):
		if self.configmode == True:
			self.position_index2[index] = self.position_index2[index] + 1
			if self.position_index2[index] > 1:
				self.position_index2[index] = 0
			obj.text=self.robot_return[self.position_index2[index]]
			if self.position_index2[index] == 1 and obj != self.last_robot_button2:
				if self.last_robot_button2 is not None:
					self.last_robot_button2.text = self.robot_return[0]
				self.set_text_index(self.last_robot_button2, 0)
				self.last_robot_button2 = obj
	def return_button1_callback(self, obj,):
		self.robot_start_position_callback2(obj, 0) 
	def return_button2_callback(self, obj):
		self.robot_start_position_callback2(obj, 1) 
	def return_button3_callback(self, obj):
		self.robot_start_position_callback2(obj, 2) 
	def return_button4_callback(self, obj):
		self.robot_start_position_callback2(obj, 3) 
	def return_button5_callback(self, obj):
		self.robot_start_position_callback2(obj, 4) 
			
	def set_text_index(self, obj, list_index):
		if self.position_button5 is obj:
			self.position_index[4] = list_index
		if self.position_button4 is obj:
			self.position_index[3] = list_index
		if self.position_button3 is obj:
			self.position_index[2] = list_index
		if self.position_button2 is obj:
			self.position_index[1] = list_index		
		if self.position_button1 is obj:
			self.position_index[0] = list_index			
if __name__ == '__main__':
	MyPaintApp().run()
