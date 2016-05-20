//Wander van de Ven
//10470476

//variable of all country codes
var country_codes = [
      ["af", "AFG", "Afghanistan"],
      ["ax", "ALA", "Åland Islands"],
      ["al", "ALB", "Albania"],
      ["dz", "DZA", "Algeria"],
      ["as", "ASM", "American Samoa"],
      ["ad", "AND", "Andorra"],
      ["ao", "AGO", "Angola"],
      ["ai", "AIA", "Anguilla"],
      ["aq", "ATA", "Antarctica"],
      ["ag", "ATG", "Antigua and Barbuda"],
      ["ar", "ARG", "Argentina"],
      ["am", "ARM", "Armenia"],
      ["aw", "ABW", "Aruba"],
      ["au", "AUS", "Australia"],
      ["at", "AUT", "Austria"],
      ["az", "AZE", "Azerbaijan"],
      ["bs", "BHS", "Bahamas"],
      ["bh", "BHR", "Bahrain"],
      ["bd", "BGD", "Bangladesh"],
      ["bb", "BRB", "Barbados"],
      ["by", "BLR", "Belarus"],
      ["be", "BEL", "Belgium"],
      ["bz", "BLZ", "Belize"],
      ["bj", "BEN", "Benin"],
      ["bm", "BMU", "Bermuda"],
      ["bt", "BTN", "Bhutan"],
      ["bo", "BOL", "Bolivia, Plurinational State of"],
      ["bq", "BES", "Bonaire, Sint Eustatius and Saba"],
      ["ba", "BIH", "Bosnia and Herzegovina"],
      ["bw", "BWA", "Botswana"],
      ["bv", "BVT", "Bouvet Island"],
      ["br", "BRA", "Brazil"],
      ["io", "IOT", "British Indian Ocean Territory"],
      ["bn", "BRN", "Brunei Darussalam"],
      ["bg", "BGR", "Bulgaria"],
      ["bf", "BFA", "Burkina Faso"],
      ["bi", "BDI", "Burundi"],
      ["kh", "KHM", "Cambodia"],
      ["cm", "CMR", "Cameroon"],
      ["ca", "CAN", "Canada"],
      ["cv", "CPV", "Cape Verde"],
      ["ky", "CYM", "Cayman Islands"],
      ["cf", "CAF", "Central African Republic"],
      ["td", "TCD", "Chad"],
      ["cl", "CHL", "Chile"],
      ["cn", "CHN", "China"],
      ["cx", "CXR", "Christmas Island"],
      ["cc", "CCK", "Cocos (Keeling) Islands"],
      ["co", "COL", "Colombia"],
      ["km", "COM", "Comoros"],
      ["cg", "COG", "Congo"],
      ["cd", "COD", "Congo, the Democratic Republic of the"],
      ["ck", "COK", "Cook Islands"],
      ["cr", "CRI", "Costa Rica"],
      ["ci", "CIV", "Côte d'Ivoire"],
      ["hro", "HRV", "Croatia"],
      ["cu", "CUB", "Cuba"],
      ["cw", "CUW", "Curaçao"],
      ["cy", "CYP", "Cyprus"],
      ["cz", "CZE", "Czech Republic"],
      ["den", "DNK", "Denmark"],
      ["dj", "DJI", "Djibouti"],
      ["dm", "DMA", "Dominica"],
      ["do", "DOM", "Dominican Republic"],
      ["ec", "ECU", "Ecuador"],
      ["eg", "EGY", "Egypt"],
      ["sv", "SLV", "El Salvador"],
      ["gq", "GNQ", "Equatorial Guinea"],
      ["er", "ERI", "Eritrea"],
      ["est", "EST", "Estonia"],
      ["et", "ETH", "Ethiopia"],
      ["fk", "FLK", "Falkland Islands (Malvinas)"],
      ["fo", "FRO", "Faroe Islands"],
      ["fj", "FJI", "Fiji"],
      ["fin", "FIN", "Finland"],
      ["fra", "FRA", "France"],
      ["gf", "GUF", "French Guiana"],
      ["pf", "PYF", "French Polynesia"],
      ["tf", "ATF", "French Southern Territories"],
      ["ga", "GAB", "Gabon"],
      ["gm", "GMB", "Gambia"],
      ["ge", "GEO", "Georgia"],
      ["dui", "DEU", "Germany"],
      ["gh", "GHA", "Ghana"],
      ["gi", "GIB", "Gibraltar"],
      ["gre", "GRC", "Greece"],
      ["gl", "GRL", "Greenland"],
      ["gd", "GRD", "Grenada"],
      ["gp", "GLP", "Guadeloupe"],
      ["gu", "GUM", "Guam"],
      ["gt", "GTM", "Guatemala"],
      ["gg", "GGY", "Guernsey"],
      ["gn", "GIN", "Guinea"],
      ["gw", "GNB", "Guinea-Bissau"],
      ["gy", "GUY", "Guyana"],
      ["ht", "HTI", "Haiti"],
      ["hm", "HMD", "Heard Island and McDonald Islands"],
      ["va", "VAT", "Holy See (Vatican City State)"],
      ["hn", "HND", "Honduras"],
      ["hk", "HKG", "Hong Kong"],
      ["hu", "HUN", "Hungary"],
      ["is", "ISL", "Iceland"],
      ["in", "IND", "India"],
      ["id", "IDN", "Indonesia"],
      ["ir", "IRN", "Iran, Islamic Republic of"],
      ["iq", "IRQ", "Iraq"],
      ["ier", "IRL", "Ireland"],
      ["im", "IMN", "Isle of Man"],
      ["il", "ISR", "Israel"],
      ["ita", "ITA", "Italy"],
      ["jm", "JAM", "Jamaica"],
      ["jp", "JPN", "Japan"],
      ["je", "JEY", "Jersey"],
      ["jo", "JOR", "Jordan"],
      ["kz", "KAZ", "Kazakhstan"],
      ["ke", "KEN", "Kenya"],
      ["ki", "KIR", "Kiribati"],
      ["kp", "PRK", "Korea, Democratic People's Republic of"],
      ["kr", "KOR", "Korea, Republic of"],
      ["kw", "KWT", "Kuwait"],
      ["kg", "KGZ", "Kyrgyzstan"],
      ["la", "LAO", "Lao People's Democratic Republic"],
      ["lv", "LVA", "Latvia"],
      ["lb", "LBN", "Lebanon"],
      ["ls", "LSO", "Lesotho"],
      ["lr", "LBR", "Liberia"],
      ["ly", "LBY", "Libya"],
      ["li", "LIE", "Liechtenstein"],
      ["lt", "LTU", "Lithuania"],
      ["lu", "LUX", "Luxembourg"],
      ["mo", "MAC", "Macao"],
      ["mk", "MKD", "Macedonia, the former Yugoslav Republic of"],
      ["mg", "MDG", "Madagascar"],
      ["mw", "MWI", "Malawi"],
      ["my", "MYS", "Malaysia"],
      ["mv", "MDV", "Maldives"],
      ["ml", "MLI", "Mali"],
      ["mt", "MLT", "Malta"],
      ["mh", "MHL", "Marshall Islands"],
      ["mq", "MTQ", "Martinique"],
      ["mr", "MRT", "Mauritania"],
      ["mu", "MUS", "Mauritius"],
      ["yt", "MYT", "Mayotte"],
      ["mx", "MEX", "Mexico"],
      ["fm", "FSM", "Micronesia, Federated States of"],
      ["md", "MDA", "Moldova, Republic of"],
      ["mc", "MCO", "Monaco"],
      ["mn", "MNG", "Mongolia"],
      ["me", "MNE", "Montenegro"],
      ["ms", "MSR", "Montserrat"],
      ["ma", "MAR", "Morocco"],
      ["mz", "MOZ", "Mozambique"],
      ["mm", "MMR", "Myanmar"],
      ["na", "NAM", "Namibia"],
      ["nr", "NRU", "Nauru"],
      ["np", "NPL", "Nepal"],
      ["nld", "NLD", "Netherlands"],
      ["nc", "NCL", "New Caledonia"],
      ["nz", "NZL", "New Zealand"],
      ["ni", "NIC", "Nicaragua"],
      ["ne", "NER", "Niger"],
      ["ng", "NGA", "Nigeria"],
      ["nu", "NIU", "Niue"],
      ["nf", "NFK", "Norfolk Island"],
      ["mp", "MNP", "Northern Mariana Islands"],
      ["nor", "NOR", "Norway"],
      ["om", "OMN", "Oman"],
      ["pk", "PAK", "Pakistan"],
      ["pw", "PLW", "Palau"],
      ["ps", "PSE", "Palestine, State of"],
      ["pa", "PAN", "Panama"],
      ["pg", "PNG", "Papua New Guinea"],
      ["py", "PRY", "Paraguay"],
      ["pe", "PER", "Peru"],
      ["ph", "PHL", "Philippines"],
      ["pn", "PCN", "Pitcairn"],
      ["pl", "POL", "Poland"],
      ["port", "PRT", "Portugal"],
      ["pr", "PRI", "Puerto Rico"],
      ["qa", "QAT", "Qatar"],
      ["re", "REU", "Réunion"],
      ["ro", "ROU", "Romania"],
      ["ru", "RUS", "Russian Federation"],
      ["rw", "RWA", "Rwanda"],
      ["bl", "BLM", "Saint Barthélemy"],
      ["sh", "SHN", "Saint Helena, Ascension and Tristan da Cunha"],
      ["kn", "KNA", "Saint Kitts and Nevis"],
      ["lc", "LCA", "Saint Lucia"],
      ["mf", "MAF", "Saint Martin (French part)"],
      ["pm", "SPM", "Saint Pierre and Miquelon"],
      ["vc", "VCT", "Saint Vincent and the Grenadines"],
      ["ws", "WSM", "Samoa"],
      ["sm", "SMR", "San Marino"],
      ["st", "STP", "Sao Tome and Principe"],
      ["sa", "SAU", "Saudi Arabia"],
      ["sn", "SEN", "Senegal"],
      ["rs", "SRB", "Serbia"],
      ["sc", "SYC", "Seychelles"],
      ["sl", "SLE", "Sierra Leone"],
      ["sg", "SGP", "Singapore"],
      ["sx", "SXM", "Sint Maarten (Dutch part)"],
      ["sk", "SVK", "Slovakia"],
      ["si", "SVN", "Slovenia"],
      ["sb", "SLB", "Solomon Islands"],
      ["so", "SOM", "Somalia"],
      ["za", "ZAF", "South Africa"],
      ["gs", "SGS", "South Georgia and the South Sandwich Islands"],
      ["ss", "SSD", "South Sudan"],
      ["esp", "ESP", "Spain"],
      ["lk", "LKA", "Sri Lanka"],
      ["sd", "SDN", "Sudan"],
      ["sr", "SUR", "Suriname"],
      ["sj", "SJM", "Svalbard and Jan Mayen"],
      ["sz", "SWZ", "Swaziland"],
      ["swe", "SWE", "Sweden"],
      ["ch", "CHE", "Switzerland"],
      ["sy", "SYR", "Syrian Arab Republic"],
      ["tw", "TWN", "Taiwan, Province of China"],
      ["tj", "TJK", "Tajikistan"],
      ["tz", "TZA", "Tanzania, United Republic of"],
      ["th", "THA", "Thailand"],
      ["tl", "TLS", "Timor-Leste"],
      ["tg", "TGO", "Togo"],
      ["tk", "TKL", "Tokelau"],
      ["to", "TON", "Tonga"],
      ["tt", "TTO", "Trinidad and Tobago"],
      ["tn", "TUN", "Tunisia"],
      ["tr", "TUR", "Turkey"],
      ["tm", "TKM", "Turkmenistan"],
      ["tc", "TCA", "Turks and Caicos Islands"],
      ["tv", "TUV", "Tuvalu"],
      ["ug", "UGA", "Uganda"],
      ["ua", "UKR", "Ukraine"],
      ["ae", "ARE", "United Arab Emirates"],
      ["gb", "GBR", "United Kingdom"],
      ["us", "USA", "United States"],
      ["um", "UMI", "United States Minor Outlying Islands"],
      ["uy", "URY", "Uruguay"],
      ["uz", "UZB", "Uzbekistan"],
      ["vu", "VUT", "Vanuatu"],
      ["ve", "VEN", "Venezuela, Bolivarian Republic of"],
      ["vn", "VNM", "Viet Nam"],
      ["vg", "VGB", "Virgin Islands, British"],
      ["vi", "VIR", "Virgin Islands, U.S."],
      ["wf", "WLF", "Wallis and Futuna"],
      ["eh", "ESH", "Western Sahara"],
      ["ye", "YEM", "Yemen"],
      ["zm", "ZMB", "Zambia"],
      ["zw", "ZWE", "Zimbabwe"]
    ];

