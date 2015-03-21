var map;
function initialize(PLACE_ID) {
  map = new google.maps.Map(document.getElementById('googleMap'), {
    center: new google.maps.LatLng(-33.8665433, 151.1956316),
    zoom: 15
  });

  var request = {
    placeId: PLACE_ID,
  };

  var infowindow = new google.maps.InfoWindow();
  var service = new google.maps.places.PlacesService(map);

  service.getDetails(request, function(place, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
      setResult(place);
      var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
      });
    }
  });
}
