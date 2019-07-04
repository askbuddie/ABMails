#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from termcolor import colored
import time,random,string,sys,os,platform

#----Texts----

banner_nocolor = \
'''
     ___         __      ____            __    ___    
    /   |  _____/ /__   / __ )__  ______/ /___/ (_)__ 
   / /| | / ___/ //_/  / __  / / / / __  / __  / / _ \\
  / ___ |(__  ) ,<    / /_/ / /_/ / /_/ / /_/ / /  __/
 /_/  |_/____/_/|_|  /_____/\__,_/\__,_/\__,_/_/\___/ 
                                         Mails v.1.0
 KEEP YOUR REAL E-MAIL CLEAN AND SECURE    
----------------------------------------    '''

list_color = ["yellow","red","blue","white","green","cyan","magenta"]

def banner():
	print(colored(banner_nocolor,random.choice(list_color)))

def help():
	print('\n Ask Buddie Mails 1.0 - (c) Ask Buddie')
	print(colored(' https://www.askbuddie.com','yellow'))
	print(colored('\n Usage: ./abmails.py [ Basic Option ] [ Optional Option(s) ]','magenta'))
	print('            Eg; ./abmails.py --receive -n -d')

	print(colored('\n     [ Basic Options ]\r\n','blue'))
	print(colored('      --receive     Allow you to receive temporary mails\n      --help        Show this options and exit\n      --about       About the program','cyan'))                                                                    
	print(colored('\n     [ Optional ]\r\n','blue'))
	print(colored('      -s,--save     Save the mails in a text file\n      -n,--cname    Set your custom username for email\n      -d,--cdomain  Set your custom domain name for email\n      -t,--ctime    Set your custom time to refresh\n','cyan'))
      
about = \
'''
 Ask Buddie Mails / ABMails helps you to create temporary or
 disposable e-mail with a certain lifetime.It does not require 
 registration so you can do anything instantly and save your precious 
 time. ABmails can be used to register on dubious sites,create social 
 media accounts and for many other purpose without using your
 real e-mail account.

 [USE ABMAILS AND KEEP YOUR REAL EMAIL AWAY FROM SPAM AND HACKS]

 ABMails uses two sites ;
 * https://www.temp-mail.org
 * https://www.mailsac.com
'''

features = \
'''
 1.ABMails can create e-mail with 11 different domains,ie;

 * @mailsac.com
 * @safe-planet.com
 * @fastair.info
 * @air-blog.com
 * @bizsearch.info
 * @skymailgroup.com
 * @eaglemail.top
 * @airsport.top
 * @theskymail.com
 * @planet-travel.club
 * @skymailapp.com

 2.Allow you to create an e-mail with custom name and domain.

 3.Instantly create a random e-mail with random name and domain.

 4.Allow you to save all mails received in a text file.
'''
askbuddie = \
'''
 ABMails is a program created by AskBuddie Open Source Program Teams.
 Ask Buddie is a technology community found in May 16, 2017. Since our 
 founding, we have been providing online solutions and guidance to our 
 users related to technology. Our mission is to create a large community
 of technology enthusiast people to provide support in less time. 

 Visit: www.askbuddie.com

 Join our community on Facebook: www.facebook.com/groups/askbuddie
 Like our Facebook page: www.facebook.com/askbuddie

 GitHub: https://github.com/askbuddie
'''
authors = \
'''
 Hemanta Pokharel
 Rohit Joshi
'''




#----Mailsac.org--- [This provide provides only one domain name ]

# Counting number of mails received on mailsac.com
def count_mails_mailsac():
	count = driver.find_element_by_css_selector('div.container-fluid > div.ng-scope > div > h3')
	count = count.text[0]
	return int(count)

# Searching mails on mailsac.com
def search_mails_mailsac(count):
    mails = []
    for i in range(int(count)):
        mail = {}
        mailDiv = driver.find_element_by_css_selector('tr:nth-child('+str(i+2)+') > td.col-xs-4')
        mailDiv.click()
        time.sleep(1)
        info = driver.find_element_by_css_selector('tr:nth-child('+str(i+2)+') > td.active.not-clickable > p').text.split("\n")
        mail['sender'] = info[0]
        mail['subject'] = info[1]
        mail['time'] = info[2]
        mail['msg'] = driver.find_element_by_css_selector('tr:nth-child('+str(i+2)+') > td.active.not-clickable > div.ng-binding.ng-scope > div').text
        mails.append(mail)
        i += 1
    return mails

#----Temp mail---- [ Temp-mail.org provides many domain ] 

# Counting number of mails received on temp-mail.org
def count_mails_tempmail():
    links = driver.find_elements_by_xpath("//a[@class='link']")
    count = len(links)
    return int(count)

