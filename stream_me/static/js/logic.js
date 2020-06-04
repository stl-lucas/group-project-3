// Create Total Movie Bar Plot
var svgWidth = 300;
var svgHeight = 300;

var chartMargin = {
  top: 10,
  right: 10,
  bottom: 10,
  left: 10
};

var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

var svg = d3
  .select("#movies")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

var movieUrl = "/api/v1/movies";

d3.json(movieUrl).then(function(movieData) {
    totalMovies = [{'netflix': 0, 'hulu': 0, 'prime': 0, 'disney': 0}]

    movieData.forEach(function(data) {
        if (data.netflix) {
            totalMovies['netflix']+=1;
        }
        if (data.hulu) {
            totalMovies['hulu']+=1;
        }
        if (data.prime) {
            totalMovies['prime']+=1;
        }
        if (data.disney) {
            totalMovies['disney']+=1;
        }
    });

    var barSpacing = 5;
    var scaleY = 10;

    var barWidth = (chartWidth - (barSpacing * 3)) / 4;

    chartGroup.selectAll(".bar")
        .data(totalMovies)
        .enter()
        .append("rect")
        .classed("bar", true)
        .attr("width", d => barWidth)
        .attr("height", d => d.values * scaleY)
        .attr("x", (d, i) => i * (barWidth + barSpacing))
        .attr("y", d => chartHeight - d.values * scaleY);
}).catch(error => console.log(error));
