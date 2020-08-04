<img align="center" src="./assets/abmails.png" />

###  **KEEP YOUR REAL E-MAIL CLEAN AND SECURE**

:information_source: ABOUT
 -----
 Ask Buddie Mails / ABMails helps you to create temporary or
 disposable e-mail with a certain lifetime.It does not require 
 registration so you can do anything instantly and save your precious 
 time. ABmails can be used to register on dubious sites,create social 
 media accounts and for many other purpose without using your
 real e-mail account.

 ABMails uses two sites ;
 * https://www.temp-mail.org
 * https://www.mailsac.com
 
 ----------
 
:email: FEATURES
 --------
 1. ABMails can create e-mail with more than 10 different domains.

 2. Allow you to create an e-mail with custom name and domain.

 3. Instantly create a random e-mail with random name and domain.

 4. Allow you to save all mails received in a text file.
 
 ----------
 
 ##  :warning: Requirements

Selenium requires a driver to interface with the chosen browser.

## For Firefox
#### Firefox requires geckodriver, which needs to be installed .

  - Windows
    - Download and extract the zip file of [geckodriver](https://github.com/mozilla/geckodriver/releases)
     and copy geckodriver.exe file in c://windows.

  - Linux
    - Download and extract the zip file of [geckodriver](https://github.com/mozilla/geckodriver/releases)
     and copy the extracted file in /usr/bin or /usr/local/bin.
     Make sure to give executive permission to the geckodriver with the command;
     ```chmod +x geckodriver```


## For Chrome
#### Chrome requires chromedriver,which needs to be installed .

  - Windows
    - Download and extract the zip file of [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
     and copy chromedriver.exe file in c://windows.

  - Linux
    - Download and extract the zip file of [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
     and copy the extracted file in /usr/bin or /usr/local/bin.
     Make sure to give executive permission to the geckodriver with the command;
     ```chmod +x chromedriver```

----------

## :floppy_disk: Get Started

* clone this repo by typing this command in terminal

```bash
git clone https://github.com/askbuddie/ABMails.git
```

* you also have to install the dependencies for running ABMails by running

```bash
pip3 install -r requirements.txt
```

* when you have cloned the repo, simply run the .py file in terminal .

```bash
$ python3 abmails.py
```

now ABMails expects an arguments to be passed which defines what proccess you are doing.

### Arguments;
     
     [ Basic Options ]

      --receive     Allow you to receive temporary mails
      --help        Show this options and exit
      --about       About the program

     [ Optional ]

      -s,--save     Save the mails in a text file
      -n,--cname    Set your custom username for email
      -d,--cdomain  Set your custom domain name for email
      -t,--ctime    Set your custom time to refresh
      
You are supposed to pass only one argument from Basic options. Pass the optional
options if only '--receive' is taken from basic options. Optional options are 
optional arguments , you can leave it or pass it according to your wish.

```Usage: python3 abmails.py [ Basic Option ] [ Optional Option(s) ]```

> Eg: python3 abmails.py --receive -n -d

----------

## :heart: Contribution
You wanna contribute to the project? Great to hear that.

please refer to our Contribution Guide [here](./CONTRIBUTING.md)

 
----------
 
 :ab: ASK BUDDIE
 ----------
 ABMails is a program created by [AskBuddie Open Source Program](https://github.com/askbuddie) Teams.
 [Ask Buddie](https://www.askbuddie.com) is a technology community found in May 16, 2017. Since our 
 founding, we have been providing online solutions and guidance to our 
 users related to technology. Our mission is to create a large community
 of technology enthusiast people to provide support in less time. 

 [Join our community on Facebook](https://www.facebook.com/groups/askbuddie)

----------

## :octocat: Author

- **Ask Buddie**

-----------

## :octocat: Primary Contributor

- **[Hemant Pokharel]**
- https://github.com/Hemantapkh

----------

## :stars: Contributors
<table>
  <tr>
   <td align="center">
      <a href="https://github.com/Hemantapkh">
      <img src="https://avatars2.githubusercontent.com/u/58947310?s=460&v=4" width="100px;" alt="Hemanta Pokharel"/>
      <br />
      <sub><b>Hemanta Pokharel</b></sub></a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/joshirk11166">
      <img src="https://avatars2.githubusercontent.com/u/34398948?s=400&v=4" width="100px;" alt="Rohit Joshi"/>
      <br />
      <sub><b>Rohit Joshi</b></sub></a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/muna-kopila">
      <img src="https://avatars3.githubusercontent.com/u/51370579?s=400&v=4" width="100px;" alt="Muna Puri"/>
      <br />
      <sub><b>Muna Puri</b></sub></a>
      <br />
    </td>
    <td align="center">
      <a href="https://anuraghazra.github.io">
      <img src="https://avatars1.githubusercontent.com/u/35374649?s=460&v=3" width="100px;" alt="Anurag Hazra"/>
      <br />
      <sub><b>Anurag Hazra</b></sub></a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/ashiishme">
      <img src="https://avatars3.githubusercontent.com/u/18111862?s=460&v=3" width="100px;" alt="Ashish Yadav"/>
      <br />
      <sub><b>Ashish Yadav</b></sub></a>
      <br />
    </td>
   <td align="center">
      <a href="https://github.com/pr0d33p">
      <img src="https://avatars0.githubusercontent.com/u/29733866?s=460&v=4" width="100px;" alt="Pradeep Bhattarai"/>
      <br />
      <sub><b>Pradeep Bhattarai</b></sub></a>
      <br />
    </td>
  </tr>
</table>

-----------
 :heart: AskBuddie

