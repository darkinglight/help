#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

import json
import requests

def biz_test(url):
    headers = {}
    params = {
        'asset':{
            'item_no':'testlight007',
            'type':'hospital',
            'name':'test001',
            'period_type':'month',
            'period_count':3,
            'repayment_type':'equal',
            'fee_rate':0,
            'interest_rate':0,
            'secure_rate':0,
            'manage_rate':0,
            'withhold_rate':0,
            'withhold_multi_period':0,
            'amount':10000,
            'first_channel':'DSQ',
            'second_channel':'',
            'province_district_code':'210000',#辽宁省
            'city_district_code':'210300',#鞍山市
            'due_at':'1000-01-01',
            'first_payat':'1000-01-01',
            'payoff_at':'1000-01-01',
            'grant_at':'1000-01-01',
            'sign_at':'1000-01-01',
            'secure_amount':0,
            'interest_amount':0
        },
        'borrower':{
            'name':'名字电费',
            'idnum':'330225198901144038',
            'gender':'m',
            'residence':'这是住址',
            'workplace':'',
            'tel':'18668599634',
            'mate_name':'',
            'mate_tel':'',
            'relative_name':'',
            'relative_tel':'',
            'relative_relation':'',
            'workmate_name':'',
            'workmate_tel':'',
        },
        'repayer':{
            'name':'名字电费',
            'idnum':'330225198901144038',
            'gender':'m',
            'residence':'这是住址',
            'workplace':'',
            'tel':'18668599634',
            'mate_name':'',
            'mate_tel':'',
            'relative_name':'',
            'relative_tel':'',
            'relative_relation':'',
            'workmate_name':'',
            'workmate_tel':'',
        },
        'borrow_enterprise':{
            'name':'某某某企业名字',
            'license':'12313324324',
            'office_addr':'moumou企业地址',
            'contact':'faren',
            'tel':'15022384657',
            'legal_person':'',
            'legal_person_tel':'',
            'legal_person_num':'',
            'contact_backup':'',
            'tel_backup':'',
        },
        'repay_card':{
            'bankname':'中国工商银行',
            'username':'light',
            'phone':'18668566047',
            'individual_idnum':'330225198801144038',
            'credentials_type':'0',
            'credentials_num':'330225198801144038',
            'account_type':'debit',
            'account_num':'6222021001116245702',
        },
        'receive_card':{
           'name':'分行名',
           'type':'enterprise',
           'owner_id':'12312392394',
           'owner_name':'收款企业名啊啊啊',
           'num':'6222021001116245702',
           'bank':'招商银行',
           'account_name':'账户名',
        },
        'dtransactions':[
            {
                'dtransaction_type':'repayprincipal',
                'dtransaction_amount':'10000.00',
                'dtransaction_period':'1',
                'dtransaction_expect_finish_time':'2016-08-07',
            },
        ],
    }
    req = requests.post(url, headers=headers, data=json.dumps(params))
    req.encoding = 'utf-8'
    print(req.text)

if __name__ == '__main__':
    #url = "http://bizapi/asset/sync";
    url = "http://test.bizapi4.so/asset/sync";
    biz_test(url)
