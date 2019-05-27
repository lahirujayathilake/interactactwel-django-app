<template>
    <div>
        <div class="chart_container"></div>
    </div>
</template>

<script>
    import * as d3 from "d3";

    export default {
        name: "pathways-graph",
        data() {
            return {
                w: 700,
                h: 300,
                pathid: 0,
                margin: {
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
                Times_map: {
                    "0": "2001",
                    "1": "2002",
                    "2": "2003",
                    "3": "2004",
                    "4": "2005",
                    "5": "2006",
                    "6": "2007",
                    "7": "2008",
                    "8": "2009",
                    "9": "2010"
                },
                colorIndex: 0,
                xList: [],
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
            computedTimes() {
                return Object.keys(this.Times_map).map(key => {
                    return {
                        key: key,
                        value: this.Times_map[key]
                    };
                });
            },

            yScale() {
                return d3
                    .scaleBand()
                    .domain(this.computedActions.map(d => d.value))
                    .rangeRound([-14, this.h-45]);
            },

            xScale() {
                return d3
                    .scaleBand()
                    //.domain([1993, 2018])
                    .domain(this.computedTimes.map(d =>d.value))
                    .rangeRound([0, this.w - 200]);
            }
        },
        methods: {
            nextPathId() {
                this.pathid++;
                return "path" + this.pathid;
            },
            xListComputed(v) {
                return this.xList.push(v);
            },
            generatePath(pathY_points) {
                let nextX = 0;
                let previousY;
                this.xListComputed(nextX);
                const pathPointsArray = [];
                const a = pathY_points.map(element => parseInt(element) * 22);
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
                d3.select("svg").remove();
                const svg = d3
                    .select(".chart_container")
                    .append("svg")
                    .attr("width", this.w)
                    .attr("height", this.h);
                //   svg.selectAll("*").remove();
                const g = svg
                    .append("g")
                    .attr("transform", "translate(" + 200 + "," + 10 + ")")
                    .call(d3.axisLeft(this.yScale));

                const gx = svg
                    .append("g")
                    .attr("transform", "translate(" + 200 + "," + 265 + ")")
                    .call(d3.axisBottom(this.xScale).tickFormat(d3.format("d")))

                g.selectAll('line-x').on('mouseenter', function() {
                    if (this !== d3.select('line-x:last-child').node()) {
                        this.parentElement.appendChild(this);
                        d3.select(this)
                            .transition()
                            .duration(200)
                            .attr('r', 55)
                            .transition()
                            .ease('elastic')
                            .attr('r', 50);
                    }
                });

                g.selectAll("line-x")
                    .data(this.data)
                    .enter()
                    .append("path")
                    .attr("id", data => this.nextPathId())
                    .attr("d", data => this.generatePath(data.value))
                    .on("mouseover", (d, i, n) => {

                        d3.select("#" + n[i].id).style("stroke-width", 8);
                        d3.select("#" + n[i].id).raise();

                        svg.selectAll("path").sort(function(a, b) {
                            // select the parent and sort the path's
                            if (a !== null && a.id != n[i].id) return -1;
                            // a is not the hovered element, send "a" to the back
                            else if (a != null) return 1; // a is the hovered element, bring "a" to the front
                        });

                        const pathsArray = [...svg.selectAll("path")._groups[0]];
                        const index = pathsArray.findIndex(p => {
                            return p.id === n[i].id;
                        });
                    })
                    .on("mouseout", (d, i, n) => {
                        d3.select("#" + n[i].id).style("stroke-width", 4);
                    })
                    .style("fill", "none")
                    .style("stroke", data => this.getPathColor(data.key))
                    .style("stroke-width", 4);

                g.selectAll("line-y")
                    .data(this.xList)
                    .enter()
                    .append("line")
                    .attr("stroke-dasharray", "5,5")
                    .style("stroke", "#d3d3d326")
                    .attr("x1", d => d)
                    .attr("y1", -10)
                    .attr("x2", d => d)
                    .attr("y2", this.h - 30);
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
    .dummy {
    }
</style>
