//CREATE ACCOUNT IN PLOTLY AND GET REQUIRED KEYS
var serialport = require('serialport'),
    plotly = require('plotly')('your username','your API key'),
    token = 'your token';

var portName = 'COM3';  //CHANGE TO YOUR COM PORT
var sp = new serialport.SerialPort(portName,{
    baudRate: 115200,
    dataBits: 8,
    parity: 'none',
    stopBits: 1,
    flowControl: false,
    parser: serialport.parsers.readline("\r\n")
});

// helper function to get a nicely formatted date string
function getDateString() {
    var time = new Date().getTime();
   
    var datestr = new Date(time).toISOString().replace(/T/, ' ').replace(/Z/, '');
    return datestr;
}

var initdata = [{x:[], y:[], stream:{token:token, maxpoints: 1000000}}];
var initlayout = {fileopt : "extend", filename : "ARM_project-video"};

plotly.plot(initdata, initlayout, function (err, msg) {
    if (err) return console.log(err)

    console.log(msg);
    var stream = plotly.stream(token, function (err, res) {
        console.log(err, res);
    });

    sp.on('data', 
	      function(input) 
		  {
			if(isNaN(input) || input > 512) 
			  return;

			var streamObject = JSON.stringify({ x : getDateString(), y : input });
            console.log(streamObject);
            stream.write(streamObject+'\n');
		  }
		);
});