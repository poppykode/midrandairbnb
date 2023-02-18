
$(document).ready(function () {
    
    fetchBookings();
  });
 
  function fetchBookings(){
    // var id = document.getElementById("property_id").value;
    var url = "http://127.0.0.1:8000/api/v1/bookings/" + document.getElementById("property_id").value;
    console.log(url)
    fetch(url).then(
      function (response) {
        if (response.status !== 200) {
          console.warn('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }
        // Examine the text in the response  
        response.json().then(function (data) {
            var s = []
            for (let i = 0; i < data.length; i++) {
                s.push(data[i].trim())
            }
            console.log(s)
            $('#datePick').multiDatesPicker({
               dateFormat: 'dd-mm-yy',
                beforeShowDay: function(date){
                    var string = jQuery.datepicker.formatDate('dd-mm-yy', date);
                    return [s.indexOf(string) == -1]
                }
            });
        });
      }
    )
    .catch(function (err) {
      console.error('Fetch Error -', err);
    });
    }