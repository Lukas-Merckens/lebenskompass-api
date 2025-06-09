const { getHumanDesignData } = require('./hdkit.js');

const result = getHumanDesignData("02.12.1966", "22:54", "Vienna");
console.log(result);
const { generateChart } = require('./hdkit.js');

const chart = generateChart("02.12.1966", "22:54", "Vienna");
console.log(chart);

