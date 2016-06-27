
// // objeto para guardar productos y factura de la compra
var proceso = new Object();
proceso.producto = new Array();

var table = new Array();



$(".agregar_item").keypress(function(e){
   if(e.which == 13) {
      if($('#add_buscar_item').val() == ''){
        
        alert('necesitas buscar un producto');
      }else{
            
        console.log('----datosss array ------------');
      
        var d = table;

        var item =  $( "#add_buscar_item" ).val();
      
        var cantidad =  $( "#cantidad" ).val();

        proceso.producto.push({
          'codigo_item': item,
          'pk': $('#pk').val(),
          'cantidad': cantidad,
          'unidad': $('#unidad').val(),
          'descripcion': $('#descripcion').val(),
          'pr_costo': $('#pr_costo').val(),
          'subtotal': ($('#pr_costo').val())*cantidad,
         
        });

        console.log(proceso);

        // obteniendo la tabla para insertar los campos
        var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
        // obteniendo el tr de la tabla
        var rowCount = t.rows.length-1;
            // insertando los  td
            var row = t.insertRow(rowCount);
            // insertando ids a los tr de la tabla
            row.id='tr_'+rowCount;
            //agregando celdas
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);
            var cell7 = row.insertCell(6);

            // insertando los datos en los td
            cell1.innerHTML = $( "#add_buscar_item" ).val();
            cell2.innerHTML = $( "#unidad" ).val();
            cell3.innerHTML = $( "#descripcion" ).val();

            cell4.innerHTML = $( "#cantidad" ).val();
       
            cell5.innerHTML =  $('#pr_costo').val();

            cell6.innerHTML = ($('#pr_costo').val())*cantidad;


            var ct= rowCount+1;
           
            cell7.innerHTML ="<a class='btn ladda-button btn-danger progress-button' id='eliminar-"+ct+"'><i class='fa fa-trash-o fs20'></i></a>";

            $('#eliminar-'+ct).click(function (){
              console.log('deleteeeeeeeeeeeeeeee');
              row.remove();
              calTotal();
              proceso.producto.splice(ct-1,1);
              console.log(proceso.producto);
            });
            
            calTotal();


            $( "#add_buscar_item" ).val('');
            $( "#unidad" ).val('');
            $( "#descripcion" ).val('');
            $("#cantidad").val('');
            $("#pr_costo").val('');
            $("#pk").val('');

          }
        }

          
        });

var total = 0;
function calTotal(){
  console.log('holaaaaaaaa');
    var total=0;
    var t=0;
    $('#tb-detalle tbody tr').each(function () {
        total = total*1 + $(this).find("td").eq(5).html()*1;  
        
        if (!isNaN(total)) {
          t = t*1 + $(this).find("td").eq(5).html()*1; 
          
        };
    });

    console.log(t);
    $('#sum-subtotal').text(t.toFixed(2));
    
    $('#sum-tax').text(t.toFixed(2));

    $('#sum-total').text(total.toFixed(2));


}

// === metodo para mandar el csrf_token a django mediante ajax ====
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

  function onEnviar(){
      proceso.comprobante = $('#comprobante').val();
      proceso.factura = $('#factura').val();
      proceso.fecha = $('#datepicker1').val();
      proceso.tipodcompra = $('input[name=tipodcompra]:checked').val();
      



      console.log(JSON.stringify(proceso));
     document.getElementById("proceso").value=JSON.stringify(proceso);

     $.ajax({
            type: "POST",
            url: "/compras/",
            dataType: "json",
            data: JSON.stringify(proceso),
            success: function(data) {
               console.log(data);
               console.log('guardo correctamenteeeee');
               new PNotify({
                    title: "Guardado",
                    text: "La compra se guardo correctamente",
                    addclass: "stack-custom",
                    type: 'success',
                    width: '100%',
                    shadow: true,
                    stack: {"dir1":"down", "dir2":"right", "push":"top", "spacing1": 0,"spacing2": 0}
                                
                });

              
          }
        }); 


     var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
      
      //funcion para eliminar tr por el id 
     function  deleteRow(id) {
        document.getElementById('tb-detalle').getElementsByTagName('tbody')[0].removeChild(
        document.getElementById(id)
        );
     }

     // for para contar los tr y eliminarlos
    for (i = 0; i < t.rows.length; i++) {
      console.log(t.rows[i]);
      
      deleteRow('tr_'+i);
      
    }

    // vaciar texto del subtotal de la tabla
    $('#sum-subtotal').text('');

    delete proceso['comprobante'];
    delete proceso['factura'];
    delete proceso['fecha'];
    delete proceso['tipodcompra']
    
    $('#comprobante').val('');
    $('#factura').val('');
    $('#fecha').val('');
    $('#tipodcompra').val('');
    
   

    proceso.producto = new Array();

     
    console.log('procesooooo newwwwww');
    console.log(proceso);
  }

  

    
    

   $( "#add_buscar_item" ).autocomplete({

    source: function( request, response ) {
      console.log('leeeeeegooo');
      $.ajax({
        url: "/buscar_item/",
        dataType: "json",
        data: {'id':request.term},
        success: function( data ) {
         console.log(data);
         response($.map(data, function (pn) {
          console.log(pn);
          return {
            pk: pn.pk,
            codigo: pn.fields.codigo,
            unidad: pn.fields.unidad,
            descripcion: pn.fields.descripcion,
            cantidad: pn.cantidad,
            pr_costo: pn.fields.pr_costo,
            label: pn.fields.codigo+"-"+pn.fields.descripcion
          };
        }));

       }
     });
    }, 
    minLength: 1,       
    select: function( event, ui ) {
      var fila = new Object();
      fila.pk = ui.item.pk_id_item;
      fila.codigo_item = ui.item.codigo_item;
      fila.precio = ui.item.precio_unitario;
      fila.descripcion= ui.item.descripcion;
      fila.cantidad = 1;

      
      $( "#add_item_detail" ).val( ui.item.label );
      $( "#add_buscar_item" ).val( ui.item.codigo );
       $( "#pk" ).val( ui.item.pk );
      $( "#descripcion" ).val( ui.item.descripcion );

      $( "#unidad" ).val( ui.item.unidad );

      $( "#pr_costo" ).val( ui.item.pr_costo );
      $( "#cantidad" ).val( 1 );
      

  
      

      // add_calculo_totales();
      
     
      
      return false;
    },      
    open: function() {
      $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
    },
    close: function() {
      $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
    }
    });


