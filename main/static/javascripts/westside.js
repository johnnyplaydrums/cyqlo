function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'));

  var markers = createMarkers(cityracks),
    mcStyles = [
      { url: "/static/img/blue1.png", width: 45, height: 46, textSize: 10, textColor: '#fff' },
      { url: "/static/img/blue2.png", width: 55, height: 56, textSize: 11, textColor: '#fff' },
      { url: "/static/img/blue3.png", width: 65, height: 66, textSize: 12, textColor: '#fff' }
    ],
    mcOptions = { gridSize: 81, batchSize: 5000, batchSizeIE: 400, styles: mcStyles },
    mc = new MarkerClusterer(map, markers, mcOptions);

  directionsDisplay.setMap(map);

  var button = document.getElementById("buttonid");
  var control = document.getElementById('floating-panel');
  control.style.display = 'block';
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(control);

  button.addEventListener("click", function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
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
    origin: {lat:40.703104, lng:-74.016847},
    destination: {lat: 40.850089, lng:-73.946785},
    waypoints: waypts,
    optimizeWaypoints: true,
    travelMode: 'BICYCLING'
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    }
    else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}

var infowindow;

function createMarkers(points) {
    var image = new google.maps.MarkerImage("/static/img/blue-dot.png",
      new google.maps.Size(16, 16), // size
      new google.maps.Point(0, 0), // origin
      new google.maps.Point(8, 7) // anchor
    ),
      shape = {coords: [5,0,24,19], type: 'rect'},
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
