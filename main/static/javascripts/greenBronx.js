function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'));
  directionsDisplay.setMap(map);

  var button = document.getElementById("buttonid");
  var control = document.getElementById('floating-panel');
  control.style.display = 'block';
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(control);

  button.addEventListener("click", function() {
  directionsDisplay.setPanel(document.getElementById('right-panel'));
  });

  calculateAndDisplayRoute(directionsService, directionsDisplay);
  document.getElementById('submit').addEventListener('click', function() {
  calculateAndDisplayRoute(directionsService, directionsDisplay);
  });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
  var waypts = [];
  var checkboxArray = document.getElementById('waypoints');
  for (var i = 0; i < checkboxArray.length; i++) {
    if (checkboxArray.options[i].selected) {
      waypts.push({
        location: checkboxArray[i].value,
        stopover: true
      });
    }
  }

    directionsService.route({
    origin: {lat:40.89, lng:-73.896389},
    destination: {lat:40.89, lng:-73.896389},
    waypoints:waypts,
    optimizeWaypoints:true,
    travelMode:'BICYCLING'


  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    }
     else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}
