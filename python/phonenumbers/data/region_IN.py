"""Auto-generated file, do not edit by hand. IN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IN = PhoneMetadata(id='IN', country_code=91, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{7,12}|[2-9]\\d{9,10}', possible_number_pattern='\\d{6,13}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:11|2[02]|33|4[04]|79)[2-6]\\d{7}|80[2-46]\\d{7}|(?:1(?:2[0-249]|3[0-25]|4[145]|[59][14]|6[014]|7[1257]|8[01346])|2(?:1[257]|3[013]|4[01]|5[0137]|6[0158]|78|8[1568]|9[14])|3(?:26|4[1-3]|5[34]|6[01489]|7[02-46]|8[159])|4(?:1[36]|2[1-47]|3[15]|5[12]|6[126-9]|7[0-24-9]|8[013-57]|9[014-7])|5(?:[136][25]|22|4[28]|5[12]|[78]1|9[15])|6(?:12|[2345]1|57|6[13]|7[14]|80)|7(?:12|2[14]|3[134]|4[47]|5[15]|[67]1|88)|8(?:16|2[014]|3[126]|6[136]|7[078]|8[34]|91))[2-6]\\d{6}|(?:(?:1(?:2[35-8]|3[346-9]|4[236-9]|[59][0235-9]|6[235-9]|7[34689]|8[257-9])|2(?:1[134689]|3[24-8]|4[2-8]|5[25689]|6[2-4679]|7[13-79]|8[2-479]|9[235-9])|3(?:01|1[79]|2[1-5]|4[25-8]|5[125689]|6[235-7]|7[157-9]|8[2-467])|4(?:1[14578]|2[5689]|3[2-467]|5[4-7]|6[35]|73|8[2689]|9[2389])|5(?:[16][146-9]|2[14-8]|3[1346]|4[14-69]|5[46]|7[2-4]|8[2-8]|9[246])|6(?:1[1358]|2[2457]|3[2-4]|4[235-7]|5[2-689]|6[24-58]|7[23-689]|8[1-6])|8(?:1[1357-9]|2[235-8]|3[03-57-9]|4[0-24-9]|5\\d|6[2457-9]|7[1-6]|8[1256]|9[2-4]))\\d|7(?:(?:1[013-9]|2[0235-9]|3[2679]|4[1-35689]|5[2-46-9]|[67][02-9]|9\\d)\\d|8(?:2[0-6]|[013-8]\\d)))[2-6]\\d{5}', possible_number_pattern='\\d{6,10}', example_number='1123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:2(?:0[04-9]|5[09]|7[5-8]|9[389])|3(?:0[13-9]|5[0-4789]|7[3679]|8[1-9]|9[689])|4(?:0[245789]|1[15-9]|[29][89]|39|8[389])|5(?:0[0-5789]|[47]9|[25]0|6[6-9]|[89][7-9])|6(?:0[027]|12|20|3[19]|5[45]|6[5-9]|7[679]|9[6-9])|7(?:0[27-9]|[39][5-9]|42|60)|8(?:[03][07-9]|14|2[7-9]|4[25]|6[09]|7\\d|9[013-9]))|8(?:0(?:[01589]\\d|66)|1(?:[024]\\d|1[56]|30|7[19]|97)|2(?:[2369]\\d|52|7[01357]|8[567])|3(?:0[235-8]|4[14789]|74|90)|4(?:[02-58]\\d|10|6[09])|5(?:0[079]|11|2\\d|30|4[47]|53|7[45]|9[015])|6(?:[0589]\\d|7[09])|7(?:1[24]|[2569]\\d)|8(?:[07-9]\\d|17|2[024-8]|44|5[389]|6[0167])|9(?:[057-9]\\d|2[35-9]|3[09]|4[036-8]|6[0-46-9]))|9\\d{3})\\d{6}', possible_number_pattern='\\d{10}', example_number='9123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:600\\d{6}|80(?:0\\d{4,8}|3\\d{9}))', possible_number_pattern='\\d{8,13}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='186[12]\\d{9}', possible_number_pattern='\\d{13}', example_number='1861123456789'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='1860\\d{7}', possible_number_pattern='\\d{11}', example_number='18603451234'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[0128]|12|298)|2611', possible_number_pattern='\\d{3,4}', example_number='108'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1(?:600\\d{6}|8(?:0(?:0\\d{4,8}|3\\d{9})|6(?:0\\d{7}|[12]\\d{9})))', possible_number_pattern='\\d{8,13}', example_number='1800123456'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{6})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7(?:2[0579]|3[057-9]|4[0-389]|5[024-9]|6[0-35-9]|7[03469]|8[0-4679])|8(?:0[01589]|1[0-479]|2[236-9]|3[0479]|4[0-68]|5[0-579]6[05789]7[12569]|8[0124-9]|9[02-9])|9', '7(?:2(?:0[04-9]|5[09]|7[5-8]|9[389])|3(?:0[13-9]|5[0-4789]|7[3679]|8[1-9]|9[689])|4(?:0[245789]|1[15-9]|[29][89]|39|8[389])|5(?:0[0-5789]|[47]9|[25]0|6[6-9]|[89][7-9])|6(?:0[027]|12|20|3[19]|5[45]|6[5-9]|7[679]|9[6-9])|7(?:0[27-9]|3[5-9]|42|60|9[5-9])|8(?:[03][07-9]|14|2[7-9]|4[25]|6[09]|7|9[013-9]))|8(?:0[01589]|1(?:[024]|1[56]|30|7[19]|97)|2(?:[2369]|7[01357]|8[567])|3(?:0[235-8]|4[14789]|74|90)|4(?:[02-58]|10|6[09])|5(?:0[079]|11|2|30|4[47]|53|7[45]|9[015])|6(?:[0589]|70)|7(?:1[24]|[2569])|8(?:[07-9]|17|2[024-8]|44|5[389]|6[0167])|9(?:[057-9]|2[35-9]|3[09]|4[03678]|6[0-46-9]))|9'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['11|2[02]|33|4[04]|79|80[2-46]'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1(?:2[0-249]|3[0-25]|4[145]|[569][14]|7[1257]|8[1346]|[68][1-9])|2(?:1[257]|3[013]|4[01]|5[0137]|6[0158]|78|8[1568]|9[14])|3(?:26|4[1-3]|5[34]|6[01489]|7[02-46]|8[159])|4(?:1[36]|2[1-47]|3[15]|5[12]|6[126-9]|7[0-24-9]|8[013-57]|9[014-7])|5(?:[136][25]|22|4[28]|5[12]|[78]1|9[15])|6(?:12|[2345]1|57|6[13]|7[14]|80)'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7(?:12|2[14]|3[134]|4[47]|5[15]|[67]1|88)', '7(?:12|2[14]|3[134]|4[47]|5(?:1|5[2-6])|[67]1|88)'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8(?:16|2[014]|3[126]|6[136]|7[078]|8[34]|91)'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1(?:[2-579]|[68][1-9])|[2-8]'], national_prefix_formatting_rule=u'0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1600)(\\d{2})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['160', '1600'], national_prefix_formatting_rule=u'\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1800)(\\d{4,5})', format=u'\\1 \\2', leading_digits_pattern=['180', '1800'], national_prefix_formatting_rule=u'\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(18[06]0)(\\d{2,4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['18[06]', '18[06]0'], national_prefix_formatting_rule=u'\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{4})(\\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['18[06]', '18(?:03|6[12])'], national_prefix_formatting_rule=u'\\1', national_prefix_optional_when_formatting=True)])