//all countrycodes with available data
countries = ["AUT", "BEL", "BGR", "CYP", "CZE", "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "GBR", "GRC", "HRV",
"HUN", "IRL", "ISL", "ITA", "LIE", "LTU", "LUX", "LVA", "MLT", "NLD", "NOR", "POL", "PRT", "ROU", "SVK", 
"SVN", "SWE", "TUR"];



//to be used variable
var data;

d3.json("students_ready.json", function(error, json) {
  if (error) return console.warn(error);
  data = json;
  
      //all variables to be used
      var year_2003_in = []
      var year_2006_in = []
      var year_2009_in = []
      var year_2012_in = []

      //go through all countries out of json array
      for (i = 0; i < data.length; i++)
      { 
        //go through all countries with countrycodes
        for (j = 0; j < country_codes.length; j++)
        { 
          //if country names match, 
          if (data[i].country === country_codes[j][2])
          {
            //update variables
            year_2003_in[country_codes[j][1]] = {in_year: data[i].in_2003};

            year_2006_in[country_codes[j][1]] = {in_year: data[i].in_2006};

            year_2009_in[country_codes[j][1]] = {in_year: data[i].in_2009};

            year_2012_in[country_codes[j][1]] = {in_year: data[i].in_2012};

          }
        }
      }

 

   
 
//function to give every datapoint a fillkey
function fill_dec(dataset){
      console.log(dataset.length)
      for (i = 0; i < countries.length; i++) {
            if (dataset[countries[i]].in_year > 120)
                  dataset[countries[i]]["fillKey"] = '7';    
            else if (dataset[countries[i]].in_year > 80)
                  dataset[countries[i]]["fillKey"] = '6';
            else if (dataset[countries[i]].in_year > 65)
                  dataset[countries[i]]["fillKey"] = '5';
            else if (dataset[countries[i]].in_year > 50)
                  dataset[countries[i]]["fillKey"] = '4';
            else if (dataset[countries[i]].in_year > 35)
                  dataset[countries[i]]["fillKey"] = '3';
            else if (dataset[countries[i]].in_year > 25)
                  dataset[countries[i]]["fillKey"] = '2';
            else if (dataset[countries[i]].in_year > 1)
                  dataset[countries[i]]["fillKey"] = '1';
      // console.log(dataset)
      }

}

//default year for data
temp = year_2003_in;
fill_dec(temp)    

//create map centered at Europe
  var graph = new Datamap({
          element: document.getElementById("container1"),
          projection: 'mercator',
          setProjection: function(element) {
            var projection = d3.geo.equirectangular()
              .center([10, 50])
              .rotate([4.4, 0])
              .scale(600)
              .translate([element.offsetWidth / 2, element.offsetHeight / 2]);
            var path = d3.geo.path()
              .projection(projection);
            return {path: path, projection: projection};  
          },
          // create tooltip
          geographyConfig: {
            highlightBorderColor: '#bada55',
            popupTemplate: function(geography, data) {
              return '<div class="hoverinfo"><b>' + geography.properties.name + '</b></br> Number of Students: ' +  data.in_year + ' '
            },
          highlightBorderWidth: 3
          },
          //fill scale
          fills: {
              '1' : "#eff3ff",
              '2' : '#c6dbef',
              '3' : '#9ecae1',
              '4' : '#6baed6',
              '5' : '#4292c6',
              '6' : '#2171b5',
              '7' : '#084594',
              defaultFill: 'black' 
           },
           data: temp,
           //when a country is clicked, call function MakeBarChart
           done: function(datamap) {
              datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
                MakeBarChart(geography.id)
           });
          }
    });