function deleteAll() {
  var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
            
      //funcion para eliminar tr por el id 
     function  deleteRow(id) {
        document.getElementById('tb-detalle').getElementsByTagName('tbody')[0].removeChild(
        document.getElementById(id)
        );
     }

     // for para contar los tr y eliminarlos
    for (i = 0; i < t.rows.length; i++) {
      console.log(t.rows[i]);
      
      deleteRow('tr_'+i);
      
    }

    // vaciar texto del subtotal de la tabla
    $('#sum-subtotal').text('');

    delete proceso['comprobante'];
    delete proceso['factura'];
    delete proceso['fecha'];
    delete proceso['tipodcompra']
    
    $('#comprobante').val('');
    $('#factura').val('');
    $('#fecha').val('');
    $('#tipodcompra').val('');
    
   

    proceso.producto = new Array();
}


  //         $( "#add_nit" ).autocomplete({
  //         source: function( request, response ) {
  //           console.log(request);
  //           $.ajax({
  //             url: "/buscar_proveedor/",
  //             dataType: "json",
  //             data: {'id':request.term},
  //             success: function( data ) {
  //              console.log(data);
  //              response($.map(data, function (pn) {
  //               console.log('estoo es stockkkkkkkkkk')
  //               console.log(pn);
  //               console.log('uuuuuuuuuuuuuuuuuuuuu')
  //               return {
  //                 pk: pn.pk,
  //                 nit: pn.fields.nit,
  //                 razon_social: pn.fields.razon_social,
  //                 label: pn.fields.nit+"-"+pn.fields.razon_social
  //               };
  //             }));

  //            }
  //          });
  //         }, 

  //         focus: function(event, ui) {
  //           event.preventDefault();
  //           $(this).val(ui.item.nit);
  //         },

  //         minLength: 2,       
  //         select: function( event, ui ) {
  //           var fila = new Object();
  //           fila.pk = ui.item.pk_id_item;
  //           fila.nit = ui.item.nit;
  //           fila.razon_social = ui.item.razon_social;

  //           $( "#add_razon" ).focus().val( ui.item.razon_social );

  //           return false;
  //         },      
  //         open: function() {
  //           $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
  //         },
  //         close: function() {
  //           $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
  //         }
  //         });

  //         $( "#add_razon" ).autocomplete({
  //         source: function( request, response ) {
  //           console.log(request);
  //           $.ajax({
  //             url: "/buscar_proveedor/",
  //             dataType: "json",
  //             data: {'id':request.term},
  //             success: function( data ) {
  //              console.log(data);
  //              response($.map(data, function (pn) {
  //               console.log('estoo es stockkkkkkkkkk')
  //               console.log(pn);
  //               console.log('uuuuuuuuuuuuuuuuuuuuu')
  //               return {
  //                 pk: pn.pk,
  //                 nit: pn.fields.nit,
  //                 razon_social: pn.fields.razon_social,
  //                 label: pn.fields.razon_social+"-"+pn.fields.nit
  //               };
  //             }));

  //            }
  //          });
  //         }, 

  //         focus: function(event, ui) {
  //           event.preventDefault();
  //           $(this).val(ui.item.razon_social);
  //         },

  //         minLength: 2,       
  //         select: function( event, ui ) {
  //           var fila = new Object();
  //           fila.pk = ui.item.pk_id_item;
  //           fila.nit = ui.item.nit;
  //           fila.razon_social = ui.item.razon_social;
            
  //           $( "#add_nit" ).focus().val( ui.item.nit );

  //           return false;
  //         },      
  //         open: function() {
  //           $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
  //         },
  //         close: function() {
  //           $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
  //         }
  //         });

  // });