# Searching mails on temp-mail.org
def search_mails_tempmail():
    inboxDiv = driver.find_element_by_class_name('inbox-dataList')
    mails = []
    buttons = inboxDiv.find_elements_by_xpath("//a[@class='link']")
    links = []
    for button in buttons:
        links.append(button.get_attribute('href'))
    for link in links:
        mail = {}
        driver.get(link)
        inboxdata = driver.find_element_by_class_name('inbox-data-content')
        mail['sender'] = inboxdata.find_element_by_css_selector('div.inbox-data-content > div.inbox-data-content-header > div.user-data-name > p:nth-child(3)').text
        mail['time'] = inboxdata.find_element_by_css_selector('div.inbox-data-content > div.inbox-data-content-header > div.user-data-time > div.user-data-time-data > span').text
        mail['subject'] = inboxdata.find_element_by_css_selector('div.inbox-data-content > div.user-data-subject > h4').text
        try:
            mail['msg'] = inboxdata.find_element_by_css_selector('div.inbox-data-content > div.inbox-data-content-intro > div > div > div').text
        except Exception:
            mail['msg'] = inboxdata.find_element_by_css_selector('div.inbox-data-content > div.inbox-data-content-intro > div > div ').text
        mails.append(mail)  
    return mails


#----Common Functions----

# Clearing terminal for windows and linux
def clean_terminal():
	operating_system = platform.system()
	if operating_system == "Linux":
		os.system("clear")

	elif operating_system == "Windows":
		os.system("cls") 		
	else:
		pass
    
# Generate random strings for username
def rand_str():	
	rand_string = ''.join([random.choice(string.ascii_letters ) for n in range(8)])
	return rand_string.lower()

# Text Animation
def text_anim(text,t):
    i = 0
    print(' '*25,end = '\r')
    for x in range (0,t*2):
        print(text+"{}".format("."*i+' '*(3-i)),end='\r')
        if i < 3:
            i += 1
        else:
            i = 0
        time.sleep(0.5)
    print(' '*25,end = '\r')

# Getting optional arguments only if -r/--receive is taken from Basic Options
arglist = []
for i in range(len(sys.argv)):
	arglist = arglist + [ sys.argv[i] ] 

if '--receive' in arglist :
	if '-s' in arglist or '--save' in arglist:
		save_mail = True
	else:
		save_mail = False
		
	if '-n' in arglist or '--cname' in arglist:
		custom_username = True
	else:
		custom_username = False
		
	if '-t' in arglist or '--ctime' in arglist:
		custom_time = True
	else:
		custom_time = False
	if '-d' in arglist or '--cdomain' in arglist:
		custom_domain = True
	else:
		custom_domain = False
else:
	save_mail = False
	custom_time = False
	custom_username = False
	custom_domain = False

# Print the received mails on screen
def print_mails(mails):
    for mail in mails:
        print("\nFrom: ",colored(mail['sender'],'red'))
        print("Time: ",colored(mail['time'],'blue'))
        print("                       ",colored(mail['subject'],'green'))
        print(colored('\n'+mail['msg'],'yellow'))
        print('_'*80)

# Select Domain
def select_domain():
        driver.get('https://temp-mail.org/en/option/change/')
        domains = [option.text for option in driver.find_elements_by_tag_name('option')]
        domains.append('@mailsac.com')

        print("\nList of available domains...")
        for i,domain in enumerate(domains):
                print("{}. {}".format(i+1,domain))
        d = input("\nChoose any one domain among above 1-10:- ")
        if d == '0':
                select_zero = True
        try:
                int(d)

        except Exception:
                return random.choice(domains)

        else:
                if int(d) in range(1,len(domains)+1):
                        return domains[int(d)-1] 
                else:
                        return random.choice(domains)
                        
# Random domain selection
def random_domain():
	driver.get('https://temp-mail.org/en/option/change/')
	domains = [option.text for option in driver.find_elements_by_tag_name('option')]
	domains.append('@mailsac.com')
	
	return random.choice(domains)


