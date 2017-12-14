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
	dateString = (new Date()).toISOString().split('T')[0]
	center = (new Date(dateString)).getTime();
    Highcharts.chart('chart-container', {
        chart: {
            type: 'column',
            height: 80
        },
        title: {
            text: ''
        },
        xAxis: {
            type: "datetime",
            labels: {
                enabled: true
            },
            plotLines: [{
                color: '#DDDDFF',
                width: 20,
                value: center
            }],
            max: center + 604800000,
            min: center - 604800000
        },
        yAxis: {
            title: {
                text: ''
            },
            labels: {
                enabled: false
            },
            gridLineWidth: 0,
            max: 20,
            min: 0
        },
        legend: {
            enabled: false
        },
        tooltip: {
            xDateFormat: ' ',
            shared: true,
            valueSuffix: " mm",
            valueDecimals: 2
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Neerslag',
            data: receivedData,
            pointRange: 24 * 3600 * 1000,
            pointPadding: 0,
            groupPadding: 0,
            pointPlacement: 1.0/12.0,
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

function setTimeAxis(date) {
    var chart = $('#chart-container').highcharts();
    if (chart) {
        var msInWeek = 604800000;
        chart.xAxis[0].setExtremes(date.getTime() - msInWeek, date.getTime() + msInWeek);
        chart.xAxis[0].options.plotLines[0].value = date.getTime();
        chart.xAxis[0].update();
    }
}