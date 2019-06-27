
$(function() {
    const HTTP_CODES = {OK:200, CREATED:201, BAD_REQUEST:400, NOT_FOUND:404}

    $(document).ready(function() {
        console.log("test")
    });

    $("#alert-button").click(function(event) {
        $.ajax({
            url : alert_sound_url,
            type : 'POST',
            data : {},
            dataType:'json',
            success : function(data) {              
                alert('Data: '+data);
            },
            error : function(request,error)
            {
                alert("Request: "+JSON.stringify(request));
            }
        }); 
    });
});
