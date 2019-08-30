function mangleData(data,inputChoice) {
    let renamedDateTime = renameDateTime(data,inputChoice['output_range_end_datetime']);
    let removedNotSet = renameNotSetInFilterValue(renamedDateTime);
    let renamedSumCum = renameSumCumName(removedNotSet);
    let removedAccumulation = renameAccumulation(renamedSumCum);
    let namedChartData = renameChartName(removedAccumulation,inputChoice['filter_standard']);
    return namedChartData;
};

function renameDateTime(data,output_range_end_time) {
    let newDate = data['x_axis_labels'].map((datetime) => {
        if (datetime == 'condition') {
            let date = output_range_end_time.substring(2,10);
            date = date.replace(/-/gi,'.')
            let time = output_range_end_time.substring(11,16);
            return date + ' ' + time;
        }
        else {
            let date = datetime.substring(2,10);
            date = date.replace(/-/gi,'.')
            let time = datetime.substring(11,16);
            return date + ' ' + time;
        }
    });
    data['x_axis_labels'] = newDate;
    return data;
};

function renameNotSetInFilterValue(data) {
    let newData = Object.assign({},data);
    Object.keys(data).forEach((columnName) => {
        if (columnName.includes('condition1')) {
            let filterValue = filterValueMap.get('condition1');
            let newName = columnName.replace('condition1',filterValue);
            newData = renameData(newData,newName,columnName);
        }
        else{
            if (columnName.includes('condition2')) {
                let filterValue = filterValueMap.get('condition2');
                let newName = columnName.replace('condition2',filterValue);
                newData = renameData(newData,newName,columnName);
            }
        }
    });
    return newData;
};

function renameSumCumName(data) {
    let newData = Object.assign({},data);
    Object.keys(data).forEach((columnName) => {
        if (columnName.includes('condition1')) {
            let filterValue = filterValueMap.get('condition1');
            let newName = columnName.replace('condition1',filterValue);
            newData = renameData(newData,newName,columnName);
        }
    });
    return newData;
};

function renameAccumulation(data) {
    let newData = Object.assign({},data);
    Object.keys(data).forEach((columnName) => {
        if (columnName.includes('condition2')) {
            let newName = columnName.replace('condition2','condition2 name');
            newData = renameData(newData,newName,columnName);
        }
    });
    return newData;
}

function renameChartName(data,filterStandard) {
    let newData = Object.assign({},data);
    Object.keys(data).forEach((columnName) => {
        if (filterValueMap.has(filterStandard)) {
            for (let filterValue of filterValueMap.get(filterStandard).keys()) {
                if (columnName.includes(filterValue)) {
                    let newName = columnName.replace(
                        filterValue,
                        filterValueMap.get(filterStandard).get(filterValue)
                    );
                    newData = renameData(newData,newName,columnName);                    
                }
            }
        }
    });
    return newData;
};

function renameData(data,newName,oldName) {
    Object.defineProperty(
        data, 
        newName, 
        Object.getOwnPropertyDescriptor(data,oldName)
    );
    delete data[oldName];
    return data;
};