# Description
In Taiwan, the latest iPhone usually solded out after Apple Event. If you don't order iPhone at the first time, you need to wait it after a month.
However, Apple will update the status of availability. We want to know whether iPhone in stock through code with crontab. We will receive a LINE message 
if iPhone is available.

# Setting
1. Add ChromeDriver into Project Folder

    1. Go to https://chromedriver.chromium.org/
    2. Download ChromeDriver with relative version

2. Obtain LINE Token

    1. Log in https://notify-bot.line.me/zh_TW/
    2. click personal page
    3. click generate token
    4. paste your token into `config.ini` 
    
3. Modify Absolute Path

    1. modify absolute path for `config_path` and `chromedriver_path` in `where_is_my_iPhone.py`
    2. modify absolute path of `python` and `where_is_my_iPhone.py` in `run.sh`
    
4. Add `run.sh` to crontab
    
    1. command `crontab -e`
    2. add new schedule using `*/1 * * * * bash /Users/hau/Documents/Python/iPhone_in_Stock/run.sh`
    3. do the bash at every minute
