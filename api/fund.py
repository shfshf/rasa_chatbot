import requests
import json
import codecs


API = 'http://fund.eastmoney.com/api/FundGuide.aspx?'
'''
dt=0&ft=gp&sd=&ed=&sc=z&st=desc&pi=1&pn=20&zf=diy&sh=list&rnd=0.7248546315993467
dt: 0
ft: gp,hh,zq,zs,qdii,fof,bb #基金类型
rs: 1y,20_jn,50_6y,20 #基金业绩
sd: 
ed: 
cp: 80000222 #公司
tp: 964deab6bb6bb363 #基金主题
rt: sz,5_zs,5_ja,5 #机构评级
se: 10 #基金规模
nx: 3 #成立年限
sc: 6y # 排序指标
st: desc # 排序方向
pi: 1
pn: 20
zf: diy
sh: list,table #展示方式
rnd: 0.726573364945424
'''

DEFAULT_PARAMS = {
    'dt': 0,
    'sd': '',
    'ed': '',
    'sc': 'z',
    'st': 'desc',
    'pi': 1,
    'pn': 20,
    'zf': 'diy',
    'sh': 'list',
    'rnd': 0.3874453763350052
}

slot_key = {
    'fund_type': 'ft',
    'fund_company': 'cp',
    'fund_topic': 'tp',
    'fund_achievement_duration': 'rs',
    'fund_achievement_topk': 'rs',
}

slot_value = json.load(codecs.open(
    './api/FundGuide_metadata.json', 'r', encoding='utf-8'))


def slots2params(slots,raw_value=True):
    params = {}

    for k, v in slots.items():
        short_key = slot_key[k]
        if v != '':
            if short_key not in params.keys():
                params.update({short_key: slot_value[short_key][v] if not raw_value else v})
            else:
                params.update(
                    {short_key: str(params[short_key])+','+str(slot_value[short_key][v] if not raw_value else v)})
    return '&'.join([f'{k}={v}' for k, v in DEFAULT_PARAMS.items()] +
                    [f'{k}={v}' for k, v in params.items()])


class FundSearch(object):
    '''
    Api for tiantian fund filter
    '''

    def __init__(self,):
        self.api_name = 'FundGuide'

    def info(self, **info):
        return self.api_name+':'+info.__str__()

    def search(self, slots, raw_value=True):
        for k, v in slots.items():
            if isinstance(v, list):
                slots.update({k: v[0]})
            if v == None:
                slots.update({k: ''})
        get_params = slots2params(slots, raw_value)
        response = requests.get(API+get_params)
        response_json = json.loads(response.text[14:])
        return response_json['datas'][0].split(',')[1]


if __name__ == '__main__':
    results = FundSearch().search({
        'fund_type': '股票型',
        'fund_company': '易方达',
        #'fund_topic':'',
        # params.update({short_key:slot_value[short_key][v]})  KeyError: ''
        #'fund_achievement_duration':'jn',
        #'fund_achievement_topk':'100'
        #   params.update({short_key:slot_value[short_key][v]}) KeyError: 'rs'
    })
    print(results)
