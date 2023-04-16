$(document).ready(function () {

    
    data = [5,6,7,8,9,10]

    $("#submit").on("click", function () {
        data = preparedata()
        console.log(data)
        make_predictions(data)
    });
    
});

function preparedata() {
    full_name = d3.select("#name").node().value;
    gender = d3.select("#gender").node().value;
    age = d3.select("#age").node().value;
    employment = d3.select("#employment").node().value;
    property = d3.select("#property").node().value;
    marital_status = d3.select("#marital_status").node().value;
    income_source = d3.select("#income_source").node().value;
    occupation = d3.select("#occupation").node().value;
    car = d3.select("#car").node().value;
    years_working = d3.select("#years_working").node().value;
    residence = d3.select("#residence").node().value;
    education = d3.select("#education").node().value;
    income = d3.select("#income").node().value;
    cc_active_time = d3.select("#cc_active_time").node().value;
    num_children = d3.select("#num_children").node().value;
    size_family = d3.select("#size_family").node().value;
    
    if (num_children > 3) {
        num_children = 3;
      }

      if (size_family > 4) {
        size_family = 4;
      }


    data_json = {
        'Gender': gender, 
        'Own_car': car,
        'Own_property': property, 
        'Unemployed': employment, 
        'Num_children': parseInt(num_children),
        'Num_family': parseInt(size_family),
        'Account_length': parseInt(cc_active_time), 
        'Total_income': parseFloat(income)*6,
        'Age': parseInt(age), 
        'Years_employed': parseInt(years_working),
        'Income_type': income_source, 
        'Education_type': education, 
        'Family_status': marital_status, 
        'Housing_type': residence,
        'Occupation_type': occupation,
    }
    return data_json;
    
}

function make_predictions(payload) {

    $.ajax({
        type: "POST",
        url: "/makePredictions",
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