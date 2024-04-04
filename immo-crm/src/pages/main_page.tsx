import React from "react";
import Graph from "./widgets/graph/graph";
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';

function MainPage() {
    const [city, setCity] = React.useState('Lille');

    const handleChange = (event: SelectChangeEvent) => {
        setCity(event.target.value as string);
    };
    return (
        <div className="Graph">
            <Box sx={{ minWidth: 120 }}>
                <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-label">City</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={city}
                        label="Age"
                        onChange={handleChange}
                    >
                        <MenuItem value={"Lille"}>Lille</MenuItem>
                        <MenuItem value={"Lyon"}>Lyon</MenuItem>
                        <MenuItem value={"Rennes"}>Rennes</MenuItem>
                    </Select>
                </FormControl>
            </Box>
            <br />
            <Graph city={city} />
        </div>
    );
}

export default MainPage;