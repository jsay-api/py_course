# coding: utf-8
# определение бота по USER_AGENT
user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

bots = ['Yandex', 'Google', 'Rambler', 'Aport', 'Yahoo', 'msnbot']
l = any(map(lambda bot: bot in user_agent, bots))
print l