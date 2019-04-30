<template>
  <div>
    <div class="chart_container"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "MyChart",
  data() {
    return {
      w: 1500,
      h: 460,
      margin: {
        top: 50,
        right: 20,
        bottom: 30,
        left: 40
      },
        padding:{
            top: 20,
            right: 20,
            bottom: 30,
            left: 40
        },
      pathColors: [
          "#0176b8",
          "#7b549c",
          "#c73431",
          "#d2701b",
          "#219b9f",
          "#d2a02f",
          "#dc4b8a",
          "#6ba629",
          "#737478"
      ],

        pathColors0:[
            "#9cdbf1",
            "#f2e3ee",
            "#ffe2d3",
            "#ffebb5",
            "#d4ebea",
            "#f9f0b8",
            "#",
            "#",
            "#",
        ],

      colorIndex: 0,
      xList: ["0", "200", "300"],
      visibleKeyList: ["1"],
      jk: ""
    };
  },
  computed: {
    computedActions() {
      return Object.keys(this.actions).map(key => {
        return {
          key: key,
          value: this.actions[key]
        };
      });
    },
    yScale() {
      return d3
        .scaleBand()
        .domain(this.computedActions.map(d => d.value))
        .rangeRound([0, this.h]);
    },
      xScale() {
          return d3
              .scaleLinear()
              .domain([2000, 2018])
              .rangeRound([0, this.w - 1000]);
      }
  },
  methods: {
    xListComputed(v) {
      return this.xList.push(v);
    },
    generatePath(pathY_points) {
      let nextX = 0;
      let previousY;
      this.xListComputed(nextX);
      const pathPointsArray = [];
      const a = pathY_points.map(element => parseInt(element) * 40);
      a.forEach((y, i) => {
        if (i === 0) {
          previousY = y;
        }
        if (y !== previousY) {
          pathPointsArray.push(nextX - 20);
          pathPointsArray.push(y);
        }
        pathPointsArray.push(nextX);
        pathPointsArray.push(y);
        previousY = y;
        nextX += 20;
        this.xListComputed(nextX);
        pathPointsArray.push(nextX);
        pathPointsArray.push(y);
        nextX += 20;
        this.xListComputed(nextX);
      });
      let path = "";
      pathPointsArray.forEach((point, index) => {
        if (index === 0) {
          path += "M";
          path += point;
          path += " ";
        } else if (index === 1) {
          path += point;
          path += " ";
        } else {
          if (index % 2 === 0) {
            path += "L";
            path += point;
            path += " ";
          } else {
            path += point;
            path += " ";
          }
        }
      });

      return path;
    },
    getPathColor(key) {
      const color = this.pathColors[key];
      return color;
    },

    drawChart() {
      //console.log(this.data);
      d3.select("svg").remove();
      const svg = d3
        .select(".chart_container")
        .append("svg")
        .attr("width", this.w)
        .attr("height", this.h);
      //   svg.selectAll("*").remove();
      const g = svg
        .append("g")
        .attr("transform", "translate(" + 200 + "," + 0 + ")")
        .call(d3.axisLeft(this.yScale))

        const gx = svg
            .append("g")
            .attr("transform", "translate(" + 200 + "," + 440 + ")")
            .call(d3.axisBottom(this.xScale))

      g.selectAll("line-x")
        .data(this.data)
        .enter()
        .append("path")
        .attr("d", data => this.generatePath(data.value))
        .style("fill", "none")
        .style("stroke", data => this.getPathColor(data.key))
        .style("stroke-width", 4);

      gx.selectAll("line-y")
        .data(this.xList)
        .enter()
        .append("line")
        .attr("stroke-dasharray", "5,5")
        .style("stroke", "#f1f1f1")
        .attr("x1", d => d)
        .attr("y1", -10)
        .attr("x2", d => d)
        .attr("y2", this.h);
    }
  },
  mounted() {
    this.drawChart();
  },
  updated() {
    this.drawChart();
  },
  watch: {
    data() {
      this.drawChart();
    }
  },
  props: ["data", "actions"]
};
</script>


<style scoped>
</style>
