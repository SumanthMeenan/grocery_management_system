$(function () {
    //Json data by api call for order table
    $.get(customerproductUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            console.log(response)
            $.each(response, function(index, sale) {
                totalCost += parseFloat(sale.total);
                table += '<tr>' +
                    '<td>'+ sale.customer_name +'</td>'+
                    '<td>'+ sale.name +'</td>'+
                    '<td>'+ sale.total_price +'</td>'
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


