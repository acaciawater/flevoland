// Requires:   	<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
//  			<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

function getDatePicker(id) {
     $.datepicker.regional.nl = {
         closeText: 'Sluiten',
         prevText: '←',
         nextText: '→',
         currentText: 'Vandaag',
         monthNames: ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'],
         monthNamesShort: ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec'],
         dayNames: ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag'],
         dayNamesShort: ['zon', 'maa', 'din', 'woe', 'don', 'vri', 'zat'],
         dayNamesMin: ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za'],
         weekHeader: 'Wk',
         dateFormat: 'yy-mm-dd',
         firstDay: 1,
         isRTL: false,
         showMonthAfterYear: false,
         yearSuffix: ''
     };
     $.datepicker.setDefaults($.datepicker.regional["nl"]);

     var picker = $(id).datepicker({
         defaultDate: new Date()
     });
     
     $("#datepicker").datepicker("setDate", new Date());
     $("#datepicker").datepicker("refresh");
     
     return picker;
 }