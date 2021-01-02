import React from 'react'

// Define variables
const seasonConfig = {
    Summer: {
        text: 'It is hot',
        iconName: 'sun'
    },
    Winter: {
        text: 'It is cold',
        iconName: 'snowflake'
    }
};
// Halla estacion depende latitud
const getSeason = (lat, month) => {
    if (month>2 && month<9) {
        return lat > 0 ? 'Summer':'Winter';
    }else{
        return lat > 0 ? 'Winter':'Summer';
    }
};
// muestra en pantalla
const SeasonDisplay = (props) => {

    const season = getSeason(props.lat, new Date().getMonth());
    const { text, iconName } = seasonConfig[season]
 
    return (
        <div>
            <i className={`massive ${iconName} icon`} />
            <h1>{text}</h1>
            <i className={`massive ${iconName} icon`} />
        </div>
        );
};

// Export line
export default SeasonDisplay;