//d3 load JSON file
//http://stackoverflow.com/questions/17214293/importing-local-json-file-using-d3-json-does-not-work

//laad de data in
// var data = d3.json("barchart.json", function(error, data) {
// 	console.log(data);
// )};

var data; // a global

d3.json("barchart.json", function(error, json) {
  if (error) return console.warn(error);
  data = json;
  console.log(data)
});