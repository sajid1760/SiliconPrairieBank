import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():

    def __init__(self):
        pass

    def makePredictionss(self, data):
        gender_dict = {'Male': 1, 'Female': 0}
        yes_no_dict = {'Yes': 1, 'No': 0}
        occupation_type_dict = {'Other': 'Other', 'Labor': 'Laborers', 'Sales': 'Sales staff',
                                'Core Staff': 'Core staff',
                                'Manager': 'Managers',
                                'Transport': 'Drivers',
                                'High Skill Technology': 'High skill tech staff',
                                'Accountant': 'Accountants',
                                'Medical Staff': 'Medicine staff',
                                'Kitchen Services': 'Cooking staff',
                                'Security': 'Security staff',
                                'Cleaning Services': 'Cleaning staff',
                                'Private Services': 'Private service staff',
                                'Low-skill Labor': 'Low-skill Laborers',
                                'Secretary': 'Secretaries',
                                'Waiter/Bartender': 'Waiters/barmen staff',
                                'Human Resources': 'HR staff',
                                'Information Technology': 'IT staff',
                                'Realtor': 'Realty agents' }
        education_type_dict = {'Secondary': 'Secondary / secondary special',
                                'College Graduate': 'Higher education',
                                'Some College': 'Incomplete higher',
                                'Lower Secondary': 'Lower secondary',
                                'Post-Graduate Degree': 'Academic degree'}
        family_status_dict = {'Married': 'Married', 'Single': 'Single / not married', 'Civil Marriage': 'Civil marriage', 'Separated': 'Separated',
                            'Widowed': 'Widow'}
        housing_type_dict = {'Own House/Apartment': 'House / apartment',
                            'With Parents': 'With parents',
                            'Municipal Apartment': 'Municipal apartment',
                            'Rented Apartment': 'Rented apartment',
                            'Office Apartment': 'Office apartment',
                            'Co-op Apartment': 'Co-op apartment'}
        
        one_hot_cols = ['Income_type_Commercial associate', 'Income_type_Pensioner',
        'Income_type_State servant', 'Income_type_Student',
        'Income_type_Working', 'Education_type_Academic degree',
        'Education_type_Higher education', 'Education_type_Incomplete higher',
        'Education_type_Lower secondary',
        'Education_type_Secondary / secondary special',
        'Family_status_Civil marriage', 'Family_status_Married',
        'Family_status_Separated', 'Family_status_Single / not married',
        'Family_status_Widow', 'Housing_type_Co-op apartment',
        'Housing_type_House / apartment', 'Housing_type_Municipal apartment',
        'Housing_type_Office apartment', 'Housing_type_Rented apartment',
        'Housing_type_With parents', 'Occupation_type_Accountants',
        'Occupation_type_Cleaning staff', 'Occupation_type_Cooking staff',
        'Occupation_type_Core staff', 'Occupation_type_Drivers',
        'Occupation_type_HR staff', 'Occupation_type_High skill tech staff',
        'Occupation_type_IT staff', 'Occupation_type_Laborers',
        'Occupation_type_Low-skill Laborers', 'Occupation_type_Managers',
        'Occupation_type_Medicine staff', 'Occupation_type_Other',
        'Occupation_type_Private service staff',
        'Occupation_type_Realty agents', 'Occupation_type_Sales staff',
        'Occupation_type_Secretaries', 'Occupation_type_Security staff',
        'Occupation_type_Waiters/barmen staff']
        final_cols = ['Gender', 'Own_car', 'Own_property', 'Unemployed', 'Num_children',
        'Num_family', 'Account_length', 'Total_income', 'Age', 'Years_employed',
        'Income_type_Commercial associate', 'Income_type_Pensioner',
        'Income_type_State servant', 'Income_type_Student',
        'Income_type_Working', 'Education_type_Academic degree',
        'Education_type_Higher education', 'Education_type_Incomplete higher',
        'Education_type_Lower secondary',
        'Education_type_Secondary / secondary special',
        'Family_status_Civil marriage', 'Family_status_Married',
        'Family_status_Separated', 'Family_status_Single / not married',
        'Family_status_Widow', 'Housing_type_Co-op apartment',
        'Housing_type_House / apartment', 'Housing_type_Municipal apartment',
        'Housing_type_Office apartment', 'Housing_type_Rented apartment',
        'Housing_type_With parents', 'Occupation_type_Accountants',
        'Occupation_type_Cleaning staff', 'Occupation_type_Cooking staff',
        'Occupation_type_Core staff', 'Occupation_type_Drivers',
        'Occupation_type_HR staff', 'Occupation_type_High skill tech staff',
        'Occupation_type_IT staff', 'Occupation_type_Laborers',
        'Occupation_type_Low-skill Laborers', 'Occupation_type_Managers',
        'Occupation_type_Medicine staff', 'Occupation_type_Other',
        'Occupation_type_Private service staff',
        'Occupation_type_Realty agents', 'Occupation_type_Sales staff',
        'Occupation_type_Secretaries', 'Occupation_type_Security staff',
        'Occupation_type_Waiters/barmen staff']
        
        data2 = [data]
        df = pd.DataFrame(data2)
        
        df.loc[0, 'Gender'] = gender_dict[df.loc[0, 'Gender']]
        df.loc[0, 'Own_car'] = yes_no_dict[df.loc[0, 'Own_car']]
        df.loc[0, 'Own_property'] = yes_no_dict[df.loc[0, 'Own_property']]
        df.loc[0, 'Unemployed'] = yes_no_dict[df.loc[0, 'Unemployed']]
        
        df.loc[0, 'Education_type'] = education_type_dict[df.loc[0, 'Education_type']]
        df.loc[0, 'Family_status'] = family_status_dict[df.loc[0, 'Family_status']]
        df.loc[0, 'Housing_type'] = housing_type_dict[df.loc[0, 'Housing_type']]
        df.loc[0, 'Occupation_type'] = occupation_type_dict[df.loc[0, 'Occupation_type']]
        
        df_categ = df.loc[:, ['Income_type', 'Education_type', 'Family_status', 'Housing_type', 'Occupation_type']]
        df_numerical = df.loc[:, ['Gender', 'Own_car', 'Own_property', 'Unemployed', 'Num_children',
                                'Num_family', 'Account_length', 'Total_income', 'Age', 'Years_employed']]
        df_categ_one_hot = pd.get_dummies(df_categ)
        df_ready = pd.concat([df_numerical, df_categ_one_hot], axis=1)
        
        for col in one_hot_cols:
            if col not in df_ready.columns:
                df_ready[col] = 0
        
        cols = ['Gender', 'Own_car', 'Own_property', 'Unemployed']
        for col in cols:
            df_ready[col] = df_ready[col].astype('int')

        final_values = []
        for col in final_cols:
            final_values.append(df_ready.loc[0, col])

        # final_values = [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00,
        #                 1.54114853e+00, 3.31172280e+00, 1.15062176e+01, 1.48500000e+05,
        #                 3.17934748e+01, 3.00187765e+00, 0.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 2.29425734e-01, 0.00000000e+00, 7.70574266e-01,
        #                 0.00000000e+00, 7.70574266e-01, 0.00000000e+00, 2.29425734e-01,
        #                 0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 2.29425734e-01, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00, 7.70574266e-01, 0.00000000e+00,
        #                 0.00000000e+00, 0.00000000e+00]
        
        final_values = [final_values]
        
        pickled_model = pickle.load(open('lgb_cc_model.pkl', 'rb'))
        pred = pickled_model.predict(final_values)
        prob = pickled_model.predict_proba(final_values)
        rpred = int(pred[0])
        rprob = round(prob[0][rpred],2)
        print(f'Prediction: {rpred}  Probability: {rprob}')
        return [rpred, rprob]