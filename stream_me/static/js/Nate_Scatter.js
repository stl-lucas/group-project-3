var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

  d3.csv("Documents/GitHub/group-project-3/data/movies_100.csv").then(function(csvdata) {  
    console.log(csvdata);
    csvdata.forEach(function(data){
        data.IMDb = +data.IMDb;
        data.Directors = data.Directors;
          console.log("parseData",data)
    });
    var xLinearScale = d3.scaleLinear()
    .domain([10, d3.max(csvdata, d => d.IMDb)])
    .range([0, width]);
  
      var yLinearScale = d3.scaleLinear()
    .domain([20, d3.max(csvdata, d => d.Directors)])
    .range([height, 0]);

    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);
    
      var circlesGroup = chartGroup.selectAll("circle")
      .data(csvdata)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d.IMDb))
      .attr("cy", d => yLinearScale(d.Directors))
      .attr("text-anchor", "middle")
      .attr("r", "10")
      .attr("fill", "green")
      .attr("opacity", ".5");
      console.log(csvdata);
      chartGroup.selectAll("null").data(csvdata)
      .enter().append("text").text(function(d){
       return d.abbr;
    })
    .attr("x",d => xLinearScale(d.IMDb))
    .attr("y", d => yLinearScale(d.Directors))
    .attr("text-anchor", "middle")
    .attr('fill', 'white')
    .attr('font-size', 10);
 
   var toolTip = d3.tip()
       .attr("class", "tooltip")
       .offset([80, -60])
       .html(function(d) {
         return (`<br>Top IMDb Scores : ${d.IMDb}<br>Top 100 Directors: ${d.Directors}`);
       });
 
       chartGroup.call(toolTip);
 
       circlesGroup.on("click", function(csvdata) {
         toolTip.show(csvdata, this);
       })
 
       .on("mouseout", function(csvdata, index) {
         toolTip.hide(csvdata);
       });
 
       chartGroup.append("text")
       .attr("transform", "rotate(-90)")
       .attr("y", 0 - margin.left + 40)
       .attr("x", 0 - (height / 2))
       .attr("dy", "1em")
       .attr("class", "axisText")
       .text("Directors");
 
       chartGroup.append("text")
       .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
       .attr("class", "axisText")
       .text("IMDb");
   }).catch(function(error) {
     console.log(error);
   });
 
  