from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from sys import exit
import time
import sys
chrome_options = Options()
chrome_options.add_argument("--headless")
import gabbage_remover
#from verify_email import verify_email
sys.setrecursionlimit(200000)
import time
import os
from datetime import datetime
start_time =  time.asctime(time.localtime(time.time()))

marketing = 'https://mcscglobal.org/wp-admin/admin.php?page=sp-emails&view=edit&emailID=1149'
deferred_reminder ='https://mcscglobal.org/wp-admin/admin.php?page=sp-emails&view=edit&emailID=749'
event_reminder = 'https://mcscglobal.org/wp-admin/admin.php?page=sp-emails&view=edit&emailID=1079'

def word_press():

    chrome = webdriver.Chrome(executable_path=os.path.abspath("/home/ben/anaconda3/bin/chromedriver"),   chrome_options=chrome_options)
   #'C:/Users/Ben/AppData/Local/Programs/Python/Python37-32/Scripts/chromedriver.exe')
    chrome.get(marketing) #'https://mcscglobal.org/wp-admin/admin.php?page=sp-emails&view=edit&emailID=754')
    chrome.find_element_by_id("user_login").send_keys(username)
    chrome.find_element_by_id("user_pass").send_keys(password)
    chrome.find_element_by_id("user_pass").send_keys(Keys.RETURN)
    return chrome

def correct_name(n, browser, name):
    val = browser.find_element_by_xpath('html/body/table/tbody/tr[1]/td[3]/p[{}]'.format(n)).text
    if val and val =='Dear {},'.format(name):
        return
    elif val and val !='Dear {},'.format(name):
            browser.execute_script('document.querySelector("#tinymce > table > tbody > tr:nth-child(1) > td.content > p:nth-child({})").innerHTML = "Dear {},"'.format(n,name))
            print('corrected', name)
    else:
        n +=1
        correct_name(n, browser, name)

def create_dict():
	names_and_emails_dict = dict()
	count = 0
	dt = raw_data.split('\n')
	for item in dt:
		if item != '':
			if '@' not in item:
				capLock = [w.capitalize() for w in item.split()]
				name = ' '.join(capLock)
				count= 0
			elif '@' in item:
				count += 1
				if count > 1:
					email = ''.join(item.split())
					name = '{}{}'.format(' ', name)
					names_and_emails_dict[name] = email
				else:
					email = ''.join(item.split())
					names_and_emails_dict[name] = email
			else:
				print('Error')
				names_and_emails_dict[name] = email
	#names_and_emails_dict[name] = email
	#result = gabbage_remover.remove_garbabe(names_and_emails_dict)
	print(len(names_and_emails_dict),names_and_emails_dict)
	return names_and_emails_dict

done= []

