import pandas as pd
import pickle
import numpy as np

class ModelHelperld():

    def __init__(self):
        pass

    def makePredictionssld(self, data):

        own_home_dict = {'Rent': 'RENT', 'Mortgage': 'MORTGAGE', 'Own': 'OWN', 'Other': 'OTHER'}

        purpose_dict = {'Car': 'car', 'Credit Card': 'credit_card', 'Debt Consolida': 'debt_consolidation', 'Educational': 'educational',
                        'Home Improveme': 'home_improvement', 'House': 'house', 'Major Purchase': 'major_purchase', 'Medical': 'medical',
                        'Moving': 'moving', 'Other': 'other', 'Small Business': 'small_business', 'Vaca': 'vacation', 'Wedding': 'wedding'}

        fed_reserve_dict = {'1':['ME','VT', 'NH', 'MA', 'CT', 'RI'],
                            '2':['NY'],
                            '3':['PA', 'NJ'],
                            '4':['OH'],
                            '5':['MD', 'DE', 'VA', 'WV', 'NC', 'SC', 'DC'],
                            '6':['FL', 'TN', 'GA', 'AL', 'MS'],
                            '7':['MI', 'WI', 'IL', 'IN', 'IA'],
                            '8':['AR', 'MO', 'KY'],
                            '9':['MN', 'ND', 'SD', 'MT'],
                            '10':['WY', 'CO', 'KS', 'NE', 'OK'],
                            '11':['TX', 'NM', 'LA'],
                            '12':['CA', 'AZ', 'NV', 'OR', 'WA', 'ID', 'UT', 'HI', 'AK']}

        final_cols = ['loan_amnt', 'term', 'int_rate', 'sub_grade', 'emp_length', 'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths',
                        'open_acc', 'revol_bal', 'revol_util', 'total_acc', 'pub_rec_bankruptcies', 'last_credit_pull_d_int', 'home_ownership_MORTGAGE',
                        'home_ownership_OTHER', 'home_ownership_OWN', 'home_ownership_RENT', 'purpose_car', 'purpose_credit_card', 'purpose_debt_consolidation',
                        'purpose_educational', 'purpose_home_improvement', 'purpose_house', 'purpose_major_purchase', 'purpose_medical', 'purpose_moving',
                        'purpose_other', 'purpose_small_business', 'purpose_vacation', 'purpose_wedding', 'fed_reserve_region_1', 'fed_reserve_region_2',
                        'fed_reserve_region_3', 'fed_reserve_region_4', 'fed_reserve_region_5', 'fed_reserve_region_6', 'fed_reserve_region_7',
                        'fed_reserve_region_8', 'fed_reserve_region_9', 'fed_reserve_region_10', 'fed_reserve_region_11', 'fed_reserve_region_12']

        fed_reserve_inv_dict ={}
        for key in list(fed_reserve_dict.keys()):
            for state in fed_reserve_dict[key]:
                fed_reserve_inv_dict[state] = key

        grade_list = ['A', 'B', 'C', 'D', 'E','F','G']
        grade_dict = dict(zip(grade_list, list(range(1,8))))

        data2 = [data]
        df = pd.DataFrame(data2)

        df.loc[0, 'state'] = fed_reserve_inv_dict[df.loc[0, 'state']]
        df = df.rename(columns={'state': 'fed_reserve_region'})
        df.loc[0, 'home_ownership'] = own_home_dict[df.loc[0, 'home_ownership']]
        df.loc[0, 'purpose'] = purpose_dict[df.loc[0, 'purpose']]
        df.loc[0, 'sub_grade'] = str(grade_dict[df.loc[0, 'sub_grade'][0]]) + df.loc[0, 'sub_grade'][1]
        df.loc[0, 'last_credit_pull_d_int'] = ''.join(df.loc[0, 'last_credit_pull_d_int'].split('-'))

        object_cols = ['home_ownership', 'purpose', 'fed_reserve_region']
        df_categ = df.loc[:, object_cols]
        df_numerical = df.drop(object_cols, axis=1)

        df_categ_one_hot = pd.get_dummies(df_categ)
        df_ready = pd.concat([df_numerical, df_categ_one_hot], axis=1)

        for col in final_cols:
                if col not in df_ready.columns:
                    df_ready[col] = 0

        final_values = []
        for col in final_cols:
            final_values.append(df_ready.loc[0, col])
        final_values = [final_values]

        pickled_model = pickle.load(open('ld_approval_model_rf2.pkl', 'rb'))
        pred = pickled_model.predict(final_values)
        prob = pickled_model.predict_proba(final_values)
        rpred = int(pred[0])
        rprob = round(prob[0][rpred],2)
        print(f'Prediction: {rpred}  Probability: {rprob}')
        # rpred = 0
        # rprob = 0.72
        return [rpred, rprob]