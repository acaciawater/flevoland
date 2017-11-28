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
                text: 'Peil'
            },
            labels: {
                format: '{value} m'
            },
            min: -1.5,
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
            max: 40

        }],
        legend: {
            enabled: false
        },
        tooltip: {
            xDateFormat: ' ',
            shared: false,
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

function addDataToChart(data) {
    var chart = $('#chart-container').highcharts();
    if (chart) {
    	chart.addSeries({                        
    	    name: 'Peil',
    	    data: data,
            yAxis: 0
    	});
    }
}

function addData(series_url) {
    $.ajax({
        url: series_url,
        datatype: "json",
        success: addDataToChart
    });
}