var buffer = {};

d3.json("../vaccines.json")
    .then(
        d => {
            Object.entries(d.vaccine).forEach(e => {
                buffer[e[1].State] = {
                    value: e[1]["Philosophical Exemption"],
                    href: "#",
                    tooltip: { content: `<span style="font-weight:bold;">${e[1].State}</span><br />Philosophical Exemptions : ${e[1]["Philosophical Exemption"]}` }
                };
            });
        }
    ).then(
        () => {
            $(".phcontainer").mapael({
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
                        title: "Philosophical Exemptions",
                        slices: [
                            {
                                sliceValue: "Yes",
                                attrs: {
                                    fill: "#A34522"
                                },
                                label: "Yes"
                            },
                            {
                                sliceValue: "No",
                                attrs: {
                                    fill: "#87bd7a"
                                },
                                label: "No"
                            }
                        ]
                    }
                },
                areas: buffer
            });
        }
    );