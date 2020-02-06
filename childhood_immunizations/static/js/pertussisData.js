var buffer = {};

d3.json("/static/js/vaccines.json")
    .then(
        d => {
            Object.entries(d.vaccine).forEach(e => {
                buffer[e[1].State] = {
                    value: e[1]["Pertussis cases (2018)"],
                    href: "#",
                    tooltip: { content: `<span style="font-weight:bold;">${e[1].State}</span><br />Pertussis Incidents : ${e[1]["Pertussis cases (2018)"]}` }
                };
            });
        }
    ).then(
        () => {
            $(".pecontainer").mapael({
                map: {
                    // Set the name of the map to display
                    name: "usa_states",
                    defaultArea: {
                        attrs: {
                            stroke: "#fff",
                            "stroke-width": 1
                        },
                        attrsHover: {
                            "stroke-width": 2
                        }
                    }
                },
                legend: {
                    area: {
                        title: "Pertussis incidents per state (2018)",
                        slices: [
                            {
                                min: 1,
                                max: 49,
                                attrs: {
                                    fill: "#87bd7a"
                                },
                                label: "1-49"
                            },
                            {
                                min: 50,
                                max: 99,
                                attrs: {
                                    fill: "#EADB7C"
                                },
                                label: "50-99"
                            },
                            {
                                min: 100,
                                max: 299,
                                attrs: {
                                    fill: "#F7B438"
                                },
                                label: "100-290"
                            },
                            {
                                min: 300,
                                max: 499,
                                attrs: {
                                    fill: "#D87613"
                                },
                                label: "300-499"
                            },
                            {
                                min: 500,
                                max: 999,
                                attrs: {
                                    fill: "#A34522"
                                },
                                label: "500-999"
                            },
                            {
                                min: 1000,
                                attrs: {
                                    fill: "#000000"
                                },
                                label: "1000+"
                            }
                        ]
                    }
                },
                areas: buffer
            });
        }
    );