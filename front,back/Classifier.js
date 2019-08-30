function classifyData(data,inputChoice) {
    let classifiedData = {
        'chartStandard': filterStandardMap.get(inputChoice['filter_standard']),
        'chartColumnNames': new Array(),
        'chartValues': new Array(),
    };
    for (let [indexName,indexValues] of Object.entries(data)) {
        indexValues.unshift(indexName);
        classifiedData['chartValues'].push(indexValues);
        classifiedData['chartColumnNames'].push(indexName);
    }
    return classifiedData;
};

function classifyChartTypeNames(data) {
    let barGroups = new Array();
    for (let chartName of Object.keys(data)) {
        if (chartName.includes('condition') || chartName == 'x_axis_labels') {
            continue;
        }
        else {
            barGroups.push(chartName)
        }
    };
    let barGroupArray = new Array();
    barGroupArray.push(barGroups);
    return barGroupArray;
}

