//Wander van de Ven


//neem de data uit Weather.html en split de strings per /n
var Weather = document.getElementById("rawdata").value;
var array = Weather.split('\n');


//maak arrays voor data en tijd stop elk data & weer punt in de array
j = 0;
var data = [];
var temp = [];
for (var i = 0; i < 365; i++) {
    var tijdelijk = array[i];
    var tijd = tijdelijk.split(",");
    data.push( new Date(tijd[0]));
    temp.push(tijd[1]/10);
    
}    


//open de eerste canvas
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");



//Transformatiefunctie naar canvas coordinaten
function createTransform(domain, range){
	// domain is a two-element array of the data bounds [domain_min, domain_max]
	// range is a two-element array of the screen bounds [range_min, range_max]
	// This gives you two equations to solve:
	// range_min = alpha * domain_min + beta
	// range_max = alpha * domain_max + beta
    // Implement your solution here:
 	var alpha = (range[1] - range[0]) / (domain[1] - domain[0]);
	var beta = range[0] - alpha * domain[0];
	
	return function(x){
		return alpha * x + beta;
	};
}

//maak transformed temperature array
transf_temp = []; 
var transformation = createTransform([-10, 40], [50 , canvas.height]);
for (var i = 0; i < temp.length; i++) {
    
    transf_temp.push(transformation(temp[i]));
}    




//maak transformed data array
var transformation_two = createTransform([data[0].getTime(), data[364].getTime()], [50 , canvas.width]);
transf_dates = []; 
for (var i = 0; i < temp.length; i++) {
    
    transf_dates.push(transformation_two(data[i].getTime()));
}    



//trek lijnen tussen de (data,weer) coordinaten
//ctx.strokeStyle = '#f00'
ctx.beginPath();
for (var i = 0; i < temp.length; i++) {
    ctx.lineTo(transf_dates[i],(canvas.height - transf_temp[i]));
    ctx.lineWidth = 0.1;    
    ctx.stroke();
    }
    

//header
ctx.font = "20px serif";
ctx.fillText("Gemiddelde temperatuur in de Bilt", 300, 50);




    
//lijn onder
ctx.beginPath();
ctx.moveTo( 50 , canvas.height - 50);
ctx.lineWidth = 2;
ctx.lineTo(canvas.width, canvas.height - 50);
ctx.stroke();


//lijn links
ctx.beginPath();
ctx.moveTo( 50 , canvas.height -50 );
ctx.lineWidth = 2;
ctx.lineTo( 50 , 0);
ctx.stroke();

//lijntjes bij de x-as
j = 50;
for( var i = 0; i < 13; i++){
    ctx.beginPath();
    ctx.moveTo( j , canvas.height - 50);
    ctx.lineWidth = 2;
    ctx.lineTo( j , canvas.height - 45);
    ctx.stroke();
    j += (canvas.width - 50)/12;
}    

//lijntjes bij de y-as
j = 50;
for( var i = 0; i < 10; i++){
    ctx.beginPath();
    ctx.moveTo( 50 , canvas.height - j);
    ctx.lineWidth = 2;
    ctx.lineTo( 45 , canvas.height - j);
    ctx.stroke();
    j += (canvas.height - 50)/10;
    
}    

//temperaturen aan de assen
temperaturen = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40];
j = 50;
for( i = 0; i < 10; i++){
    ctx.font = "10px serif";
    //var temperaturen = temperatuur.tostring();
    ctx.fillText(temperaturen[i], 25, canvas.height - j + 6);
    j += (canvas.height - 50)/10;
}

//maanden op de x-as
maanden = ["april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december", "januari", "februari", "maart"];
j = 50;
for( i = 0; i < 12; i++){
    ctx.font = "10px serif";
    //var temperaturen = temperatuur.tostring();
    ctx.fillText(maanden[i], j, canvas.height - 30);
    j += (canvas.width - 50)/12;
}

//extra titels
ctx.fillText("temp", 5, 10);
ctx.fillText("in celc.", 5, 20);
ctx.fillText("2015", 35, canvas.height - 15);
ctx.fillText("2016", 750, canvas.height - 15);


/////////////////////////////// Opdracht 2 /////////////////////////////////////



//open 2de canvas
//http://www.html5canvastutorials.com/advanced/html5-canvas-mouse-coordinates/
var canvas_sec = document.getElementById("mySecondCanvas");
var ctx_sec = canvas_sec.getContext("2d");
 	
//functie die de muispositie pakt 	
function getMousePos(canvas, evt) {
        var rect = canvas_sec.getBoundingClientRect();
        return {
          x: evt.clientX - rect.left,
          y: evt.clientY - rect.top
        };
    }    
    
 //bij muispositie trek lijn van x positie omhoog, verticaal
 //bij muispositie trek lijn van y positie horizontaal
    //http://www.html5canvastutorials.com/advanced/html5-canvas-mouse-coordinates/
    canvas_sec.addEventListener('mousemove', function(evt) {
        ctx_sec.clearRect(0 , 0, canvas.width, canvas.height);
        var mousePos = getMousePos(canvas_sec, evt);
        
        //trek lijn horizontaal
 	    ctx_sec.beginPath();
 	    //transf_temp takes the transformed temperatures
        ctx_sec.moveTo(canvas.width , canvas.height - transf_temp[Math.round(((mousePos.x - 50)/3))]);
        ctx_sec.lineWidth = 2;
        ctx_sec.lineTo(50, canvas.height - transf_temp[Math.round((mousePos.x - 50)/3)]);
        console.log(mousePos.x);
        ctx_sec.stroke();
        
        //transform x --> data coordinate round it up
        
        
        //trek lijn verticaal
        ctx_sec.beginPath();
        ctx_sec.moveTo(mousePos.x , 0);
        ctx_sec.lineWidth = 2;
        ctx_sec.lineTo(mousePos.x, canvas.height);
        ctx_sec.stroke();
        
 	    }, false);
       
        
    function removeHandler() {
    document.getElementById("myDIV").removeEventListener("mousemove", getMousePos);
}
      
        
//canvas_sec.removeEventListener("mousemove", 
    

      
      
      
      