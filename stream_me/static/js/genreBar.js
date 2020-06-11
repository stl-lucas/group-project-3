// Set API URL Variables
var movieUrl = "api/v1/movies";
var showUrl = "api/v1/shows";
var serviceUrl = "/api/v1/services";    //This segment borrowed from Tim

// Grab Movie Data
d3.json(movieUrl).then(function (movieData) {

    // Grab Show Data
    d3.json(showUrl).then(function (showData) {

        d3.json(serviceUrl).then(function (servicesData) {

            // Set Variables and Loop Through each Movie
            var genreCounts = {
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

            movieData.forEach(movie => {
                var services = [];
                if (movie.netflix) {
                    services.push("netflix");
                }
                if (movie.prime) {
                    services.push("prime");
                }
                if (movie.hulu) {
                    services.push("hulu");
                }
                if (movie.disney) {
                    services.push("disney");
                }
                if (movie.genres) {
                    theGenres = movie.genres.split(',');
                    theGenres.forEach(genre => {
                        services.forEach(service => {
                            if (genreCounts[service][genre]) {
                                genreCounts[service][genre] = genreCounts[service][genre] + 1;
                            } else {
                                genreCounts[service][genre] = 1;
                            }
                        })
                    })
                }
            });

            // servicesData.forEach(function (data) {
            //     if (data.name === "Netflix") {
            //         yPrice[0] = data.price;
            //     }
            //     if (data.name === "Hulu") {
            //         yPrice[1] = data.price;
            //     }
            //     if (data.name === "Prime Video") {
            //         yPrice[2] = data.price;
            //     }
            //     if (data.name === "Disney +") {
            //         yPrice[3] = data.price;
            //     }
            // });

            // movieData.forEach(function (data) {
            //     if (data.netflix) {
            //         yMovies[0] += 1;
            //         if (data.imdb_score) {
            //             imdb[0] = imdb[0] + data.imdb_score;
            //             imdb_count[0] += 1;
            //         }
            //         if (data.rotten_tomatoes) {
            //             tomatoes[0] = tomatoes[0] + data.rotten_tomatoes;
            //             tomatoes_count[0] += 1;
            //         }
            //     }
            //     if (data.hulu) {
            //         yMovies[1] += 1;
            //         if (data.imdb_score) {
            //             imdb[1] = imdb[1] + data.imdb_score;
            //             imdb_count[1] += 1;
            //         }
            //         if (data.rotten_tomatoes) {
            //             tomatoes[1] = tomatoes[1] + data.rotten_tomatoes;
            //             tomatoes_count[1] += 1;
            //         }
            //     }
            //     if (data.prime) {
            //         yMovies[2] += 1;
            //         if (data.imdb_score) {
            //             imdb[2] = imdb[2] + data.imdb_score;
            //             imdb_count[2] += 1;
            //         }
            //         if (data.rotten_tomatoes) {
            //             tomatoes[2] = tomatoes[2] + data.rotten_tomatoes;
            //             tomatoes_count[2] += 1;
            //         }
            //     }
            //     if (data.disney) {
            //         yMovies[3] += 1;
            //         if (data.imdb_score) {
            //             imdb[3] = imdb[3] + data.imdb_score;
            //             imdb_count[3] += 1;
            //         }
            //         if (data.rotten_tomatoes) {
            //             tomatoes[3] = tomatoes[3] + data.rotten_tomatoes;
            //             tomatoes_count[3] += 1;
            //         }
            //     }
            // });

            // // Calculate Avg Ratings
            // var avgImdb = [0, 0, 0, 0];
            // var avgTomato = [0, 0, 0, 0];

            // for (var i = 0; i < 4; i++) {
            //     avgImdb[i] = (imdb[i] / imdb_count[i]).toPrecision(2);
            //     avgTomato[i] = (tomatoes[i] / tomatoes_count[i]).toPrecision(2);
            // };

            // // Loop Through Shows
            // showData.forEach(function (data) {
            //     if (data.netflix) {
            //         yShows[0] += 1;
            //     }
            //     if (data.hulu) {
            //         yShows[1] += 1;
            //     }
            //     if (data.prime) {
            //         yShows[2] += 1;
            //     }
            //     if (data.disney) {
            //         yShows[3] += 1;
            //     }
            // });

            // // Build Avg Display
            // d3.select("#ratingNetflix").selectAll("p").html(`Price: $${yPrice[0]}<br/>Avg IMDB:  ${avgImdb[0]}<br/>Avg Rotten Tomatoes: ${avgTomato[0]}%`);
            // d3.select("#ratingHulu").selectAll("p").html(`Price: $${yPrice[1]}<br/>Avg IMDB:  ${avgImdb[1]}<br/>Avg Rotten Tomatoes: ${avgTomato[1]}%`);
            // d3.select("#ratingPrime").selectAll("p").html(`Price: $${yPrice[2]}<br/>Avg IMDB:  ${avgImdb[2]}<br/>Avg Rotten Tomatoes: ${avgTomato[2]}%`);
            // d3.select("#ratingDisney").selectAll("p").html(`Price: $${yPrice[3]}<br/>Avg IMDB:  ${avgImdb[3]}<br/>Avg Rotten Tomatoes: ${avgTomato[3]}%`);

            // // Build Price Count Plot
            // var trace0 = {
            //     x: xAxis,
            //     y: yPrice,
            //     name: "Price",
            //     marker: {
            //         color: ["#E50914", "#1DB954", "#FF9900", "#333399"]
            //     },
            //     type: "bar"
            // };

            // var data0 = [trace0];

            // var layout0 = {
            //     title: "Monthly Service Price $",
            //     yaxis: {
            //         automargin: true
            //     }
            // };

            // Plotly.newPlot("prices", data0, layout0);

            // // Build Title Count Plot
            // var trace1 = {
            //     x: xAxis,
            //     y: yMovies,
            //     name: "Movies",
            //     marker: {
            //         color: ["#E50914", "#1DB954", "#FF9900", "#333399"]
            //     },
            //     type: "bar"
            // };

            // var trace2 = {
            //     x: xAxis,
            //     y: yShows,
            //     name: "Shows",
            //     marker: {
            //         color: ["#B70710", "#179443", "#CC7A00", "#28287A"]
            //     },
            //     type: "bar"
            // };

            // var data1 = [trace1, trace2];

            // var layout1 = {
            //     title: "# of Movies and Shows by Service",
            //     barmode: "group",
            //     yaxis: {
            //         automargin: true
            //     }
            // };

            // Plotly.newPlot("titles", data1, layout1);

        }).catch(error => console.log(error));

    }).catch(error => console.log(error));

}).catch(error => console.log(error));