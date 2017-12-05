Highcharts.setOptions({
    global: {
        useUTC: true
    },
    lang: {
        shortMonths: ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"],
        months: ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"],
        weekdays: ["Zondag", "Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag"],
    }
});

function initializeChart(receivedData) {
	now = (new Date()).getTime();
    Highcharts.chart('chart-container', {
        chart: {
            type: 'line',
            height: '30%',
            zoomType: 'x'
        },
        title: {
            text: ''
        },
        xAxis: {
            type: "datetime",
            labels: {
                enabled: true
            },
            min: 1504224000000
        },
        yAxis: [{
            title: {
                text: 'Peil (t.o.v. maaiveld)'
            },
            labels: {
                format: '{value} m'
            },
            min: -1,
            max: 0

        }, {
            gridLineWidth: 0,
            title: {
                text: 'Neerslag'
            },
            labels: {
                format: '{value} mm'
            },
            opposite: true,
            min: 0,
            max: 6

        }],
        legend: {
            enabled: true
        },
        tooltip: {
            shared: false,
            valueDecimals: 2
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Neerslag',
            type: 'column',
            data: receivedData,
            pointRange: 1 * 3600 * 1000,
            tooltip: {
                xDateFormat: ' ',
            	valueSuffix: " mm"
            },
            pointPadding: 0,
            groupPadding: 0,
            yAxis: 1,
        }]
    });
}

function loadPrecipitation(series_url) {
    $.ajax({
        url: series_url,
        datatype: "json",
        success: initializeChart
    });
}

seriesName = null;
yAxis = 0;
function addDataToChart(data) {
    var chart = $('#chart-container').highcharts();
    if (chart) {
    	chart.addSeries({                        
    	    name: seriesName,
    	    data: data,
            yAxis: yAxis,
            tooltip: {
            	valueSuffix: " m"
            }
    	});
    }
}

function addData(series_url,name,y) {
	var chart = $('#chart-container').highcharts();
    var seriesLength = chart.series.length;
    for(var i = seriesLength - 1; i > -1; i--) {
        if(chart.series[i].name == name) {
            chart.series[i].remove();
            return;
        }
    }
    
    yAxis = y;
	seriesName = name;
    $.ajax({
        url: series_url,
        datatype: "json",
        success: addDataToChart
    });
}