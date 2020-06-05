// Set API URL Variables
var movieUrl = "api/v1/movies";
var showUrl = "api/v1/shows";

// Grab Movie Data
d3.json(movieUrl).then(function(movieData) {
    
  // Grab Show Data
  d3.json(showUrl).then(function(showData) {
      
    // TODO: Need code to filter data with user input

    // Set Variables and Loop Through each Movie
    var xAxis = ['Netflix', 'Hulu', 'Prime', 'Disney']
    var yMovies = [0, 0, 0, 0]
    var yShows = [0, 0, 0, 0]
    var imdb = [0, 0, 0, 0]
    var tomatoes = [0, 0, 0, 0]

    movieData.forEach(function(data) {
      if (data.netflix) {
          yMovies[0]+=1;
          imdb[0] = imdb[0] + data.imdb_score;
          tomatoes[0] = tomatoes[0] + data.rotten_tomatoes;
      }
      if (data.hulu) {
          yMovies[1]+=1;
          imdb[1] = imdb[1] + data.imdb_score;
          tomatoes[1] = tomatoes[1] + data.rotten_tomatoes;
      }
      if (data.prime) {
          yMovies[2]+=1;
          imdb[2] = imdb[2] + data.imdb_score;
          tomatoes[2] = tomatoes[2] + data.rotten_tomatoes;
      }
      if (data.disney) {
          yMovies[3]+=1;
          imdb[3] = imdb[3] + data.imdb_score;
          tomatoes[3] = tomatoes[3] + data.rotten_tomatoes;
      }
    });

    // Calculate Avg Ratings
    var avgImdb = [0, 0, 0, 0];
    var avgTomato = [0, 0, 0, 0];

    for (var i = 0; i < 4; i++) {
      avgImdb[i] = (imdb[i] / yMovies[i]).toPrecision(2);
      avgTomato[i] = (tomatoes[i] / yMovies[i]).toPrecision(2);
    };

    // Loop Through Shows
    showData.forEach(function(data) {
      if (data.netflix) {
          yShows[0]+=1;
      }
      if (data.hulu) {
          yShows[1]+=1;
      }
      if (data.prime) {
          yShows[2]+=1;
      }
      if (data.disney) {
          yShows[3]+=1;
        }
    });

    // Build Avg Display
    d3.select("#ratingNetflix").selectAll(".card-text").html(`Avg IMDB:  ${avgImdb[0]}<br/>Avg Rotten Tomatoes: ${avgTomato[0]}%`)
    d3.select("#ratingHulu").selectAll("p").html(`Avg IMDB:  ${avgImdb[1]}<br/>Avg Rotten Tomatoes: ${avgTomato[1]}%`)
    d3.select("#ratingPrime").selectAll("p").html(`Avg IMDB:  ${avgImdb[2]}<br/>Avg Rotten Tomatoes: ${avgTomato[2]}%`)
    d3.select("#ratingDisney").selectAll("p").html(`Avg IMDB:  ${avgImdb[3]}<br/>Avg Rotten Tomatoes: ${avgTomato[3]}%`)

    // Build Title Count Plot
    var trace1 = {
      x: xAxis,
      y: yMovies,
      name: "Movies",
      marker:{
        color: ["#E50914", "#1DB954", "#FF9900", "#333399"]
      },
      type: "bar"
    };

    var trace2 = {
      x: xAxis,
      y: yShows,
      name: "Shows",
      marker:{
        color: ["#B70710", "#179443", "#CC7A00", "#28287A"]
      },
      type: "bar"
    };
      
    var data = [trace1, trace2];
    
    var layout = {
      title: "# of Movies and Shows by Service",
      barmode: "group",
      yaxis: {
        automargin: true
      }
    };
    
    Plotly.newPlot("titles", data, layout);

  }).catch(error => console.log(error));
}).catch(error => console.log(error));


