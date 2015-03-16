var map;
var geocoder;
var service;
var infowindow;
var searchLocation;
var searchResults;
var placeName;
var directionsDisplay;

function initialize(searchLatLng, PLACE_ID) {
    searchLocation = searchLatLng.match(/[-,\d,.]+/g);
    searchLocation[0] = parseFloat(searchLocation[0]);
    searchLocation[1] = parseFloat(searchLocation[1]);
    directionsDisplay = new google.maps.DirectionsRenderer();
    var mapProp = {
        zoom:18,
        mapTypeId:google.maps.MapTypeId.HYBRID
    };

    map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
    directionsDisplay.setMap(map);

    var request = {
        placeId: PLACE_ID,
    };

    infowindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);
    service.getDetails(request, callback);
}

function callback(result, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        console.log(result);
        setResult(result);
        new google.maps.Marker({
            map: map,
            position: new google.maps.LatLng(searchLocation[0], searchLocation[1]),
        });
        new google.maps.Marker({
            map: map,
            position: result["geometry"]["location"],
        });
        var directionsService = new google.maps.DirectionsService();
        var request = {
            origin: new google.maps.LatLng(searchLocation[0], searchLocation[1]),
            destination: result["geometry"]["location"],
            travelMode: google.maps.TravelMode.WALKING
        };
        directionsService.route(request, function(response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                console.log(response);
                directionsDisplay.setDirections(response);
            }
        });
    }
}

function setResult(result) {
    map.setCenter(result["geometry"]["location"]);
    $("#placeName").append(result["name"]);
    $("#placeLocation").append(result["formatted_address"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#placeRating").append(result["rating"]);
    $("#placeWebsite").append(result["website"]);
    $("#placeWebsite").attr("href", result["website"]);
    if (result["reviews"] != undefined) {
        result["reviews"].forEach(function(review) {
            var html = "<div class='review'>";
            html += review["author_name"];
            html += ": " + review["rating"];
            html += "<br>";
            html += review["text"];
            html += "</div>";
            $("#placeReviews").append(html);
        });
    }
    $('.placeReviews').slick({
        infinite: true,
        appendArrows: $("#placeReviewsButtons"),
        prevArrow: "<a class='slick-prev button small'>Previous</a>",
        nextArrow: "<a class='slick-next button small'>Next</a>",
    });
    result["types"].forEach( function(type) {
        $("#placeTypes").append(type + ", ");
    });
    if (result["photos"] != undefined) {
        $("#placePhoto").attr("src",result["photos"][0].getUrl({'maxHeight': 150}));
    } else {
        $("#placePhoto").attr("src","http://placehold.it/329x150&text=No Place Image");
    }
}
