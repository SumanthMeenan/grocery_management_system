$("#search-customer").on("click", function () {
    var value = document.getElementById("cust-search").value
    //Json data by api call for order table
    $.post(custHistUrl, {customer: value}, function (response) {
        if(response) {
            document.getElementById("cust-search").value = "";
            if(!response.length){
                return;
            }
            var table = '';
            var totalCost = 0;
            console.log(response)
            $.each(response, function(index, sale) {
                totalCost += parseFloat(sale.total);
                table += '<tr>' +
                    '<td>'+ sale.order_id +'</td>'+
                    '<td>'+ sale.customer_name +'</td>'+
                    '<td>'+ sale.total+'</td>'+
                    '<td>'+ sale.datetime +' Rs</td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});

$("#cust-search-form").submit(function(e){
    return false;
});


