var map;
var geocoder;
var service;
var infowindow;
var paginationCache;
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
                position: locationObject,
                icon: '/static/img/marker-home.png',
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

function callback(results, status, pagination) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        paginationCache = pagination;
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
    //console.log(result);
    $("#placeName").html(result["name"]);
    $("#placeLocation").html(result["vicinity"]);
    $("#typeIcon").attr("src",result["icon"]);
    $("#thisPlace").attr("href","/place/" + searchLocation + "/" + result["place_id"] + "/");
    $("#placeName").attr("data-place", result["place_id"]);
    if (result["photos"] != undefined) {
        $("#placePhoto").attr("src",result["photos"][0].getUrl({'maxHeight': 150}));
    } else {
        $("#placePhoto").attr("src","http://placehold.it/329x150&text=Place Image");
    }
    $("#placeRating").html(result["rating"] != undefined ? result["rating"] : "No Ratings");
    $("#placeTypes").html("");
    for (var i=0;i<result["types"].length; i++) {
        $("#placeTypes").append(result["types"][i]);
        if (i < result["types"].length -1) {
            $("#placeTypes").append(", ");
        }
    }
    if (result["opening_hours"] != undefined) {
        if (result["opening_hours"]["open_now"] == true) {
            $("#placeOpen").html("Open!");
        } else {
            $("#placeOpen").html("Closed!");
        }
    } else {
        $("#placeOpen").html("Unknown.");
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
    if ($("#blacklist").hasClass("info")) {
      $("#blacklist").removeClass("info");
      $("#blacklistIcon").html("")
    }
    } else {
        if (paginationCache.hasNextPage) {
            paginationCache.nextPage();
        } else {
            alert("Sorry, we cannot get any more results. Please refresh to go back to the start, or try a different location.");
        }
    }
}

$("#thisPlace").click(function() {
    var place = $("#placeName").attr("data-place");
    var name = $("#placeName").html();
    $.ajax({
        type:"POST",
        url:"/add_like/",
        data: {"place":place, "name":name},
        success: function(result) {
            //console.log("Like added.");
        },
        error: function(error) {
            console.log(error["responseText"]);
        },
    });
});

$("#blacklist").click(function() {
    var place = $("#placeName").attr("data-place");
    var name = $("#placeName").html();
    $.ajax({
        type:"POST",
        url:"/add_blacklist/",
        data:{place:place, name:name},
        success:function(data) {
            if (data == "Added") {
                $("#blacklist").addClass("info");
                $("#blacklistIcon").html("<i class='fi-x'></i> ")
            } else if (data == "Removed") {
                $("#blacklist").removeClass("info");
                $("#blacklistIcon").html("")
            } else {
                console.log(data);
            }
        },
        error: function(result) {
            console.log(result["responseText"]);
        },
    });
});
