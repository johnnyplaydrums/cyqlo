function initMap() {

    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 40.774022,
            lng: -73.970599
        },
        zoom: 12
    });

    var markers = createMarkers(cityracks),
        mcStyles = [{
                url: "/static/img/blue1.png",
                width: 45,
                height: 46,
                textSize: 10,
                textColor: '#fff'
            },
            // { url: "/static/img/blue2.png", width: 55, height: 56, textSize: 11, textColor: '#fff' },
            // { url: "/static/img/blue3.png", width: 65, height: 66, textSize: 12, textColor: '#fff' }
        ],
        mcOptions = {
            gridSize: 81,
            batchSize: 5000,
            batchSizeIE: 400,
            styles: mcStyles
        },
        mc = new MarkerClusterer(map, markers, mcOptions);

    directionsDisplay.setMap(map);
    //var infoWindow = new google.maps.InfoWindow({map: map});

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            var im = 'http://www.robotwoods.com/dev/misc/bluecircle.png';
            // var im = '/static/img/currentlocation.png';
            var userMarker = new google.maps.Marker({
                position: pos,
                map: map,
                icon: im
            });

            map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }

    var button = document.getElementById("buttonid");
    var control = document.getElementById('floating-panel');
    control.style.display = 'block';
    button.addEventListener("click", function() {
        calculateAndDisplayRoute(directionsService, directionsDisplay);
        directionsDisplay.setPanel(document.getElementById('right-panel'));
    });

    calculateAndDisplayRoute(directionsService, directionsDisplay);

    var button = document.getElementById("gobutton");
    button.onclick = function() {
        var center = map.getCenter();
        window.open('http://bit.ly/2olqQVg');
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {

    navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        var waypts = [];
        var checkboxArray = document.getElementById('waypoints');

        //free api allows a max of 9 total stops including the start and end address
        //premier allows a total of 25 stops.
        // add start of route as first waypoint
        // items = [address1, address2]; so for a loop, we can gather couple waypoints along the route and generate a loop
        var items = ["40.768808, -73.979916", "40.780029, -73.964794", "40.769970, -73.971397", "40.795799, -73.953409", "40.797715, -73.954320"];
        for (var i = 0; i < items.length; i++) {
            var address = items[i];
            if (address !== "") {
                waypts.push({
                    location: address,
                    stopover: true
                });
            }
        }

        for (var i = 0; i < checkboxArray.length; i++) {
            if (checkboxArray.options[i].selected) {
                waypts.push({
                    location: checkboxArray[i].value,
                    stopover: true
                });
                var finaldestination = checkboxArray[i].value;
            }
        }
        directionsService.route({
            origin: {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            },
            // origin: {lat:40.7535965,lng:-73.9832326},
            destination: {
                lat: 40.768808,
                lng: -73.979916
            },
            // destination: finaldestination,
            waypoints: waypts,
            optimizeWaypoints: true,
            travelMode: 'BICYCLING'
        }, function(response, status) {
            if (status === 'OK') {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });
    })
}

var infowindow;

function createMarkers(points) {
    var image = new google.maps.MarkerImage("/static/img/blue-dot.png",
            new google.maps.Size(16, 16), // size
            new google.maps.Point(0, 0), // origin
            new google.maps.Point(8, 7) // anchor
        ),
        shape = {
            coords: [5, 0, 24, 19],
            type: 'rect'
        },
        i = points.length - 1,
        point,
        markers = [];
    do {
        point = points[i];
        latlng = new google.maps.LatLng(point[0], point[1]);
        var marker = new google.maps.Marker({
            position: latlng,
            icon: image,
            shape: shape,
            title: point[2]
        });

        var content = '<strong>' + point[2] + '</strong><br>';
        // infowindow
        if (point[3] == 1) {
            content = content + 'one rack';
        } else {
            content = content + point[3] + ' racks';
        }
        makeInfowindow(marker, content);
        markers.push(marker);
    } while (--i >= 0);
    return markers;
};

function makeInfowindow(marker, content) {
    google.maps.event.addListener(marker, 'click', function() {
        if (infowindow) {
            infowindow.close();
        }
        infowindow = new google.maps.InfoWindow({
            content: content
        });
        infowindow.open(marker.get('map'), this);
    });
}
