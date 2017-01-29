import re
source = u""""name":"M50 Interceptor","focus":"Racing \\/ Interception","description":"If you want to get from point A to point B as quickly as possible and with as much style as possible then ORIGIN\'s M50 is for you. Featuring supercharged engines that counter a tiny weapons loadout, the M50 is a ship for going FAST.","tagline":null,"url":"\\/pledge\\/ships\\/origin-m50\\/M50-Interceptor","manufacturer":{"id":"6","code":"ORIG","name":"Origin Jumpworks GmbH","known_for":"the 300i series","description":"The BMW of the Star Citizen universe.  Their craft are more expensive, sleeker looking status symbols, maybe more so than they\\u2019re worth?  They get numbers instead of names: \\u201cOrigin 300i,\\u201d\\"Origin 890 Jump,\\u201d \\u201cOrigin M50 Turbo,\\u201d etc.","media":[{"id":"312958","slug":"0ffygmebwd3t1","status":"P","time_modified":"2014-08-04 13:09:28","publish_start":null,"publish_end":null,"type":"I","tag_st"""

# print(source.encode('utf-8').decode('utf-8')) # converts unicode to utf-8 if leading unicode \ is not escaped: \\u2018

slashPat = r'(\\).{5}\1'

print(re.sub(slashPat, '', source))