var geocoder;
function initialise() {
    geocoder = new google.maps.Geocoder();
    var input = document.getElementById('location');
    var autocomplete = new google.maps.places.Autocomplete(input);
}

$("#addLocation").click(function() {
    var address = $("#location").val();
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            var locationObject = "" + results[0].geometry.location;
            var name = results[0].formatted_address;
            $.ajax({
                type:"POST",
                url:"/add_location/",
                data:{"name":name, "geometry":locationObject},
                success: function(data) {
                    location.reload();
                },
                error: function(result) {
                    console.log(result["responseText"]);
                },
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });

});

$(".removeLoc").click(function() {
    var name = $(this).parent().prev().html();
    console.log(name);
    $.ajax({
        type:"POST",
        url:"/add_location/",
        data:{"name":name},
        success: function(data) {
            location.reload();
        },
        error: function(result) {
            console.log(result["responseText"]);
        },
    });
});

google.maps.event.addDomListener(window, 'load', initialise);
