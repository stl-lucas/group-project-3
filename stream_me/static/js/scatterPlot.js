d3.json("/api/v1/movies", function (movies) {

    // console.log("movies length before filter: ", movies.length);
    filteredMovies = movies.filter(movie => {
        return movie.rotten_tomatoes && movie.imdb_score;
    })
    // console.log("movies filtered length: ", filteredMovies.length)
    console.log("filtered movies: ", filteredMovies);

    // Chart area
    var chart_width = 800;
    var chart_height = 400;
    var padding = 50;

    //  Scale data for visualization
    var scale = d3.scaleLinear()   // should set a variable for your scale
        .domain([0, 100])
        .range([10, 350])

    // Create scales
    var x_scale = d3.scaleLinear()
        .domain([0, 10])
        .range([padding, chart_height]);

    var y_scale = d3.scaleLinear()
        .domain([0, 100])
        .range([0, chart_width]);

    var r_scale = d3.scaleLinear()
        .domain(0, d3.max(filteredMovies, function (d) {
            return calculateRadius(d);
        }))
        .range([5, 30]);            //range chosen so that min won't be too low
                                    //to see, and max is not bigger than padding

    var x_axis = d3.axisBottom(x_scale);
    var y_axis = d3.axisLeft(y_scale);


    // Create SVG element
    var svg = d3.select('#chart')
        .append('svg')
        .attr('width', chart_width)
        .attr('height', chart_height);

    svg.append('g')
        .attr('class', 'x-axis')
        .attr(
            'transform',
            'translate(0,' + (chart_height - padding) + ')'
        )
        .call(x_axis);

    svg.append('g')
    .attr('class', 'y-axis')
    .attr(
        'transform',
        'translate(0,' + (chart_width - padding) + ')'
    )
    .call(y_axis);

    // Calculate radius
    function calculateRadius(movie) {
        if (movie.imdb_score && movie.rotten_tomatoes) {
            return (movie.rotten_tomatoes / 10 + movie.imdb_score) / 2;
        }
        return 0;
    }

    // Create plot points
    svg.selectAll('circle')
        .data(filteredMovies)
        .enter()
        .append('circle')
        .attr('cx', function (d) { 
            // console.log('imbdb: ', d.imdb_score);  // d represents the current value in the array
            return x_scale(d.imdb_score);           // since the example contained a set of arrays
        })
        .attr('cy', function (d) {
            return y_scale(d.rotten_tomatoes);
        })
        // sets the radius of the circle
        .attr('r', function (d) {
            return calculateRadius(d);         // Scale circles here if needed to fit chart
        })
        .attr('fill', '#D1AB0E');

    // Create plot point labels
    svg.append('g')
        .selectAll('text')
        .data(filteredMovies)
        .enter()
        .append('text')
        .text(function (d) {
            return d.title;     // join() function combines arrays to strings. 
        })                          // Useful for displaying coords stored in arrays.
        .attr('x', function (d) {
            return x_scale(d[0]);
        })
        .attr('y', function (d) {
            return y_scale(d[1]);
        })


})