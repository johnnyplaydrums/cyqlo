function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.774022, lng: -73.970599},
    zoom: 12
  });
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

      //infoWindow.setPosition(pos);
      //infoWindow.setContent('Current Location');
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
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(control);

  button.addEventListener("click", function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
    directionsDisplay.setPanel(document.getElementById('right-panel'));
  });

  document.getElementById('submit').addEventListener('click', function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}


function calculateAndDisplayRoute(directionsService, directionsDisplay) {

  navigator.geolocation.getCurrentPosition(function(position) {
    var pos = { lat: position.coords.latitude, lng: position.coords.longitude };

    var waypts = [];
    var checkboxArray = document.getElementById('waypoints');
    for (var i = 0; i < checkboxArray.length; i++) {
      if (checkboxArray.options[i].selected) {
        waypts.push({
          location: checkboxArray[i].value,
          stopover: true
        });
        var end = i-1;
        var finaldestination = checkboxArray[end].value;
      }
    }
        directionsService.route({
          origin: {lat: position.coords.latitude, lng: position.coords.longitude},
          destination: finaldestination,
          waypoints:waypts,
          optimizeWaypoints:true,
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
