$(document).ready(function () {
    createdatatable2();    
});

function createdatatable2() {

    d3.json('static/data/credit_card_datatable.json').then(function(data){

        data_columns = [];

        data_headers = ['Applicant ID', 'Gender', 'Car Ownership', 'Property Ownership', 'Employment Status', 'Number of Children', 'Family Size', 'Lenth of Time Owned Credit Card (months)', 'Total Income (Yuan)', 'Age (Years)', 'Years Employed', 'Income Type', 'Education Type', 'Family Status', 'Housing Type', 'Occupation Type', 'Approval']

        data_trimmed = [];
        for (k = 0; k < data.length; k++) {
            datum = data[k];
            ret_array = [];
            for (j = 0; j < data_headers.length; j++) {
                headerr = data_headers[j];
                ret_array.push(datum[headerr]);
            }
            data_trimmed.push(ret_array);            
        }

        for (i = 0; i < data_headers.length; i++) {
            header = data_headers[i];
            title_dict = {'title': `${header}`};
            data_columns.push(title_dict);
        }

        $(document).ready(function() {

            $('#data_table').DataTable({
                data: data_trimmed,
                columns: data_columns,
                fixedColumns: true,
            });

        });

    });

}


