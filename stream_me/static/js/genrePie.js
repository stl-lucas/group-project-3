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

                },
                prime: {

                },
                hulu: {

                },
                disney: {

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

            //Filter down to top 10
            // netflixTopTen = Object.entries(genreCounts.netflix)
            // .sort((a, b) => {
            //     return b[1] - a[1];
            // })
            // .splice(0, 10);

            // console.log('netflix top 10: ', netflixTopTen);

            function filterTopTenGenres(genreCount){
                topTen = Object.entries(genreCount)
                .sort((a, b) => {
                    return b[1] - a[1];
                })
                .splice(0, 5);

                return topTen;
            }

            netflixTopTen = filterTopTenGenres(genreCounts.netflix);
            primeTopTen = filterTopTenGenres(genreCounts.prime);
            huluTopTen = filterTopTenGenres(genreCounts.hulu);
            disneyTopTen = filterTopTenGenres(genreCounts.disney);

            //Donut chart
            var data = [{
                values: netflixTopTen.map(entry => {return entry[1]}),
                labels: netflixTopTen.map(entry => {return entry[0]}),
                domain: { row: 0, column: 0 },
                name: 'Netflix',
                hoverinfo: 'label+value+percent',
                hole: .4,
                type: 'pie',
            },
            {
                values: primeTopTen.map(entry => {return entry[1]}),
                labels: primeTopTen.map(entry => {return entry[0]}),
                domain: { row: 0, column: 1 },
                name: 'Amazon Prime',
                hoverinfo: 'label+value+percent',
                hole: .4,
                type: 'pie'
            },
            {
                values: huluTopTen.map(entry => {return entry[1]}),
                labels: huluTopTen.map(entry => {return entry[0]}),
                domain: { row: 1, column: 0 },
                name: 'Hulu',
                hoverinfo: 'label+value+percent',
                hole: .4,
                type: 'pie'
            },
            {
                values: disneyTopTen.map(entry => {return entry[1]}),
                labels: disneyTopTen.map(entry => {return entry[0]}),
                domain: { row: 1, column: 1 },
                name: 'Disney+',
                hoverinfo: 'label+value+percent',
                hole: .4,
                type: 'pie'
            }];

            var layout = {
                title: 'Top 5 Genres of Each Service',
                annotations: [
                    {
                        font: {
                            size: 11
                        },
                        showarrow: false,
                        text: 'Netflix',
                        x: 0.17,
                        y: 0.75
                    },
                    {
                        font: {
                            size: 11
                        },
                        showarrow: false,
                        text: 'Prime',
                        x: 0.85,
                        y: 0.75
                    },
                    {
                        font: {
                            size: 11
                        },
                        showarrow: false,
                        text: 'Hulu',
                        x: 0.17,
                        y: 0.25
                    },
                    {
                        font: {
                            size: 11
                        },
                        showarrow: false,
                        text: 'Disney +',
                        x: 0.85,
                        y: 0.25
                    }
                ],
                height: 450,
                width: 450,
                showlegend: true,
                grid: {rows: 2, columns: 2}
            };

            Plotly.newPlot('vis', data, layout);

        }).catch(error => console.log(error));

    }).catch(error => console.log(error));

}).catch(error => console.log(error));