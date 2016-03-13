package org.robockets.stronghold.robot.modauto;

import org.robockets.stronghold.robot.Robot;

public class GetBytes {
	
	int[] bitPins = {14, 13, 12, 10, 9, 8, 4}; 
	String binaryInput = "0";
	
	public GetBytes(){
		
	}
	
	public boolean isReady(){
		return Robot.oi.gamepad.getRawButton(11);
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
