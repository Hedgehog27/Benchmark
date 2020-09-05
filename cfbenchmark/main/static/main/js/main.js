let tmp = {
  x: "",
  y: "",
};

var c = 0;
var colorList = [
  "#4B0082",
  "#FFFF00",
  "#B22222",
  "#ffd3e1",
  "#303960",
  "#FFD700"
];

let userGraph = [], userList = [];

function loadDetail(username1, username2) {
  userList.push(username1);
  userList.push(username2);
  for (j = 0; j < 2; j++) {
    if (userList[j] != "") {
      loadDataForUser(userList[j]);
    } else {
      alert("Please enter correct username/handle. ");
    }
  }
}

function loadDataForUser(username) {
  let dataArr = [];
  // const xmlreq = new XMLHttpRequest();
  const urlcf = "https://codeforces.com/api/user.rating?handle=" + username;

  axios.get(urlcf)
  .then(function (response) {
    // handle success
    const data = response.data.result
    for (i = 1; i <= data.length; i++) {
      var date = new Date(
        data[i - 1].ratingUpdateTimeSeconds * 1000
      );
      dataArr.push({ x: date, y: data[i - 1].newRating });
    }
  })
  .catch(function (error) {
    // handle error
    alert("" + username + " did not take part in any contest.");
  })
  .then(function () {
    // always executed
    // addDataToGraph()
    userGraph.push({
      color: colorList[c],
      type: "line",
      showInLegend: true,
      legendText: username,
      indexLabelFontSize: 15,
      dataPoints: dataArr,
    })
    c++;
    if (userGraph.length === userList.length) {
      let graph = getGraph(userGraph);
      graph.render()
    }
  });
}

// function addDataToGraph(graphStats) {
//   graph.options.data.push(graphStats);
//   c++;
// }

function getGraph(dataArr) {
  let graph = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    axisX: {
      labelFontSize: 20,
      labelFontStyle: "arial",
    },
    axisY: {
      labelFontSize: 16,
      labelFontStyle: "arial",
      gridThickness: 0,
      stripLines: [
        {
          startValue: 0,
          endValue: 1200,
          color: "#B8B8B8",
        },
        {
          startValue: 1200,
          endValue: 1400,
          color: "#3be13b",
        },
        {
          startValue: 1400,
          endValue: 1600,
          color: "#00FFFF",
        },
        {
          startValue: 1600,
          endValue: 1900,
          color: "#b494ff",
        },
        {
          startValue: 1900,
          endValue: 2100,
          color: "#ff4bff ",
        },
        {
          startValue: 2100,
          endValue: 2300,
          color: "#ffd082",
        },
        {
          startValue: 2300,
          endValue: 2400,
          color: "#ffbf4c",
        },
        {
          startValue: 2400,
          endValue: 2600,
          color: "#ff6471",
        },
        {
          startValue: 2600,
          endValue: 3000,
          color: "#ff0024",
        },
        {
          startValue: 3000,
          endValue: 5000,
          color: "#af0000",
        },
      ],
      includeZero: false,
    },
    title: {
      text: "Rating Graph",
      fontFamily: "arial",
      fontSize: 25,
      fontWeight: "italic",
    },
    legend: {
      fontFamily: "arial",
    },
    data: dataArr,
  });
  return graph;
}
