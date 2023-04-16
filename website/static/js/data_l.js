$(document).ready(function () {
    createdatatable2();    
});

function createdatatable2() {

    d3.json('static/data/loan_datatable.json').then(function(data){

        data_columns = [];

        data_headers = ['Applicant Id', 'loan Amount', 'Loan Term', 'Interest Rate', 'Installment', 'Subgrade', 'Employment Length (Years)', 'Home Ownership', 'Annual Income', 'Date of Issue', 'Loan Status', 'Purpose', 'Debt to Income Ratio', 'Number of Delinquencies Over Past Two Years', 'Number of Credit Inquiries Past 6 Months', 'Number of Open Credit Lines', 'Total Credit', 'Ratio of Total Credit Utilized', 'Total Number of Credit Lines', 'Number of Recent Bankruptcies', 'Federal Reserve Region', 'Date of Last Credit Pull', 'Grade', 'State of Address']
        
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


