$(document).ready(function(){
	/* Global Objects */

	posts_local_data = {}

	groups_local_data = {}

 
	/* Dynamic Table Definitions */	
	
	databases = $('#databases').dataTable({
		"sDom": '<"top"f<"clear">>rt<"bottom"ilp<"clear">>',
		"bPaginate": false,
		"bFilter": true,
		"sWidth": "100%",
		"aoColumns": [                 
			{"sWidth": "50%"},
			{"sWidth": "50%"},
		],
		"fnInitComplete": function() {
                    $('#databases tbody tr').on("click", function () {
                        load_table(this);
                    } ); }
	});
	
	

	function load_table (tr) {
		var url = window.location.href + '/' + $(tr.cells[0]).html();
		console.log(url)
		$(location).attr('href',url);
	}
	
	/* Default blur effect in textbox */
	
	$(".default-text").focus(function(srcc)
	{
	    if ($(this).val() == $(this)[0].title)
	    {
	        $(this).removeClass("default-text-active");
	        $(this).val("");
	    }
	});
    
	$(".default-text").blur(function()
	{
	    if ($(this).val() == "")
	    {
	        $(this).addClass("default-text-active");
	        $(this).val($(this)[0].title);
	    }
	});
	
    
	

	
	
	function strip(html){
   		var tmp = document.createElement("DIV");
   		tmp.innerHTML = html;
   		var txt = tmp.textContent||tmp.innerText;
		return txt.substring(0, 100);
	}


	function format_date(d) {
		var dateStr,hours,minutes,ampm;
		dateStr = (d.getMonth() + 1) +'/'+d.getDate()+'/'+d.getFullYear();
		hours = d.getHours();
		minutes = d.getMinutes();
		ampm = hours >= 12 ? 'PM' : 'AM';
		hours = hours % 12;
		if(!hours) {
			hours = 12;
		}
		//hours = hours ? hours : 12;
		minutes = minutes < 10 ? '0'+minutes : minutes;
		timeStr = hours + ':' + minutes + ' ' + ampm;
		return {'date':dateStr, 'time': timeStr}
	}



	


});
