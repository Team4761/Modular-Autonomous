package org.robockets.stronghold.robot.modauto;

import org.robockets.stronghold.robot.Robot;

public class GetBytes {
	
	final int[] bitPins = {2, 3, 4, 5, 7, 10, 17}; 
	final int dataPin = 6;
	String binaryInput = "0";
	
	public GetBytes(){
		
	}
	
	public boolean isReady(){
		return Robot.oi.gamepad.getRawButton(dataPin);
	}
	
	public void waitUntilReady(){
		while(!isReady());
	}
	
	public void resetAll(){
		binaryInput = "0";
	}
	
	public String toBinaryString(){
		for(int i=0;i<bitPins.length;i++){
			if(Robot.oi.gamepad.getRawButton(bitPins[i])){
				binaryInput += "1";
			}else{
				binaryInput += "0";
			}
		}
		return binaryInput;
	}
	
	public int stringToDec(String binaryInput){
		return Integer.parseInt(binaryInput, 2);
	}
	
	public String decToAscii(int asciiCode){
		return Character.toString((char) asciiCode);
	}
	
}
