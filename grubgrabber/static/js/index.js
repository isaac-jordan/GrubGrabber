function initialise() {
    var input = document.getElementById('mainSearch');
    var autocomplete = new google.maps.places.Autocomplete(input);
}

$(".locationItem").click(function() {
    var location = $(this).html();
    $.ajax({
        type:"POST",
        url:"/search/",
        data:{search:location},
        success:function(data) {
            document.write(data);
            var state = {
                "thisIsOnPopState": true
            };
            history.pushState(state, "GrubGrabber: Search", "/search/");
            expect(history.state).toEqual(state);
        },
        error: function(result) {
            console.log(result["responseText"]);
        },
    });
});

google.maps.event.addDomListener(window, 'load', initialise);
