# Tiva-ARM-Cortex-Activity-Tracker-and-Server-Data-Logging
#Author: Shashanka Doddamani
#ID    : shashankad92@gmail.com
In today’s world wearable technology is changing the life of people like never before. Range of activity trackers are available with different functionality. In this project a smart sleep alert system capable of live data streaming to a third party server has been explored. The system uses a three axis accelerometer to track the user’s activity and stream the data to the computer later to the server. Based on the previous readings of accelerometer the controller detects whether the user is idle or awake. The system will alarm the user until he/she performs a predefined hand gesture, thereby ensuring users minimum activity and conclude that he/she is awake. This device can be used while driving, working, and during the time people get sleep without their notice.
More information:= http://shashankad92.wix.com/shashanka#!tiva-arm-cortex-m4/b4wdo 
//*****************************************************************************
//
// 
// An Accelerometer is connected to ADC input as follows
//ADC                 :	AIN0 = CH0 = PE3 connected to x - axis of accelerometer
//		   				AIN1 = CH1 = PE2 connected to y - axis of accelerometer
//		   				AIN2 = CH2 = PE1 connected to z - axis of accelerometer
//LEDs    			  : LED1 = PN1
//		   				LED2 = PN0
//   	   				LED3 = PF4
//		   				LED4 = PF0
//Vibrator or Vibmotor: PN4 connected to vibmotor
//Accelerometer       : +3.3V supply & gnd
//*****************************************************************************
//Author			  : Shashanka Doddamani
//ID				  : shashankad92@gmail.com
//Cell                : +1 4697746761
//*****************************************************************************

//*****************************************************************************
//
//!
//!
//! Open a terminal with 115,200 8-N-1 for UART.
//  use python graph.py for python graph when sending x,y,z values
//  use server1.js, server2.js for ploting data in plotly server when sending only x values
//*****************************************************************************
ENJOY!
