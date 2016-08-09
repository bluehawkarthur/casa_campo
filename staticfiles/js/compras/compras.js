
// ====== para mostrar fecha de ingreso en el input ====
var now = new Date();

var day = ("0" + now.getDate()).slice(-2);
var month = ("0" + (now.getMonth() + 1)).slice(-2);
var today = (day)+"/"+(month)+"/"+now.getFullYear() ;

$('#datepicker1').val(today);


// funcion para resetear la tabla
function resetDetalle() {  
    var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
    console.log('losss rowsss');
    console.log(t.rows.length);
    if (t.rows.length > 1){    
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
    }
    // vaciar texto del subtotal de la tabla
    $('#sum-subtotal').text('');

}


// para eliminar los tr de la tabla =====================
function deleteRow(r) {
    var i = r.parentNode.parentNode.rowIndex;
    document.getElementById("tb-detalle").deleteRow(i);
}


// funcion pra buscar compras 

$( "#comprobante" ).autocomplete({

    source: function( request, response ) {
      
      $.ajax({
        url: "/buscar_compra/",
        dataType: "json",
        data: {'id':request.term},
        success: function( data ) {
         console.log('leeeeeegooo');
         console.log(data);
         response($.map(data, function (pn) {
          console.log(pn);
          return {
            pk: pn.pk,
            comprobante: pn.fields.comprobante,
            factura: pn.fields.factura,
            fecha: pn.fields.fecha,
            tipodcompra: pn.tipodcompra,
            pr_costo: pn.fields.pr_costo,
            detalle: pn.fields.detalle,
            label: pn.fields.comprobante
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
      console.log('los detallessss');
      var detalle1 = ui.item.detalle
      // console.log(ui.item.detalle);
      
      var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
      resetDetalle();

      for (var d in detalle1){
          console.log(detalle1[d].descripcion);
          // obteniendo la tabla para insertar los campos
          
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
          cell1.innerHTML = detalle1[d].codigo;
          cell2.innerHTML = detalle1[d].unidad;
          cell3.innerHTML = detalle1[d].descripcion;

          cell4.innerHTML = detalle1[d].cantidad;
     
          cell5.innerHTML =  detalle1[d].pr_costo;

          cell6.innerHTML = (detalle1[d].pr_costo)*detalle1[d].cantidad;


          var ct= rowCount+1;
         
          cell7.innerHTML ="<a class='btn ladda-button btn-danger progress-button' id='eliminar-"+ct+"' onclick='deleteRow(this)'><i class='fa fa-trash-o fs20'></i></a>";
          var ctotal = ct-1;
      }

      
      $('#factura').val(ui.item.factura);
      $('#datepicker1').val(ui.item.fecha);
      $('input[name=tipodcompra]:checked').val();
      
      return false;
    },      
    open: function() {
      $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
    },
    close: function() {
      $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
    }
    });


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
            $( "#add_buscar_item" ).focus();

          }
        }

          
        });

// funcion de presionado d enter y haga focus en grupo =====
$("#grupo").keypress(function(e){
   if(e.which == 13) {
    $('#datepicker1').focus();
   }
});

// funcion de presionado d enter y haga focus en fecha =====
$("#datepicker1").keypress(function(e){
   if(e.which == 13) {
    $('#factura').focus();
   }
});

// funcion de presionado d enter y haga focus en codigo producto =====
$("#factura").keypress(function(e){
   if(e.which == 13) {
    $('#add_buscar_item').focus();
   }
});


// funcion de presionado d enter y haga focus en precio de costo =====
$("#cantidad").keypress(function(e){
   if(e.which == 13) {
    $('#pr_costo').focus();
   }
});


// funcion para resetear la tabla proveedores =======
function resetProveedor(t) {  
     // for para contar los tr y eliminarlos
      // console.log(t.rows.length);
        for (var i = 0; i < t.rows.length; i++) {
          // console.log('elimnado');
          // console.log(t.rows[i]);
          document.getElementById("tb-proveedores").deleteRow(t.rows[i]); 
        } 
}



// ======================================================================================

//  inicio                        MODAL PROVEEDORES

// ======================================================================================

// funcion para filtrar la tabla de proveedor=====
  // $('#tb-proveedores').dsjtableFilter();

// ======= para validar el modal de proveedor ======
var validator_clinica = $('#formproveedor').validate({
    focusCleanup: true,
    rules: {
        codigo: {
            required: true
        },
        nombre: {
            required: true
        }
    },
    highlight: function(element, errorClass, validClass) {
      $(element).closest('.field').addClass(errorClass).removeClass(validClass);
    },
    unhighlight: function(element, errorClass, validClass) {
      $(element).closest('.field').removeClass(errorClass).addClass(validClass);
    },
    errorElement: 'em',
    errorClass: 'state-error',
    validClass: "state-success",
    errorPlacement: function(error, element) {
        if(element.parent('.field').length) {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
});


// funcion de presionado d enter y haga focus en codigo de proveedor =====
$("#proveedor").keypress(function(e){
  if(e.which == 13) {
    $("#grupo").focus();
    // e.stopPropagation();
    if ($(this).val() == '') {
      $.magnificPopup.open({
          closeBtnInside:true,
          removalDelay: 1000,
          // closeOnContentClick: true,
          // midClick: true,
          autoFocusLast : true,
          focus: "#si_compra",
          closeMarkup: '<button title="%title%" type="button" class="mfp-close cerrar">&times;</button>',
          items: {
              src: '#modal-text',
              type: 'inline'
          },
          callbacks: {
            beforeOpen: function (e) {
                this.st.mainClass = 'mfp-zoomIn';
                $('#grupo').focusout();
                console.log('ddddd');
            },
            afterClose: function() {
              $('#tb-proveedores tbody tr').removeAttr('prueba');
              $('#tb-proveedores tbody tr td').removeAttr('prueba');
              validator_clinica.resetForm();
              $("#formproveedor").find(".state-error").removeClass("state-error");
            }
          },
      });
    };
  }
});


// === para el focus item con teclado ============================
$('#modal-text').on('keydown', function(e){

  var isfocus = $(this).find(':focus');
  var isfocusindex = $(this).find(':focus').index();
  var isfocusbegin = $(this).find('*:first:focus');
  var isfocuslast = $(this).find('*:last:focus');
  if ( e.which == 37 ) { // Left arrowkey
  isfocus.prev().focus();
  isfocusbegin.siblings(':last').focus();
  }
  if ( e.which == 39 ) { // right arrowkey
  isfocus.next().focus();
  isfocuslast.siblings(':first').focus();
  }

});

// ====== funcion para listar los proveedores en el modal ===========
function listaProveedorModal() {
  var table = $('#tb-proveedores').dataTable({
    language: {
      url: "/static/localizacion/es_ES.json"
    },
    scrollY:        '220px',
    scrollCollapse: false,
    scroller:       true,
    keys:           true,
    paging:         true,
    deferRender: true,
    ajax: {
        "url": "/lista_proveedores/",
        "dataSrc": ""
    },
    columns: [
      { "data": "pk" },
      { "data": "codigo" },
      { "data": "nombre" }
    ],
    columnDefs: [
      { className: "columna_id", "targets": [ 0 ] }
    ]
  });

  table.on( 'key', function ( e, datatable, key, cell, originalEvent ) {
    // events.prepend( '<div>Key press: '+key+' for cell <i>'+cell.data()+'</i></div>' );

    if (key==13) {
      var row = datatable.row(cell.index().row);
      var tr = $(row.node());
      console.log(tr.closest('tr').children()[0].textContent);
      if (tr.hasClass('prueba')){
        $("#pk_proveedor").val(tr.closest('tr').children()[0].textContent);
        $("#proveedor").val(tr.closest('tr').children()[1].textContent);
        $("#nombre").val(tr.closest('tr').children()[2].textContent);
        tr.removeClass('prueba');
        table.fnFilterClear();
        table.fnReloadAjax();
        $.magnificPopup.close();
      }
    };
  });



 
  
}
  // $('#tb-proveedores tbody tr').addClass('prueba');
  $('#tb-proveedores tr:first-child').addClass('yourClass');

// ======= funcion para agregar y eliminar clases de los tr ========
function selectRow (newRow) {
  // make sure the parameter is a jQuery object
  newRow = $(newRow);
  // exit early if we don't have a new row
  if (newRow.length == 0) return;

  // unselect the old row
  var oldRow = $('.prueba');
  oldRow.removeClass('prueba');

  // select the new row
  newRow.addClass('prueba');
}


// ====== funcion para hacer una seleccion ==============
$('#tb-proveedores tbody').on('click', 'tr', function () {
  selectRow(this);
} );

// $('#tb-proveedores tbody').on('mouseover', 'tr', function () {
//   selectRow(this);
// } );

// ====== funcion para el moviento de las teclas de direccion ======
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
        // case 39:
        //   console.log('key izquierdo');
        //   selectButton(currentButton.next());
        //   return false;

        // case 37:
        //   console.log('key derecho');
        //   selectButton(currentButton.prev());
        //   return false;
        // case 13:
        //   if (currentButton.hasClass('color_button')){
        //     $('.color_button').click();
        //   }
        //   return false;

        // case 13:
        //     if (currentRow.hasClass('prueba')){
        //       $("#proveedor").val(currentRow.closest('tr').children()[0].textContent);
        //       $("#nombre").val(currentRow.closest('tr').children()[1].textContent);
        //       currentRow.removeClass('prueba');
        //       $.magnificPopup.close();
        //     }
        //     break;
        // 39, 37
    }
});




// funciones para los eventos si y no de proveedor ===============
$(".proveedor_confirm").click(function(e) {
  var dato = $(this).attr('data-value');
  if (dato == 'si') {
    e.stopPropagation();
    $.magnificPopup.open({
          items: {
              src: '#proveedor-nuevo',
              type: 'inline'
          },
          callbacks: {
              beforeOpen: function (e) {
                 
                  this.st.mainClass = 'mfp-zoomIn';
              },
              afterClose: function() {

              } 
          }
      });
  }else{
    
    e.stopPropagation();
    listaProveedorModal();

    $.magnificPopup.open({
      items: {
        src: '#proveedor-lista',
        type: 'inline'
      },
      callbacks: {
        beforeOpen: function (e) {     
            this.st.mainClass = 'mfp-zoomIn';
        },
        afterClose: function() {
        }  
      },
    });
  }
});

// ======================================================================================

//  fin                        MODAL PROVEEDORES

// ======================================================================================


// ======================================================================================

//  inicio                        MODAL ITEMS

// ======================================================================================

// ======= para validar el modal de item ======
var validator_item = $('#formitem').validate({
    focusCleanup: true,
    rules: {
        codigo_item: {
            required: true
        },
        descripcion_item: {
            required: true
        },
        unidad_item: {
            required: true
        },
        cantidad_item: {
            required: true
        },
        pr_costo_item: {
            required: true
        },
    },
    highlight: function(element, errorClass, validClass) {
      $(element).closest('.field').addClass(errorClass).removeClass(validClass);
    },
    unhighlight: function(element, errorClass, validClass) {
      $(element).closest('.field').removeClass(errorClass).addClass(validClass);
    },
    errorElement: 'em',
    errorClass: 'state-error',
    validClass: "state-success",
    errorPlacement: function(error, element) {
        if(element.parent('.field').length) {
            error.insertAfter(element.parent());
        } else {
            error.insertAfter(element);
        }
    }
});

// $.magnificPopup.instance._onFocusIn = function(e) {
//           // Do nothing if target element is select2 input
//           if( $(e.target).hasClass('#si_item') ) {
//             return true;
//           } 
//           // Else call parent method
//           $.magnificPopup.proto._onFocusIn.call(this,e);
// };

// === para el focus item con teclado ============================
$('#modal-item').on('keydown', function(e){

  var isfocus = $(this).find(':focus');
  var isfocusindex = $(this).find(':focus').index();
  var isfocusbegin = $(this).find('*:first:focus');
  var isfocuslast = $(this).find('*:last:focus');
  if ( e.which == 37 ) { // Left arrowkey
  isfocus.prev().focus();
  isfocusbegin.siblings(':last').focus();
  }
  if ( e.which == 39 ) { // right arrowkey
  isfocus.next().focus();
  isfocuslast.siblings(':first').focus();
  }

});

// funcion de presionado d enter y haga focus en codigo de item =====
$("#add_buscar_item").keypress(function(e){
  if(e.which == 13) {
    $("#cantidad").focus();
    // e.stopPropagation();
    if ($(this).val() == '') {
      $.magnificPopup.open({
          closeBtnInside:true,
          removalDelay: 1000,
          autoFocusLast : true,
          // closeOnContentClick: true,
          // midClick: true,
          focus: "#si_item",
          closeMarkup: '<button title="%title%" type="button" class="mfp-close cerrar">&times;</button>',
          items: {
              src: '#modal-item',
              type: 'inline'
          },
          callbacks: {
            beforeOpen: function (e) {
                this.st.mainClass = 'mfp-zoomIn';
                console.log('ddddditem');
    
                $('#grupo').focusout();
            },
            afterClose: function() {
              $('#tb-proveedores tbody tr').removeAttr('prueba');
              $('#tb-proveedores tbody tr td').removeAttr('prueba');
              validator_item.resetForm();
              $("#formitem").find(".state-error").removeClass("state-error");
            }
          },
      });
    };
  }
});

// funciones para los eventos si y no de item ===============
$(".item_confirm").click(function(e) {
  var dato = $(this).attr('data-value');
  if (dato == 'si') {
    e.stopPropagation();
    $.magnificPopup.open({
          items: {
              src: '#item-nuevo',
              type: 'inline'
          },
          callbacks: {
              beforeOpen: function (e) {
                 
                  this.st.mainClass = 'mfp-zoomIn';
              },
              afterClose: function() {

              } 
          }
      });
  }else{
    
    e.stopPropagation();
    listaProveedorModal();

    $.magnificPopup.open({
      items: {
        src: '#proveedor-lista',
        type: 'inline'
      },
      callbacks: {
        beforeOpen: function (e) {     
            this.st.mainClass = 'mfp-zoomIn';
        },
        afterClose: function() {
        }  
      },
    });
  }
});


// ======================================================================================

//  fin                        MODAL ITEMS

// ======================================================================================

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





// === guardando nuevo proveedor ===========
$('#register-proveedor').click(function(){
    console.log('am i called');
      if ($("#formproveedor").valid()) {
        $.ajax({
            type: "POST",
            url: "/registrar_proveedor/",
            dataType: "json",
            data: $("#formproveedor").serialize(),
            success: function(data) {
               console.log(data);
               // para agregar la nueva clinica registrada en el select
               $("#nombre").val(data.nombre);
               $("#proveedor").val(data.codigo);
               
               // para limpiar los imputs del modal
               $('#formproveedor').find('textarea,input').val('');

               // para cerrar el modal
               $.magnificPopup.close();
          }
        }); 
      }
  

    
});

// === guardando nuevo item ===========
$('#register-item').click(function(){
    console.log('am i called');
      if ($("#formitem").valid()) {
        $.ajax({
            type: "POST",
            url: "/registrar_item/",
            dataType: "json",
            data: $("#formitem").serialize(),
            success: function(data) {
               console.log(data);
               // para agregar la nueva clinica registrada en el select
               $('#pk').val(data.pk);
               $('#add_buscar_item').val(data.codigo);
               $('#unidad').val(data.unidad);
               $('#descripcion').val(data.descripcion);
               $('#cantidad').val(data.cantidad);
               $('#pr_costo').val(data.pr_costo);
               
               // para limpiar los imputs del modal
               $('#formitem').find('textarea,input').val('');

               // para cerrar el modal
               $.magnificPopup.close();
            },
            error: function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }  
        }); 
      } 
});
// funcion para guardar los datos =============================0
function onEnviar(){
    proceso.comprobante = $('#comprobante').val();
    proceso.factura = $('#factura').val();
    proceso.fecha = $('#datepicker1').val();
    proceso.tipodcompra = $('input[name=tipodcompra]:checked').val();
    proceso.pk_proveedor = $("#pk_proveedor").val();
    proceso.grupo = $("#grupo").val();
    



    console.log(JSON.stringify(proceso));
   document.getElementById("proceso").value=JSON.stringify(proceso);

   $.ajax({
          type: "POST",
          url: "/compras/",
          dataType: "json",
          data: JSON.stringify(proceso),
          success: function(data) {
             console.log(data.comprobante);
             console.log('guardo correctamenteeeee');
             $('#comprobante').val(data.comprobante);
             new PNotify({
                  title: "Guardado",
                  text: "La compra se guardo correctamente",
                  addclass: "stack-custom",
                  type: 'success',
                  width: '100%',
                  shadow: true,
                  delay: 2500,
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
  delete proceso['tipodcompra'];
  delete proceso['pk_proveedor'];
  delete proceso['grupo'];
  
  $('#comprobante').val('');
  $('#factura').val('');
  $('#fecha').val('');
  $('#tipodcompra').val('');
  $("#pk_proveedor").val('');
  $("#grupo").val('');
 

  proceso.producto = new Array();

   
  console.log('procesooooo newwwwww');
  console.log(proceso);
}

  

    
// funcion para buscar items =====================================0

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
    $( "#cantidad" ).focus();
    

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

// funcion para eliminar todo de la tabla ====================================
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

// funcion para buscar un proveedor ==============================

$( "#proveedor" ).autocomplete({

    source: function( request, response ) {
      console.log('leeeeeegooo');
      $.ajax({
        url: "/buscar_proveedor/",
        dataType: "json",
        data: {'id':request.term},
        success: function( data ) {
         console.log(data);
         response($.map(data, function (pn) {
          console.log(pn);
          return {
            pk: pn.pk,
            codigo: pn.fields.codigo,
            nombre: pn.fields.nombre,
            label: pn.fields.codigo+"-"+pn.fields.nombre
          };
        }));

       }
     });
    }, 
    minLength: 1,       
    select: function( event, ui ) {
      
      // $( "#add_item_detail" ).val( ui.item.label );
      $( "#nombre" ).val( ui.item.nombre );
      $( "#proveedor" ).val( ui.item.codigo );
       // $( "#pk" ).val( ui.item.pk );
      $( "#grupo" ).focus();
      
      return false;
    },      
    open: function() {
      $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
    },
    close: function() {
      $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
    }
    });






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
