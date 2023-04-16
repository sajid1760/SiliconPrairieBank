For credit card data:
 
	1.  "clean_data.csv" was exactly what we downloaded from Kaggle.
	2.  "credit_card_tableau.csv" was the data we used to create Tableau. It has names instead of numbers for the categorical data and 
		the columns are renamed.
	3.  "ml_read_credit_card.csv" is the final csv that we fed into the machine learning algorithms. This data fed into our pickle file 
		should generate our model results after a SMOTE operation and a 0.75:0.25 train-test split

For loan data:

	1.  "loan_data.csv" is the exact .csv file we downloaded from Kaggle. "Data_Dictionary" is an Excel file to help us understand the 111 columns
	2.  "loan_data1.csv" and "loan_data2.csv" are just checkpoint csvs we generated because the data cleaning involved a lot of steps
	3.  "loan_data_clean.csv" is the data cleaned and ready for one-hot coding to be applied.
	4.  "ml_read_loan_data.csv" is to be fed into our pickle model.
	5.  "loan_data_tableau_final.csv" was used to create our Tableau dashboard for the loan data.
	6.  "loan_data_states.csv" was used to create the percent-approval map for the Tableau Dashboard.

Machine Learning:

	1. The two big machine learning notebooks are "loan_data_transform_machine_learning" and "credit_card_machine_learning"