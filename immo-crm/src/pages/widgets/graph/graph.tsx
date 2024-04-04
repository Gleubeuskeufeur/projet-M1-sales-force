import React from "react";

import { Chart } from "react-google-charts";

interface CityProp {
    city: string
}

export const dataLille = [
    ["Year", "Land Price", "Loan Interest"],
    ["2004", 1000, 400],
    ["2005", 1170, 460],
    ["2006", 660, 1120],
    ["2007", 1030, 540],
];

export const dataLyon = [
    ["Year", "Land Price", "Loan Interest"],
    ["2004", 1200, 800],
    ["2005", 1170, 960],
    ["2006", 1660, 1120],
    ["2007", 2030, 540],
];

export const dataRennes = [
    ["Year", "Land Price", "Loan Interest"],
    ["2004", 300, 400],
    ["2005", 170, 760],
    ["2006", 1660, 820],
    ["2007", 1030, 740],
];

export function Graph(props: CityProp) {
    //const [data, setData] = React.useState([])
    const getDataByCity = (city: string) => {
        switch (city) {
            case "Lille":
                return dataLille;
            case "Lyon":
                return dataLyon;
            case "Rennes":
                return dataRennes;
            default:
                return dataLille;
        }
    }

    return (
        <Chart
            chartType="LineChart"
            width="100%"
            height="80vh"
            data={getDataByCity(props.city)}
            options={{
                title: `Real Estate Price Evolution in ${props.city}`,
                curveType: "function",
                legend: { position: "bottom" },
            }}
        />
    );
}

export default Graph;