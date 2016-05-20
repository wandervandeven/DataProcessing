var margin = {top: 10, right: 10, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.in_2003 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.out_2003 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.in_2006 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.out_2006 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.in_2009 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.out_2009 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.in_2012 + "</span>";
    return "<strong>2013 in:</strong> <span style='color:red'>" + d.out_2012 + "</span>";
  })

  var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);


var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data; // a global

d3.json("students_ready.json", function(error, json) {
  if (error) return console.warn(error);
  data = json;

  full_data = []

  for (i = 0; i < data.length; i++)
      { 
        //ga door de lijst van alle landen (met countrycodes)
        for (j = 0; j < country_codes.length; j++)
        { 
          //als landnamen overeenkomen  
          if (data[i].country === country_codes[j][2])
          {
            //neem de kleur
            year_2003[country_codes[j][1]] = {in_2003: data[i].in_2003, out_2003: data[i].out_2003};

            year_2006[country_codes[j][1]] = {in_2006: data[i].in_2006, out_2006: data[i].out_2006};

            year_2009[country_codes[j][1]] = {in_2009: data[i].in_2009, out_2009: data[i].out_2009};

            year_2012[country_codes[j][1]] = {in_2012: data[i].in_2012, out_2012: data[i].out_2012};

          }
        }
      }

    full_data = year_2003.push(year_2006)
    full_data = full_data.push(year_2009)
    full_data = full_data.push(year_2012)

  x.domain(data.map(function(d) { return 8; }));
  y.domain([0, d3.max(data, function(d) { return d.getElementById().in_or_out;})]);

  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Temperatuur");

  chart.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", 2003, 2003, 2006, 2006, 2009, 2009, 2012, 2012)
      .attr("y", function(d) { return y(d.getElementById().in_or_out); })
      .attr("height", function(d) { return height - y(d.getElementById().in_or_out); })
      .attr("width", x.rangeBand())
      .attr()
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)
});

function type(d) {
  d.temp = +d.temp; // coerce to number
  return d;
}

</script>





