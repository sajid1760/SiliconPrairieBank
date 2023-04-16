$(document).ready(function () {

    
    data = [5,6,7,8,9,10]

    $("#submitld").on("click", function () {
        data = preparedatald()
        console.log(data)
        make_predictionsld(data)
    });
    
});

function preparedatald() {
    full_name = d3.select("#name").node().value;
    gender = d3.select("#gender").node().value;
    age = d3.select("#age").node().value;
    home_ownership = d3.select("#home_ownership").node().value;
    state = d3.select("#state").node().value;
    employment_length = d3.select("#employment_length").node().value;
    annual_income = d3.select("#annual_income").node().value;
    loan_term = d3.select("#loan_term").node().value;
    loan_amount = d3.select("#loan_amount").node().value;
    date_issue = d3.select("#date_issue").node().value;
    purpose = d3.select("#purpose").node().value;
    rate = d3.select("#rate").node().value;
    debt_to_income_ratio = d3.select("#debt_to_income_ratio").node().value;
    grade = d3.select("#grade").node().value;
    sub_grade = d3.select("#sub_grade").node().value;
    delinquencies = d3.select("#delinquencies").node().value;
    credit_inquiries = d3.select("#credit_inquiries").node().value;
    num_open_credit_lines = d3.select("#num_open_credit_lines").node().value;
    num_total_credit_lines = d3.select("#num_total_credit_lines").node().value;
    total_credit = d3.select("#total_credit").node().value;
    credit_util_ratio = d3.select("#credit_util_ratio").node().value;
    num_bankruptcies = d3.select("#num_bankruptcies").node().value;
    date_last_credit_pull = d3.select("#date_last_credit_pull").node().value;
    

    data_json = {           
        'loan_amnt': parseFloat(loan_amount),
        'term': parseInt(loan_term),
        'int_rate': parseFloat(rate),
        'sub_grade': grade + sub_grade,
        'emp_length': parseInt(employment_length),
        'home_ownership': home_ownership,
        'annual_inc': parseFloat(annual_income),
        'purpose': purpose,
        'dti': parseFloat(debt_to_income_ratio),
        'delinq_2yrs': parseInt(delinquencies),
        'inq_last_6mths': parseInt(credit_inquiries),
        'open_acc': parseInt(num_open_credit_lines),
        'revol_bal': parseFloat(total_credit),
        'revol_util': parseFloat(credit_util_ratio),
        'total_acc': parseInt(num_total_credit_lines), 
        'pub_rec_bankruptcies': parseInt(num_bankruptcies),
        'state': state,
        'last_credit_pull_d_int': date_last_credit_pull
    }
        
    return data_json;
    
}

function make_predictionsld(payload) {

    $.ajax({
        type: "POST",
        url: "/makePredictionsld",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            pred_prob = returnedData["prediction"];
            console.log(pred_prob)
            pred = pred_prob[0];
            prob = pred_prob[1]*100;
            if (pred == 1) {
                $("#output").text("We are not able to approve your application.");
                $("#output2").text(`We predict that you have a ${prob} % chance of default`)
            } else {
                $("#output").text("Congratulations! You are approved!")
                $("#output2").text(`We predict that you have a ${prob} % chance of full repayment`);
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}