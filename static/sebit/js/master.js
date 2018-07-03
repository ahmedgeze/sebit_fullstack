var container=$('div.container');
var table=document.getElementById("table");
var tableRef = document.getElementById('my_table').getElementsByTagName('tbody')[0];
      $.ajax({
  type: 'GET',
  url: '/api/get',
  async: false, //This is deprecated in the latest version of jquery must use now callbacks
  success: function(data){
    var str;
    if(data.length==undefined){
        var curr=data;
  // Insert a row in the table at the last row
        var newRow   = tableRef.insertRow(tableRef.rows.length);

        var newCelid  = newRow.insertCell(0);
        var newCelone  = newRow.insertCell(1);
        var newCeltwo = newRow.insertCell(2);
        var newCelthree  = newRow.insertCell(3);

  // Append a text node to the cell
      var name  = document.createTextNode(curr.person_name);
      var city  = document.createTextNode(curr.city_name);
      var country  = document.createTextNode(curr.country_name);
      var id=document.createTextNode(curr.id);

      newCelid.appendChild(id);
      newCelone.appendChild(name);
      newCeltwo.appendChild(city);
      newCelthree.appendChild(country);



    }

    for( var i =0;i<data.length;i++){

      var curr=data[i];
// Insert a row in the table at the last row
      var newRow   = tableRef.insertRow(tableRef.rows.length);

      var newCelid  = newRow.insertCell(0);
      var newCelone  = newRow.insertCell(1);
      var newCeltwo = newRow.insertCell(2);
      var newCelthree  = newRow.insertCell(3);

// Append a text node to the cell
    var name  = document.createTextNode(curr.person_name);
    var city  = document.createTextNode(curr.city_name);
    var country  = document.createTextNode(curr.country_name);
    var id=document.createTextNode(curr.id);

    newCelid.appendChild(id);
    newCelone.appendChild(name);
    newCeltwo.appendChild(city);
    newCelthree.appendChild(country);

    }


  }
});

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#table tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});


$(document).ready(function() {
    $('#my_table').DataTable( {
        "order": [[ 0, "desc" ]]
    } );
} );

function saveUser(){
  var id=document.getElementsByTagName("input")[0].value;
  var name=document.getElementsByTagName("input")[1].value;
  var city=document.getElementsByTagName("input")[2].value;
  var country =document.getElementsByTagName("input")[3].value;
  alert(id+name+city+country);
  $.ajax({
type: 'GET',
url: '/api/put/'+id+"/"+name+"/"+city+"/"+country,
async: false, //This is deprecated in the latest version of jquery must use now callbacks
success: function(data){
var str;
if(data.length==undefined){
    var curr=data;
// Insert a row in the table at the last row
    var newRow   = tableRef.insertRow(tableRef.rows.length);

    var newCelid  = newRow.insertCell(0);
    var newCelone  = newRow.insertCell(1);
    var newCeltwo = newRow.insertCell(2);
    var newCelthree  = newRow.insertCell(3);

// Append a text node to the cell
  var name  = document.createTextNode(curr.person_name);
  var city  = document.createTextNode(curr.city_name);
  var country  = document.createTextNode(curr.country_name);
  var id=document.createTextNode(curr.id);

  newCelid.appendChild(id);
  newCelone.appendChild(name);
  newCeltwo.appendChild(city);
  newCelthree.appendChild(country);



}

for( var i =0;i<data.length;i++){

  var curr=data[i];
// Insert a row in the table at the last row
  var newRow   = tableRef.insertRow(tableRef.rows.length);

  var newCelid  = newRow.insertCell(0);
  var newCelone  = newRow.insertCell(1);
  var newCeltwo = newRow.insertCell(2);
  var newCelthree  = newRow.insertCell(3);

// Append a text node to the cell
var name  = document.createTextNode(curr.person_name);
var city  = document.createTextNode(curr.city_name);
var country  = document.createTextNode(curr.country_name);
var id=document.createTextNode(curr.id);

newCelid.appendChild(id);
newCelone.appendChild(name);
newCeltwo.appendChild(city);
newCelthree.appendChild(country);

}


}
});
id.value=""
name.value=""
city.value=""
country.value=""
  location.reload();





  document.getElementById("demo").innerHTML = "Hello World"

}
