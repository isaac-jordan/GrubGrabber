var map;
var geocoder;
var service;
var infowindow;
var searchLocation;
var searchResults;

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    console.log(results);
    searchResults = results;
    var html;
    var result = searchResults.shift();
    $("#placeName").append(result["name"]);
    $("#placeLocation").append(result["vicinity"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#thisPlace").attr("href","/place/" + result["place_id"] + "/");
    if (result["photos"] != undefined) {
      $("#placePhoto").attr("src",result["photos"][0].getUrl({'maxHeight': 150}));
    } else {
      $("#placePhoto").attr("src","http://placehold.it/329x150&text=Place Image");
    }
    new google.maps.Marker({
      map: map,
      position: result["geometry"]["location"]
    });

  }
}

function getNextResult() {
  var result = searchResults.shift();
  if (result != undefined) {
    $("#placeName").html(result["name"]);
    $("#placeLocation").html(result["vicinity"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#thisPlace").attr("href","/place/" + result["place_id"] + "/");
    if (result["photos"] != undefined) {
      $("#placePhoto").attr("src",result["photos"][0].getUrl({'maxHeight': 150}));
    } else {
      $("#placePhoto").attr("src","http://placehold.it/329x150&text=Place Image");
    }
    new google.maps.Marker({
      map: map,
      position: result["geometry"]["location"]
    });
  } else {
    alert("No more places.");
  }
}

function codeAddress(address) {
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var locationObject = results[0].geometry.location;
      map.setCenter(locationObject);
      var marker = new google.maps.Marker({
        map: map,
        position: locationObject
      });
      var request = {
        location: locationObject,
        rankBy: google.maps.places.RankBy.DISTANCE,
        types: ['bakery','cafe','food','meal_takeaway','restaurant']
      };

      service = new google.maps.places.PlacesService(map);
      service.nearbySearch(request, callback);
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

function initialize() {
  geocoder = new google.maps.Geocoder();
  var mapProp = {
    zoom:15,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}

function getCoords(searchParam) {
  $.ajax("https://maps.googleapis.com/maps/api/geocode/json", {
    data: {address: searchParam},
    success: function (data) {
      searchPlaces(data["results"][0]["geometry"]["location"]);
    },
    async:false,
  });
}

initialize();
