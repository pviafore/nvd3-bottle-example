// A lot of this was grabbed from nvd3.js main webpage for line graph

window.onload = function() {
    d3.json("/data", drawGraph);
}

function drawGraph(data) {
    nv.addGraph(function() {
        var chart = nv.models.lineChart()
            .margin({ left: 100 }) //Adjust chart margins to give the x-axis some breathing room.
            .useInteractiveGuideline(true) //We want nice looking tooltips and a guideline!
            .showLegend(true) //Show the legend, allowing users to turn on/off line series.
            .showYAxis(true) //Show the y-axis
            .showXAxis(true) //Show the x-axis
            .x((d) => d.x + 10) //Grab x values out of the object
            .y((d) => d.y) //Grab y values out of hte object

        chart.xAxis.axisLabel('Time in Seconds')
        chart.yAxis.axisLabel('Distance From Origin')

        d3.select('#my-custom-graph') //Select the <svg> element you want to render the chart in by querying its id 
            .datum([data]) //Populate the graph (I put it in an array because nvd3 expects it because you can have multiple lines)
            .call(chart); //Finally, render the chart!
    });





}