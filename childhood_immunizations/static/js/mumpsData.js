var buffer = {};

d3.json("../vaccines.json")
    .then(
        d => {
            Object.entries(d.vaccine).forEach(e => {
                buffer[e[1].State] = {
                    value: e[1]["Mumps cases (2019)"],
                    href: "#",
                    tooltip: { content: `<span style="font-weight:bold;">${e[1].State}</span><br />Mumps Incidents : ${e[1]["Mumps cases (2019)"]}` }
                };
            });
        }
    ).then(
        () => {
            $(".mucontainer").mapael({
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
                        title: "Mumps incidents per state (2019)",
                        slices: [
                            {
                                sliceValue: "0",
                                attrs: {
                                    fill: "#87bd7a"
                                },
                                label: "0"
                            },
                            {
                                sliceValue: "1-2",
                                attrs: {
                                    fill: "#EADB7C"
                                },
                                label: "1-2"
                            },
                            {
                                sliceValue: "3-19",
                                attrs: {
                                    fill: "#F7B438"
                                },
                                label: "3-19"
                            },
                            {
                                sliceValue: "20-49",
                                attrs: {
                                    fill: "#D8A513"
                                },
                                label: "20-49"
                            },
                            {
                                sliceValue: "50-99",
                                attrs: {
                                    fill: "#D87613"
                                },
                                label: "50-99"
                            },
                            {
                                sliceValue: "100-299",
                                attrs: {
                                    fill: "#A34522"
                                },
                                label: "100-299"
                            },
                            {
                                sliceValue: "300+",
                                attrs: {
                                    fill: "#000000"
                                },
                                label: "300+"
                            }
                        ]
                    }
                },
                areas: buffer
            });
        }
    );