var dataset = 0;
var slide = document.getElementById('slide'),
    sliderDiv = document.getElementById("sliderAmount");

//on change of slider, refill the countries with colours
slide.onchange = function() { 
    sliderDiv.innerHTML = this.value    
    
    //check which year is given by slider
    if (this.value == 2006){
      dataset = year_2006_in;
      console.log(dataset)
    }  
    else if (this.value == 2009)
      dataset = year_2009_in;
    else if (this.value == 2012)
      dataset = year_2012_in;
    else
      dataset = year_2003_in;

    fill_dec(dataset)
        

    graph.updateChoropleth(dataset)
}


//to be used variable  
temp_data = [];


//function to create data variable for BarChart
function MakeBarChart(landcode){

  temp_data[0] = {year: 2003, in_year : year_2003_in[landcode].in_year};

  temp_data[1] = {year: 2006, in_year : year_2006_in[landcode].in_year};

  temp_data[2] = {year: 2009, in_year : year_2009_in[landcode].in_year};

  temp_data[3] = {year: 2012, in_year : year_2012_in[landcode].in_year};

  data = temp_data;

  console.log(data)

  //delete svg
  //d3.select(".chart").remove();   
  
//create margins
  var margin = {top: 20, right: 30, bottom: 30, left: 40},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

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

//create new svg
  var chart = d3.select("body")
                  .append("svg")
                    .attr("class", "chart")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                  .append("g")
                    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    
  x.domain(data.map(function(d) { return d.year; }));
  y.domain([0, d3.max(data, function(d) { return parseFloat(d.in_year); })]);

  chart.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

  chart.append("g")
        .attr("class", "y axis")
        .call(yAxis);

  chart.selectAll(".bar")
        .data(data)
      .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.year); })
        .attr("y", function(d) {return y(parseFloat(d.in_year)); })
        .attr("height", function(d) { return height - y(parseFloat(d.in_year)); })
        .attr("width", x.rangeBand());


  function type(d) {
    d.value = +d.value; // coerce to number
    return d;
  }
}

});




















