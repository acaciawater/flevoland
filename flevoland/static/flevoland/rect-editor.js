RectEditor = (function() {
    var SVG = null;        
    var base1 = null;
    var max_height1 = null;
    var original_stroke_width = null;
    var original_stroke = null;
    var original_fill = null;
    var base2 = null;
    var max_height2 = null;
    var date = null;
 
    return {
    	
    	
    	
	    initialize: function(SVG_id, rectangle_id_1, rectangle_id_2, initial_data) {
	        SVG = document.getElementById(SVG_id).getSVGDocument();
	        
	        var rectangle1 = SVG.getElementById(rectangle_id_1);
	        base1 = rectangle1.y.baseVal.value + rectangle1.height.baseVal.value;
	        max_height1 = rectangle1.height.baseVal.value;
	        original_stroke_width = rectangle1.style.strokeWidth;
	        original_stroke = rectangle1.style.stroke;
	        original_fill = rectangle1.style.fill;
	
	        var rectangle2 = SVG.getElementById(rectangle_id_2);
	        base2 = rectangle2.y.baseVal.value + rectangle2.height.baseVal.value;
	        max_height2 = rectangle2.height.baseVal.value;
	
	        date = new Date(initial_data.date);
	        this.setRectangles(initial_data);
	    },
	    
	    getDate: function() {
	   	 	return date;
	    },
	
	    setHeight: function(id, level) {
	        var rectangle = SVG.getElementById(id);
	        if (rectangle.style.strokeWidth != "0") {
	            var height_percentage = 1 + level / 1.5;
	            var height = height_percentage * max_height1;
	            rectangle.y.baseVal.value = base1 - height;
	            rectangle.height.baseVal.value = height;
	        } else {
	            var height_percentage = 1 + level / (7.0 / 9.0 * 1.5);
	            var height = height_percentage * max_height2;
	            rectangle.y.baseVal.value = base2 - height;
	            rectangle.height.baseVal.value = height;
	        }
	    },
	
	    setTooltip: function(id, tooltip) {
	        var rectangle = SVG.getElementById(id);
	        if (rectangle.hasChildNodes()) {
	            rectangle.children[0].textContent = tooltip;
	        } else {
	            var title = SVG.createElementNS("http://www.w3.org/2000/svg", "title");
	            title.textContent = tooltip;
	            rectangle.appendChild(title);
	        }
	    },
	
	    setOpacity: function(id, opacity) {
	        var rectangle = SVG.getElementById(id);
	        if (opacity == 0.0) {
	            rectangle.style.fillOpacity = 1.0;
	            rectangle.style.fill = "#A8A8A8";
	            return;
	        }
	        rectangle.style.fillOpacity = opacity;
	        rectangle.style.fill = original_fill;
	    },
	
	    setRectangles: function(data) {
	        date = new Date(data.date);
	        vals = data.values;
	        for (i = 0; i < vals.length; i++) {
	            x = vals[i];
	            this.setTooltip(x.id, x.date);
	            this.setHeight(x.id, x.val);
	            this.setOpacity(x.id, x.op);
	        }
	    },
	
	    toggleColor: function(id) {
	        var rectangle = SVG.getElementById(id);
	        if (rectangle.style.strokeWidth != "0.5") {
	            rectangle.style.stroke = "#ff0000";
	            rectangle.style.strokeWidth = "0.5";
	        } else {
	            rectangle.style.stroke = original_stroke;
	            rectangle.style.strokeWidth = original_stroke_width;
	        }
	    },
	
	    setToggle: function(id, action) {
	        var rectangle = SVG.getElementById(id);
	        rectangle.onclick = function onclick(evt) {
	            RectEditor.toggleColor(id);
	            action();
	        };
	        rectangle.style.cursor = 'pointer';
	    },
	
	    setURL: function(id, url) {
	        var rectangle = SVG.getElementById(id);
	        var a = SVG.createElementNS("http://www.w3.org/2000/svg", "a");
	        a.setAttribute("href", url);
	        a.setAttribute("target", "_blank");
	        rectangle.parentNode.replaceChild(a, rectangle);
	        a.appendChild(rectangle);
	    }
	    
	    
	    
	    
    };
})();