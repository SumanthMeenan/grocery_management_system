$(function () {
    //Json data by api call for order table
    $.get(productSalesUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            console.log(response)
            $.each(response, function(index, sale) {
                totalCost += parseFloat(sale.total);
                table += '<tr>' +
                    '<td>'+ sale.name +'</td>'+
                    '<td>'+ sale.product_id +'</td>'+
                    '<td>'+ sale.total_quantity +'</td>'+
                    '<td>'+ sale.total_sales +' Rs</td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});


