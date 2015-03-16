var map;
var geocoder;
var service;
var infowindow;
var searchLocation;
var searchResults;
var placeName;

function callback(result, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    console.log(result);
    $("#placeName").append(result["name"]);
    $("#placeLocation").append(result["formatted_address"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#placeRating").append(result["rating"]);
    $("#placeWebsite").append(result["website"]);
    $("#placeWebsite").attr("href", result["website"]);
    result["reviews"].forEach(function(review) {
        var html = "<div class='review'>";
        html += review["author_name"];
        html += "<br>";
        html += review["text"];
        html += "</div>";
        $("#placeReviews").append(html);
    });
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
    new google.maps.Marker({
      map: map,
      position: result["geometry"]["location"]
    });
  }
}

function initialize(PLACE_ID) {
  var mapProp = {
    zoom:15,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };

  map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

  var request = {
    placeId: PLACE_ID,
  };

  infowindow = new google.maps.InfoWindow();
  service = new google.maps.places.PlacesService(map);
  service.getDetails(request, callback);
}
