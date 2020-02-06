var buffer = {};

d3.json("/static/js/vaccines.json")
    .then(
        d => {
            Object.entries(d.vaccine).forEach(e => {
                buffer[e[1].State] = {
                    value: e[1]["Measles cases (2019)"],
                    href: "#",
                    tooltip: { content: `<span style="font-weight:bold;">${e[1].State}</span><br />Measles Incidents : ${e[1]["Measles cases (2019)"]}` }
                };
            });
        }
    ).then(
        () => {
            $(".mecontainer").mapael({
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
                        title: "Measles incidents per state (2019)",
                        slices: [
                            {
                                max: 0,
                                attrs: {
                                    fill: "#87bd7a"
                                },
                                label: "0"
                            },
                            {
                                min: 1,
                                max: 9,
                                attrs: {
                                    fill: "#EADB7C"
                                },
                                label: "1-9"
                            },
                            {
                                min: 10,
                                max: 29,
                                attrs: {
                                    fill: "#F7B438"
                                },
                                label: "10-29"
                            },
                            {
                                min: 30,
                                max: 99,
                                attrs: {
                                    fill: "#A34522"
                                },
                                label: "30-99"
                            },
                            {
                                min: 101,
                                attrs: {
                                    fill: "#000000"
                                },
                                label: "100+"
                            }
                        ]
                    }
                },
                areas: buffer
            });
        }
    );