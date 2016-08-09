<!--
/*
/
/ Programming Logic - #2  [HTML/JQUERY Table Filter]
/ Developer : Suraj Jain
/ Blog : https://developersurajjain.blogspot.com/
/ Website : http://www.surajjain.com/
/ Email : mail.surajjain@gmail.com
/
*/
-->
(function($) {
	
	$.fn.dsjtableFilter = function() {
		
		var $table = $(this);
		var $searchInput = $('#searchallInput');
		var rows = $table.find('thead tr').length;
		var cols = $table.find('thead tr th').length;
		if(rows == 2) {
			$table.find('thead tr:eq(0) th[data-type=filter]').each(function(index, element) {
				$table.find('thead tr:eq(1) th:eq(' + $(this).index() + ') input').attr('placeholder', $(this).text());
            });	
		} else {
			// alert('Invalid code.');	
		}
		$('#dsj-tableFilter').mouseenter(function(e) {    
			$(this).datepicker();
		});
				
		$searchInput.attr('placeholder', 'search');
		
		$('input[class=searchInput]:text', $table).keyup(function(e) {
			var point = $(this).parent().index();
			var search = $(this).val();
			var found = false;
			$table.find('tbody tr').each(function(i, e) {
				$(this).find('td:eq(' + point + ')').each(function(index, element) {
                   var text = $(this).text();
				   if(text.toUpperCase().indexOf(search.toUpperCase()) === -1) {
					   $(this).css("text-decoration", "none").css("font-weight", "100");
					   $(this).parent().hide();

				   } 
				   else {
					   $(this, ':contains('+ search +')').css("text-decoration", "underline").css("font-weight", "700");
					   $(this).parent().show();
					   found = true;
				   }
				   if(search == '') {
					    $(this).css("text-decoration", "none").css("font-weight", "100");
				   }
                });				
			});
			
			if(!found) {
			 if($('#noFnd').length <= 0)$table.find('tbody').append('<tr id="noFnd"><td colspan="' + cols + '">No record found</td></tr>')
			} else	{		
			 if($('#noFnd').length > 0){
			 	$table.find('tbody tr#noFnd').remove();
				//$table.find('tbody tr').show();
			 }
			}
		});
		
		$('#searchallInput').keyup(function(e) {
            var search = $(this).val();
			var found = false;
			$table.find('tbody tr').each(function(i, e) {
				var filter = true;
				$(this).find('td').each(function(index, element) {                   
				   var text = $(this).text();
				   if(text.toUpperCase().indexOf(search.toUpperCase()) === -1) {
					  $(this).css("text-decoration", "none").css("font-weight", "100");
				   } else {
					   $(this, ':contains('+ search +')').css("text-decoration", "underline").css("font-weight", "700");
					   $(this, ':contains('+ search +')').css("text-decoration", "underline").css("font-weight", "700");
					   
					   filter = false;
				   }
				   if(search == '') {
					    $(this).css("text-decoration", "none").css("font-weight", "100");
				   }
                });
				if(filter) {
				  $(this).hide();
				  $(this).addClass('none');
			   } else {
				   $(this).show();
				   $(this).addClass('encontrado');
				   found = true;
			   }				
			});
			if(!found) {
			 if($('#noFnd').length <= 0)$table.find('tbody').append('<tr id="noFnd"><td colspan="' + cols + '">No record found</td></tr>')
			} else	{		
			 if($('#noFnd').length > 0){
			 	$table.find('tbody tr#noFnd').remove();
			 }
			}
        });
				
	};
	
	$.fn.dsjtableFilter2 = function() {
		alert('sds');
	};
	
})(jQuery);
