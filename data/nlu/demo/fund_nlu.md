<!-- 20-30 unique expressions for each intent should be good for the beginning --> 
<!-- more confusable more expressions needed-->
## intent:greet  
- hi
- hey
- hello
- Hi
- Hello
- 你好
- 您好
- 喂
- 在么

## intent:thankyou
- thanks
- thankyou
- thanks very much
- 谢谢
- 十分感谢

## intent:goodbye
- bye
- see you
- goodbye
- 拜拜
- 再见
- 拜
- 退出
- 结束

## intent:fund_search_with_type
- 帮我推荐一只[股票型](fund_type)的。
- 帮我推荐一只[股票型基金](fund_type:股票型)。
- 帮我推荐一只[股基](fund_type:股票型)。

## synonym:货币型
- 货币型基金 
- 货基

## synonym:债券型
- 债券型基金 
- 债基


## intent:fund_search_with_company
- 帮我推荐一只[易方达](fund_company)的基金。

## intent:fund_search_with_topic
- 帮我推荐一只关于[2025规划](fund_topic)的基金。

## intent:fund_search_with_type_company
- 帮我推荐一只[嘉实](fund_company)的[混基](fund_type:混合型)。

## intent:fund_search_with_company_topic
- 帮我推荐一只[汇添富](fund_company)关于[5G概念](fund_topic:5G)的基金。



## regex:zipcode
- [0-9]{5}