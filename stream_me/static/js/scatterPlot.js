d3.json("api/v1/movies").then(function (movies) {

    filteredMovies = movies.filter(movie => {
        return movie.rotten_tomatoes && movie.imdb_score;
    })

    var serviceSummary = {
        netflix: {
            name: 'Netflix',
            movieCount: 0,
            imdbTotal: 0.0,
            rottenTomatoesTotal: 0
        },
        prime: {
            name: 'Amazon Prime',
            movieCount: 0,
            imdbTotal: 0.0,
            rottenTomatoesTotal: 0
        },
        hulu: {
            name: 'Hulu',
            movieCount: 0,
            imdbTotal: 0.0,
            rottenTomatoesTotal: 0
        },
        disney: {
            name: 'Disney+',
            movieCount: 0,
            imdbTotal: 0.0,
            rottenTomatoesTotal: 0
        }
    }

    filteredMovies.forEach(ratedMovie => {
        if (ratedMovie.netflix) {
            serviceSummary.netflix.movieCount++;
            serviceSummary.netflix.imdbTotal += ratedMovie.imdb_score;
            serviceSummary.netflix.rottenTomatoesTotal += ratedMovie.rotten_tomatoes;
        }

        if (ratedMovie.hulu) {
            serviceSummary.hulu.movieCount++;
            serviceSummary.hulu.imdbTotal += ratedMovie.imdb_score;
            serviceSummary.hulu.rottenTomatoesTotal += ratedMovie.rotten_tomatoes;
        }

        if (ratedMovie.prime) {
            serviceSummary.prime.movieCount++;
            serviceSummary.prime.imdbTotal += ratedMovie.imdb_score;
            serviceSummary.prime.rottenTomatoesTotal += ratedMovie.rotten_tomatoes;
        }

        if (ratedMovie.disney) {
            serviceSummary.disney.movieCount++;
            serviceSummary.disney.imdbTotal += ratedMovie.imdb_score;
            serviceSummary.disney.rottenTomatoesTotal += ratedMovie.rotten_tomatoes;
        }
    })

    var serviceDots = [
        serviceSummary.netflix, serviceSummary.hulu, serviceSummary.prime, serviceSummary.disney
    ];

    // Chart area
    var chart_width = 800;
    var chart_height = 400;
    var padding = 50;

    // Create scales
    var x_scale = d3.scaleLinear()
        .domain([6.2, 6.6])
        .range([0, chart_width - padding]);

    var y_scale = d3.scaleLinear()
        .domain([60, 68])
        .range([chart_height - padding, 0]);

    var maxCount = d3.max(serviceDots, d => { return d.movieCount });

    var r_scale = d3.scaleLinear()
        .domain([0, maxCount])
        .range([0, 125]);

    var x_axis = d3.axisBottom(x_scale);
    var y_axis = d3.axisLeft(y_scale);

    // Create SVG element
    var svg = d3.select('#chart')
        .append('svg')
        .attr('width', chart_width)
        .attr('height', chart_height)
        .append('g')
        .attr('transform', 'translate(100, 30)');

    svg.append('g')
        .attr('class', 'x-axis')
        .attr(
            'transform',
            'translate(0,' + (chart_height - padding) + ')'
        )
        .call(x_axis);

    svg.append('g')
        .attr('class', 'y-axis')
        .call(y_axis);

    // Create plot points
    svg.selectAll('circle')
        .data(serviceDots)
        .enter()
        .append('circle')
        .attr('cx', function (d) {
            return x_scale(d.imdbTotal / d.movieCount);
        })
        .attr('cy', function (d) {
            return y_scale(d.rottenTomatoesTotal / d.movieCount);
        })
        .attr('r', function (d) {
            return r_scale(d.movieCount);
        })
        .attr('fill', function (d) {
            if (d.name === "Netflix") {
                return "#E50914"; // Red
            }
            if (d.name === "Hulu") {
                return "#1DB954"; // Green
            }
            if (d.name === "Amazon Prime") {
                return "#FF9900"; // Orange
            }
            if (d.name === "Disney+") {
                return "#333399";  // Dark Blue
            }
        });

    // Create plot point labels
    svg.append('g')
        .selectAll('text')
        .data(serviceDots)
        .enter()
        .append('text')
        .text(function (d) {
            return d.name;
        })
        .attr('x', function (d) {
            return x_scale(d.imdbTotal / d.movieCount) - (r_scale(d.movieCount) / 2);
        })
        .attr('y', function (d) {
            return y_scale(d.rottenTomatoesTotal / d.movieCount);
        });

    //x-axis label
    svg.append('g')
        .attr('class', 'xLabel')
        .selectAll('text')
        .data(['Average IMDB Rating'])
        .enter()
        .append('text')
        .attr('x', chart_width / 3)
        .attr('y', chart_height - padding)
        .text(function (d) { return d });
    
    //y-axis
    svg.append('g')
        .attr('class', 'yLabel')
        .selectAll('text')
        .data(['Average Rotten Tomatoes Rating'])
        .enter()
        .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', 0 - chart_height + padding + padding)
        .attr('y', 0 - padding)
        .text(function (d) { return d })

}).catch(error => console.log(error));