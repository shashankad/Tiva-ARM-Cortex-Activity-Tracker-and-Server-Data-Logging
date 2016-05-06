import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

x= []
y=[]
z=[]
inputData = serial.Serial('com3', 115200) #Creating our serial object named inputData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
fname = 'accel.dat'
fmode = 'a'
outf = open(fname,fmode)
def makeFig(): #Create a function that makes our desired plot
 plt.ylim(140,280)                                 #Set y min and max values
 plt.title('My Live Streaming of Sensor Data')      #Plot the title
 plt.grid(True)                                  #Turn the grid on
 plt.ylabel('xAxis | yAxis | zAxis')                            #Set ylabels
 plt.plot(x, 'ro-', label='xAxis')       #plot the x
 plt.plot(y, 'b^-', label='yAxis') #plot y axis data
 plt.plot(z, 'gs-', label='zAxis') #plot z axis data
 plt.legend(loc='upper left')                  #plot the legend
    

while True: # While loop that loops forever
    while (inputData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    inputString = inputData.readline() #read the line of text from the serial port
    dataArray = inputString.split(',')   #Split it into an array called dataArray
    xValue = float( dataArray[0])            #Convert first element to floating number and put in xValue
    yValue = float( dataArray[1])            #Convert second element to floating number and put in yValue
    zValue = float( dataArray[2])            #Convert second element to floating number and put in yValue
    x.append(xValue)                     #Build our tempF array by appending temp readings
    y.append(yValue)                     #Building our pressure array by appending P readings
    z.append(zValue)                     #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        x.pop(0)                       #This allows us to just see the last 50 data points
        y.pop(0)
        z.pop(0)
    outf.write(inputString)
    outf.flush()
