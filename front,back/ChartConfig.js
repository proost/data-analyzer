function setChartTypes(data) {
    let chartType = new Object();
    Object.keys(data).forEach((chartName) => {
        if (chartName.includes('condition')) {
            chartType[chartName] = 'area-spline';
        }
        else {
            chartType[chartName] = 'bar';
        }
    });
    return chartType;
};

function setY2Axes(data) {
    let yAxesOption = new Object();
    Object.keys(data).forEach((chartName) => {
        if (chartName.includes('condition')) {
            yAxesOption[chartName] = 'y2';
        }
        else {
            yAxesOption[chartName] = 'y';
        }
    });
    return yAxesOption;
};

function setY2AxesLabel(outputStandard) {
    let outputStandardValue = outputStandardMap.get(outputStandard);
    return outputStandardValue + 'condition';
};

function setChartNames(data,filterStandard) {
    let chartNames = new Object();
    Object.keys(data).forEach((chartName) => {
        if (filterStandard == '') {
            chartNames[chartName] = chartName;
        }
        else {
            chartNames[chartName] = filterStandardMap.get(filterStandard) + " : " + chartName;
        }
    });
    return chartNames;
};

function setXaxisType = () => ('category');

<<<<<<< HEAD
function setBarWidth = () =>  ( {ratio: 'some int'} );

function setChartSize = () => ( {height: 'some int', width: 'some int'} );

function setLegend = () => ( {position: 'bottom'} );

function setChartPadding = () => ( {bottom: 'some int'} );
=======
function setBarWidth = () =>  ( {ratio: 0.2} );

function setChartSize = () => ( {height: 550, width: 1380} );

function setLegend = () => ( {position: 'bottom'} );

function setChartPadding = () => ( {bottom: 25} );
>>>>>>> 789cb97... data analyzer for web

