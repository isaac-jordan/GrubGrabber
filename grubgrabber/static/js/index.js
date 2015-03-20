function initialise() {
    var input = document.getElementById('mainSearch');
    var autocomplete = new google.maps.places.Autocomplete(input);
}

google.maps.event.addDomListener(window, 'load', initialise);
alert();
