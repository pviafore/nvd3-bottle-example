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
            .x((d) => d.x)
            .y((d) => d.y)

        chart.xAxis.axisLabel('Time in Seconds')
        chart.yAxis.axisLabel('Distance From Origin')

        d3.select('#my-custom-graph') //Select the <svg> element you want to render the chart in.   
            .datum([data]) //Populate the <svg> element with chart data...
            .call(chart); //Finally, render the chart!
    });





}