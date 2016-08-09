function listaProveedor() {

  // funcion para listar los proveedores ============
  var t = document.getElementById('tb-proveedores').getElementsByTagName('tbody')[0];
  if (t.rows.length == 0) {
    $.ajax({
      url: '/lista_proveedores/',
      dataType: 'json',
      type: 'GET',
      success: function(datos) {
        
        for (var d in datos){
            // console.log(datos[d].fields.nombre);
            
            // obteniendo el tr de la tabla
            var rowCount = t.rows.length;
            // insertando los  td
            var row = t.insertRow(rowCount);
            // insertando ids a los tr de la tabla
            row.id='tr_'+rowCount;
            row.setAttribute('class', 'trd')
            //agregando celdas
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            

            // insertando los datos en los td
            cell1.innerHTML = datos[d].fields.codigo;
            cell2.innerHTML = datos[d].fields.nombre;
            var ct= rowCount+1;
            
            cell1.setAttribute('class', 'with-cell');
            cell2.setAttribute('class', 'with-cell');
           
            

        };

        // funcion para hacer click en los tr de la tabla ========
        // $('#tb-proveedores tbody tr  td').click(function() {
    
        //         $("#proveedor").val($(this).closest('tr').children()[0].textContent);
        //         $("#nombre").val($(this).closest('tr').children()[1].textContent);
        //         $.magnificPopup.close();
        // });

        // $rows = $('table#tb-proveedores > tbody tr').keynavigator({
        //   parentFocusOn:'mouseover', 
        //   activateOn: 'click',
        //   activeClass:'prueba',
        //   cycle: false
        // });

       

        // $rows.on('up', function(e) {
        //   if ($(this).offset().top - 40 < $('.bodytable').scrollTop()) {
        //     return $('.bodytable').scrollTop($('.bodytable').scrollTop() - 40);
        //   }
        // });

        // $rows.on('down', function(e) {
        //   if ($(this).offset().top + $(this).height() + 40 > $('.bodytable').scrollTop() + $('.bodytable').height()) {
        //     return $('.bodytable').scrollTop($('.bodytable').scrollTop() + 40);
        //   }
        // });

       

        function selectRow (newRow) {
            // make sure the parameter is a jQuery object
           
            newRow = $(newRow);
            
            // exit early if we don't have a new row
            if (newRow.length == 0) return;

           
            
            // unselect the old row
            var oldRow = $('.prueba');
            oldRow.removeClass('prueba');

            // select the new row
            
    
            console.log(newRow.hasClass('none'));

            newRow.addClass('prueba');
            
            
            // we could use location.hash = '#' + newRow.attr('id'), but instead we will do...

            // scrolling magic
            var rowTop = newRow.position().top;
            var rowBottom = rowTop + newRow.height();
            var $table = $('#tb-proveedores tbody'); // store instead of calling twice
            var tableHeight = $table.height();
            var currentScroll = $table.scrollTop();
            
            if (rowTop < 0)
            {
                // scroll up
                $('#tb-proveedores tbody').scrollTop(currentScroll + rowTop);
            }
            else if (rowBottom  > tableHeight)
            {
                // scroll down
                var scrollAmount = rowBottom - tableHeight;
                $('#tb-proveedores tbody').scrollTop(currentScroll + scrollAmount);
            }
            
        }

        // simplified event handlers:
        $('#tb-proveedores tbody tr').click(function() {
            
            
            // just call our new selectRow function
            selectRow(this);
        });

        $(document).keydown(function (event) {
            // just leave this as a jQuery object. No reason to use .get(0);
            
            var currentRow = $('.prueba');
            
            switch(event.keyCode)
            {
                    //arrow down
                case 40:
                    
                    selectRow(currentRow.next());
                    
                    
                    return false; // return false to override default page scrolling on up and down keys
                    //arrow up
                case 38:
                    selectRow(currentRow.prev());
                    return false; // return false to override default page scrolling on up and down keys
                    //esc
                case 13:
                    console.log(currentRow.closest('tr').children()[0].textContent);
                    break;
            }
        });
         
                

      } //success
    });

  };
  
}
