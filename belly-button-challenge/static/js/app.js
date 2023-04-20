// Use the D3 library to read in samples.json from the URL https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json.

const url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";

d3.json(url).then(function(data) {
    console.log(data);
  });

// Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
function init() {

  let dropdownMenu = d3.select("#selDataset");

  d3.json(url).then((data) => {
    // Set a variable for the sample names
    let names = data.names;

    // Add samples to dropdown menu
    names.forEach((id) => {
    
      // Log the value of id for each iteration of the loop
      console.log(id);
    
        dropdownMenu.append("option")
        .text(id)
        .property("value",id);
    });
  // Use sample_values as the values for the bar chart.
        let sample_values = names[0];
        console.log(sample_values);

        // Build the Bar Chart
        buildMetadata(sample_values);
        buildBarChart(sample_values);
        buildBubbleChart(sample_values);
    });
};

function buildMetadata(sample) {
  d3.json(url).then(function(data) {
    let metadata = data.metadata;
    // Filter metadata to retrive sample
    let values = metadata.filter(result => result.id == sample);
    console.log(values)
    let value = values[0];

    // Clear metadata values
    d3.select("#sample-metadata").html("");
    // Use object values to add each value pair to data chart
    Object.entries(value).forEach(([key,value]) => {
      console.log(key, values);
      d3.select("#sample-metadata").append("h5").text(`${key}: ${value}`);

    });
  });
};

function buildBarChart(sample) {
  d3.json(url).then(function(data) {
    // Retrieve all sample data
    let sample_data = data.samples;
    // Filter data to retrieve each sample
    let value = sample_data.filter(result => result.id == sample);

    let samples = value[0];

    // Retrieve otu_ids, labels, and sample data for chart
    let otu_ids = samples.otu_ids;
    let otu_labels = samples.otu_labels;
    let sample_values = samples.sample_values;

    // Log data to console
    console.log(otu_ids, otu_labels, sample_values);
    // Find top 10 OTUs found in that individual in descending order
    let yticks = otu_ids.slice(0,10).map(id => `OTU ${id}`).reverse();
    let xticks = sample_values.slice(0,10).reverse();
    let labels = otu_labels.slice(0,10);

    // create trace to for the bar chart
    // Use otu_ids as the labels for the bar chart.
    // Use otu_labels as the hovertext for the chart.
    let trace = {
      x: xticks,
      y: yticks,
      labels: otu_ids,
      hovertext: otu_labels,
      type: "bar",
      orientation: "h"
    };
    // Plot the bar chart using plotly
    Plotly.newPlot("bar", [trace])

  });
};

// Create a bubble chart that displays each sample.

function buildBubbleChart(sample) {
  d3.json(url).then(function(data) {
    let sample_data = data.samples;
    let value = sample_data.filter(result => result.id == sample);

    let samples = value[0];

    let otu_ids = samples.otu_ids;
    let otu_labels = samples.otu_labels;
    let sample_values = samples.sample_values;

    console.log(otu_ids, otu_labels, sample_values);
    
  // Use otu_ids for the x values.
  // Use sample_values for the y values.
  // Use sample_values for the marker size.
  // Use otu_ids for the marker colors.
  // Use otu_labels for the text values.

    // Create trace for the bubble chart
    let trace1 = {
      x: otu_ids,
      y: sample_values,
      text: otu_labels,
      mode: "markers",
      marker: {
        size: sample_values,
        color: otu_ids,
      }
    };

    // Plot the bubble chart using Plotly
    Plotly.newPlot("bubble", [trace1])
  });
};

// Function that updates dashboard when sample is changed
function optionChanged(sample_data) { 

  // Log the new value
  console.log(sample_data); 

  // Call all functions 
  buildMetadata(sample_data);
  buildBarChart(sample_data);
  buildBubbleChart(sample_data);
};

// Call the initialize function
init();