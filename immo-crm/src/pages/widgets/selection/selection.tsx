import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';

export default function CitySelection() {
    const [city, setCity] = React.useState('');

    const handleChange = (event: SelectChangeEvent) => {
        setCity(event.target.value as string);
    };

    return (
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
    );
}