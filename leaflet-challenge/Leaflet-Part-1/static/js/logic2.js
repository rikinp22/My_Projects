// Create the Earthquake Visualization

var queryURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Using Leaflet, create a map that plots all the earthquakes from your dataset based on their longitude and latitude.

// Create the map
var myMap = L.map("map", {
    center: [47.13, -94.53],
    zoom: 5
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Hint: The depth of the earth can be found as the third coordinate for each earthquake.

// Perform a request to query the URL
d3.json(queryURL).then(function (data) {
    function mapStyle(feature) {
        return {
            opacity: 1,
            fillOpacity: 1,
            fillColor: mapColor(feature.geometry.coordinates[2]),
            color: "blue",
            radius: mapRadius(feature.properties.mag),
            stroke: true,
            weight: 0.5
        };
    }

    // Your data markers should reflect the magnitude of the earthquake by their size and the depth of the earthquake by color. Earthquakes with higher magnitudes should appear larger, and earthquakes with greater depth should appear darker in color.
    function mapColor(depth) {
        switch (true) {
            case depth > 90:
                return "255-255-204";
            case depth > 70:
                return "51-204-255";
            case depth > 50:
                return "255-153-0";
            case depth > 30:
                return "255-51-51";
            case depth > 0:
                return "green";
        }
    }

    function mapRadius(mag) {
        if (mag === 0) {
            return ;
        }
        return mag * 5;
    }

    // Add earthquake data to the map
    L.geoJson(data, {

        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng);
        },

        style: mapStyle,

        // Include popups that provide additional information about the earthquake when its associated marker is clicked.
        onEachFeature: function (feature, layer) {
            layer.bindPopup("Magnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place + "<br>Depth: " + feature.geometry.coordinates[2]);

        }
    }).addTo(myMap);

// Create a legend that will provide context for your map data.
var legend = L.control({position: "bottomright"});
legend.onAdd = function() {
  var div = L.DomUtil.create("div", "info legend"),
  depth = [-10, 10, 30, 50, 70, 90];

  for (var i = 0; i < depth.length; i++) {
    div.innerHTML +=
    '<i style="background:' + mapColor(depth[i] + 1) + '"></i> ' + depth[i] + (depth[i + 1] ? '&ndash;' + depth[i + 1] + '<br>' : '+');
  }
  return div;
};
legend.addTo(myMap)
});