$(function() {
    $("#birthdate").datepicker();
});

$("#birthdate").on("change", function() {
    var currentDate = $(".selector").datepicker("getDate");
    if (currentDate) this.name = getFullYear(currentDate);
});

var genreNames = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('description'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: {
        url: '/api/v1/genres',
        filter: function(list) {
        return $.map(list, function(val) {
            return { description: val }; });
        }
    }
});
genreNames.initialize();

$('#moviesandtvshowsgenre').tagsinput({
    typeaheadjs: {
        name: 'genreNames',
        displayKey: 'description',
        valueKey: 'description',
        source: genreNames.ttAdapter()
    }
});


var languageNames = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('description'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: {
        url: '/api/v1/languages',
        filter: function(list) {
        return $.map(list, function(val) {
            return { name: val }; });
        }
    }
});
languageNames.initialize();

$('#moviesandtvshowslanguage').tagsinput({
    typeaheadjs: {
        name: 'languageNames',
        displayKey: 'description',
        valueKey: 'description',
        source: languageNames.ttAdapter()
    }
});



var countryNames = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: {
        url: '/api/v1/countries',
        filter: function(list) {
        return $.map(list, function(val) {
            return { name: val }; });
        }
    }
});
countryNames.initialize();

$('#moviesandtvshowscountries').tagsinput({
    typeaheadjs: {
        name: 'countryNames',
        displayKey: 'name',
        valueKey: 'name',
        source: countryNames.ttAdapter()
    }
});