# Receiving mails main function
def receive_mail():

	
	# ASk for username if user want a custom username otherwise use random string
	if custom_username == True:
		username = input('\nEnter the  username for your email: ')
		if len(username) <= 0:
			username = rand_str()
	else:
		username = rand_str()
	
	# Ask for domain if user want a custom domain otherwise use one random domain
	if custom_domain == True:
		selected_domain = select_domain()
	else:
		selected_domain = random_domain()
	
	# Ask for refresh time if user want a custom refresh time
	if custom_time == True:
		rf = input("\nEnter the mail refresh time in seconds? ")
		
		try:
			int(rf)
		except Exception:
			refreshtime = 10
		else:
			refreshtime = int(rf)
	else:
		refreshtime = 10
		
	# Writing the received mails on a text file
	def write_mails(mails):
		with open(username+selected_domain,'w') as file:
			file.write('#Mails received on '+ username+selected_domain)
			for mail in mails:
				file.write("\n\nFrom: "+mail['sender'])
				file.write("\nTime: "+mail['time'])
				file.write("\nsubject: "+mail['subject'])
				file.write('\nMail: '+mail['msg']+'\n')
	
	clean_terminal()
	banner()
	print('\nYour temporary email is: ' + colored(username + selected_domain,'red'))
	print('\nAny mails received on this email will be shown here...\n')
	if save_mail == True:
		print(colored('[~] Press {ctrl+c} when done to stop the program and to save the mails in text file.\n','blue'))
	else:
		print(colored('[~] Press {ctrl+c} when done to stop the program.\n','blue'))
		
	try:
		# Receiving Mails
		refreshurl = 'https://temp-mail.org/en/option/refresh/'
	
		if selected_domain == '@mailsac.com':
			url = 'https://mailsac.com/inbox/'+username+'@mailsac.com'
		else:
		
			url = url = 'https://temp-mail.org/?email='+username+selected_domain
		driver.get(url)

		oldCount=0;changed=1
	
		while True:
			try:
				if selected_domain == '@mailsac.com':
					newCount = count_mails_mailsac()
				else:
					newCount = count_mails_tempmail()
			except Exception:
				print(colored('[!] Opps,something went wrong. Please check your internet connection or \ntry changing the domain.','red'))
				selected_domain = select_domain()
			
				clean_terminal()
				banner()
				print('\nYour temporary email is: ' + colored(username + selected_domain,'red'))
				print('\nAny mails received at your email will be shown here...\n')
				if save_mail == True:
					print(colored('[~] Press {ctrl+c} when done to stop the program and to save the mails in text file.\n','blue'))
				else:
					print(colored('[~] Press {ctrl+c} when done to stop the program.\n','blue'))
				continue
		
			if newCount != oldCount:
				changed = 1
				print(colored("\n[+] "+str(newCount-oldCount)+ " new mail found",'green'))
				work = 'fail'
				while work == 'fail':
					try:
						if selected_domain == '@mailsac.com':
							mails = search_mails_mailsac(newCount)
							work = 'done'
						else:
							mails = search_mails_tempmail()
							work = 'done'
					except Exception:
						print(colored('[!] Opps,something went wrong. Trying again.','red'))
						text_anim('Waiting',refreshtime)
						
					
				clean_terminal()
				banner()
				print('\nYour temporary email is: ' + colored(username + selected_domain,'red'))
				print('\nAny mails received on this email will be shown here...\n')
				if save_mail == True:
					print(colored('[~] Press {ctrl+c} when done to stop the program and to save the mails in text file.\n','blue'))
				else:
					print(colored('[~] Press {ctrl+c} when done to stop the program.\n','blue'))
				try :
					print('_'*80)
					print_mails(mails)
				except KeyboardInterrupt:
					pass
			else:
				'''mails = []'''
				print(colored("[-] No new mails found",'red'), end = '\r')
				time.sleep(2)
			oldCount = newCount
			text_anim('Refreshing',refreshtime)
			if selected_domain == '@mailsac.com':
				driver.refresh()
			else:
				driver.get(refreshurl)
		
	except KeyboardInterrupt:
		os.system('clear')
		banner()
		print('\n')
		try:
			if save_mail == True:
				write_mails(mails)
				changed = 0
				print(colored('[+] saving all received mails on '+username+selected_domain+'\n','magenta'))
		except Exception:
			print(colored('[-] Failled to save mails on '+username+selected_domain+'\n','red'))
		print(colored('[+] Visit Our Site: www.askbuddie.com\n[+] Join our community on Facebook: www.facebook.com/groups/askbuddie\n[+] Like our Facebook page: www.facebook.com/askbuddie\n[+] For more amazing projects: https://github.com/askbuddie','blue'))
		print(colored('\nThanks for using Ask Buddie Mails...\n\n','red'))


#----Argument Handling----

# Wrong input argument handling and help
if len(sys.argv) < 2 or len(sys.argv) > 6 or sys.argv[1] in ['-h','--help'] :
		clean_terminal()
		banner()
		help()

# About
elif sys.argv[1] == '--about':
	clean_terminal()
	banner()
	print(colored("\n\n About","yellow"))
	print(colored(" -----","yellow"))
	print(colored(about,"cyan"))
	
	print(colored("\n Features","yellow"))
	print(colored(" --------","yellow"))
	print(colored(features,"red"))
	
	print(colored("\n Ask Buddie","yellow"))
	print(colored(" ----------","yellow"))
	print(colored(askbuddie,'blue'))

	print(colored("\n Author","yellow"))
	print(colored(" ------","yellow"))
	print(colored(authors,"magenta"))

	

# Receive 
elif  '--receive' in arglist:
	clean_terminal()
	banner()
	try:
		print('\nPlease wait,we are setting up the things...\n')
		options = Options()
		options.headless = True
		driver = webdriver.Firefox(options = options)
                
	except KeyboardInterrupt:
		print(colored('\n       [Keyboard Interrupted]\n','red'))
		print(colored('[+] Visit Our Site: www.askbuddie.com\n[+] Join our community on Facebook: www.facebook.com/groups/askbuddie\n[+] Like our Facebook page: www.facebook.com/askbuddie\n[+] For more amazing projects: https://github.com/askbuddie','blue'))
		print(colored('\nThanks for using Ask Buddie Mails...\n\n','red'))
		exit()		
	receive_mail()

# Wrong arguments
else:
	clean_terminal()
	banner()
	help()

