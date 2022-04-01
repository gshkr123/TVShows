    function myFunction() {
        const val = $("#city_id").val();
        if (val !== "--") {
            $.ajax({
                url : '/getSelectData/' + val ,
                type : 'GET',
                dataType:'html',
                success : function(data) {
                    $("#alldata").hide();
                    $("#selecteddata").show();
                    $("#selecteddata").empty();
                    $("#selecteddata").html(data);
                },
                error : function(request,error)
                {
                    alert("Request: "+JSON.stringify(request));
                }
            });
        }

    }

    function showAllData() {
        $("#selecteddata").hide();
        $("#alldata").show();
    }
