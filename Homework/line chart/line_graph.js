var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseDate = d3.time.format("%d-%b-%y").parse;

var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var line = d3.svg.line()
    .x(function(d) { return x(d.day); })
    .y(function(d) { return y(d.temp); });

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.json("data_ready.json", function(error, json) {
  if (error) throw error;
  data = json;
  console.log(data[250].temp)

  data.forEach( function(d) {
    d.day = parseDate(d.day)
    d.users = +d.users;
  });

  x.domain(d3.extent(data, function(d) { return d.day; }));
  y.domain(d3.extent(data, function(d) { return d.temp; }));

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Temperature (C)");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);


  var selectthegraphs = $('.thegraph').not(this);     //select all the rest of the lines, except the one you are hovering on and drop their opacity
          d3.selectAll(selectthegraphs)
            .style("opacity",0.2);

});

function type(d) {
d.day = parseDate(d.day);
d.temp = +d.temp;
return d;
}

canvas.onclick = function(evt){
    var activePoints = myLineChart.getPointsAtEvent(evt);
  }





