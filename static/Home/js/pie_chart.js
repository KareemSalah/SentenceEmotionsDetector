window.onload = function() {
     var dps=[]; //dataPoints.
    var k =[];
    var g =[];
    var chart = new CanvasJS.Chart("chartContainer", {
        title: {
            text: "Accepting DataPoints from User Input"
        },
        data: [{
            type: "pie",
          showInLegend: true,
          dataPoints: dps
        },]
    });

    function addDataPointsAndRender() {
        dp = Number(document.getElementById("dp").value);
        kk = Number(document.getElementById("kk").value);
      gg = Number(document.getElementById("gg").value);
        dps.push({
               y:  dp

        });

        chart.render();
                dps.push({

               y: kk
        });
                chart.render();
                dps.push({

               y: gg
        });
                chart.render();
    }

    var renderButton = document.getElementById("renderButton");
    renderButton.addEventListener("click", addDataPointsAndRender);
}