def send_using(browser, list_of_names, done):
    print("starting sending")
    previous_name = ''
    months = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'May': 'May', 'Jun': 'June',
              'Jul': 'July', 'Aug': 'August', 'Sep': 'September', 'Oct': 'October', 'Nov': 'November',
              'Dec': 'December', }
    count = 0
    timestamps = []
    verified = 0
    timeStr = time.strftime("%c")
    timeStr = '.'.join(timeStr.split(':'))
    #save = open('auto_send {}.txt'.format(timeStr), 'w')
    for name in list_of_names.keys():
        verified += 1

        if name: #verify_email(list_of_names[name])==True:
            browser.find_element_by_id("content_area_one_edit-tmce").click()
            time.sleep(2)
            browser.switch_to.frame("content_area_one_edit_ifr")
            #current_name = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[3]/div/p[2]/strong").text
            #previous_name= "Dear {},".format(previous_name)
            if count > 1:
                if name: #current_name != previous_name:
                    pass
                    #print('not the same')
                    #break
                    #print('current name',current_name)k
                    #print('previous name',previous_name)
            names = name
            name = name.split('"')
            name = ''.join(name)
            name = name.split('_')
            name = ' '.join(name)
            if '@' in name:
                print('check... \nemail address may be concatenated with name... \nexiting...')
                exit()
            rep = ''.join(name.strip().split())
            checker = ['found' if char.isnumeric() else '' for char in rep]
            #print(name.strip().split())
            if 'found' in checker:
                print('check... \nnumbers may be concatenated with name... \nexiting...')
                exit()
            #print(name)
            #name = name.split(' ')
            #name = [v.capitalize() for v in name]
            #name = ' '.join(name)
            previous_name = name
            if browser.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[3]/div/p[1]/strong').text != '{}, 2021'.format(months[time.asctime(time.localtime(time.time()))[4:7]] + time.asctime(time.localtime(time.time()))[
                                                                           7:10]):

                browser.execute_script('document.querySelector("#tinymce > table:nth-child(1) > tbody > tr > td.content > div > p:nth-child(1) > strong").innerHTML = "{}, 2022"'.format(months[time.asctime(time.localtime(time.time()))[4:7]] + time.asctime(time.localtime(time.time()))[
                                                                           7:10]))
            else:
                pass
            if 'Dear' in browser.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[3]/div/p[2]/strong').text.capitalize():

                count += 1
                salute = 'Dear'
                try:
                    pw = name.split(' ')
                    frst = pw[0] if pw[0] else pw[1]
                    if not frst:
                        frst = pw[2]
                    #print(frst)
                    re = frst.split(' ')
                    p = ''.join(re)
                    #print(p)
                    if p == p.upper():
                        salute = 'DEAR'
                        #print(salute)
                    elif p == p.capitalize():
                        salute = 'Dear'
                        #print(salute)
                    else:
                        salute = 'Dear'

                    if name[-1] == ',':
                        pass
                    else:
                        name = name+','
                    browser.execute_script('document.querySelector("#tinymce > table:nth-child(1) > tbody > tr > td.content > div > p:nth-child(2) > strong").innerHTML = "{} {}"'.format(salute,'Distinguished Awardee')) #name)) #'
                    #print(count + '\t\t\t'+ name + '\t\t\t\t\t' + list_of_names[name] + '\t\t\t\t\tDone\n')
                except:
                    print('failed 1st Attempt')
                    print('broken trial')
                    break
                    try:
                        browser.execute_script(
                            'document.querySelector("#tinymce > table > tbody > tr:nth-child(1) > td.content > p:nth-child(1)").innerHTML = "Dear {},"'.format(

                 +               name))
                        #print(count + '\t\t\t'+ name + '\t\t\t\t\t' + list_of_names[name] + '\t\t\t\t\tDone\n')
                    except:
                        print('f')
                        browser.quit()
            
            else:
                print('broken main link')
                break

                #save.close()
                browser.execute_script("alert(''{} letters have been sent successfully, but none of the lines in the iframe-letter were executed. Please check the letter and start from {}')".format(count, name))
                break
            #correct_name(1, browser, name)
            browser.switch_to.default_content()
            name = names
            browser.execute_script('document.querySelector(".sp-text").value = "{}"'.format(list_of_names[name]))
            browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[4]/button').send_keys(Keys.RETURN)
            now = datetime.now()
            timestamps.append(now)
            p = '{}'.format(now)
            print(count, name + '\t\t\t' + list_of_names[name] + '\t\t\tDone' , verified, 'verified','\t\t\t', time.asctime(time.localtime(time.time()))[4:10],'\t\t\t', p[10:],'\n')
            if count> 2:
                #print((timestamps[-1]-timestamps[-2]).total_seconds( ))
                if (timestamps[-1]-timestamps[-2]).total_seconds() < 2:
                    difference = (timestamps[-1]-timestamps[-2]).total_seconds()
                    print('difference:', difference, 'broken because of ineffective skipping')
                    break
            #v = 100-19-34
            #print(v)
            #print(len(harv))
            if count==(4000):
                end_time= time.asctime(time.localtime(time.time()))
                # '
                print('started at {}'.format(start_time))
                print('ended at {}'.format(end_time))
                print('completed')
                break
                return

    #save.close()
    done.append(list_of_names[name])
    #browser.execute_script("alert('{} letters have been sent successfully')".format(count))
    browser.quit()
import dict_1
bright = dict_1.bright

status = dict_1.status



def start():
    if status:
        print("Found members in mailing list... exiting...")
        exit()
    print(len(bright))
    global chrome
    chrome= word_press()
    send_using(chrome, bright, done)
#start()

#n = 0


def repeat(n, done, bright):
    while n<5:
        try:
            for item in done:
                bright.pop(item)
                print('removed', len(done),'done', done)
            done = []
            print('restarting')
            n += 1
            start(bright, done)
        except:
            repeat(n, done, bright)
#repeat(0, done, bright)
raw_data = dict_1.st
create_dict()


