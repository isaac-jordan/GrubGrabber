var map;
var geocoder;
var service;
var infowindow;
var searchLocation;
var searchResults = [];

function initialize() {
  geocoder = new google.maps.Geocoder();
  var mapProp = {
    zoom:15,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}

function codeAddress(address) {
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var locationObject = results[0].geometry.location;
      searchLocation = locationObject;
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

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    var data = []; //Array of placeIDs
    results.forEach(function(result) {
        data.push(result["place_id"]);
    });
    $.ajax({
        type: "POST",
        url: "/sort_results/",
        data: {"data": data},
        success: function(sortedResults) {
            //SortedResults should be an array of indices (integers).
            //The indices correspond to the position of the place in results.
            sortedResults["resultArray"].forEach(function(result) {
                searchResults.push(results[result]);
            });
            //console.log(searchResults);
            setResult(searchResults.shift());
        },
        traditional: true,
        error: function(result) {
            console.log(result["responseText"]);
        },
    });

  }
}

function setResult(result) {
    $("#placeName").html(result["name"]);
    $("#placeLocation").html(result["vicinity"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#thisPlace").attr("href","/place/" + searchLocation + "/" + result["place_id"] + "/");
    $("#thisPlace").attr("data-place", result["place_id"]);
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

function getNextResult() {
  var result = searchResults.shift();
  if (result != undefined) {
    setResult(result);
  } else {
    alert("No more places.");
  }
}

$("#thisPlace").click(function() {
    var place = $("#thisPlace").attr("data-place");
    var name = $("#placeName").html();
    $.ajax({type:"post",
    url:"/add_like/",
    data: {"place":place, "name":name},
    success: function(result) {
        //console.log("Like added.");
    },
    error: function(error) {
        console.log(error["responseText"]);
    },
    });
})
