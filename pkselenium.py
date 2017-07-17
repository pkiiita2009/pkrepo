from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyautogui
import requests
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("http://www.printvenue.com")
driver.maximize_window()
time.sleep(15)
driver.switch_to_alert()
"""
below command click on cross button of sign up pop up

"""
try:
    driver.find_element_by_xpath("/html/body/div[11]/div/div/a").click()
except NoSuchElementException:
	print ("banner not found")
finally:

    time.sleep(5)

    try:
        driver.find_element_by_xpath("/html/body/div/div/span[3]").click()
    except NoSuchElementException:
	    print ("banner not found")
    finally:

		
		driver.switch_to_alert()

		"""
		find login and click on login

		"""
		driver.switch_to_default_content()
		time.sleep(10)
		driver.find_element_by_link_text("Login").click()
		driver.switch_to_alert()

		print ("i am trying to log in")
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #email").click()
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #email").clear()
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #email").send_keys("saurabh.chaturvedi@printvenue.com")
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #password").clear()
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #password").send_keys("12345")
		driver.find_element_by_css_selector("div.fancybox-inner > #user_fancybox_popup > div.login-panel > #login_popup_panel > section.login-pandel-lft > #login_popup_form > #login_form_popup > #submitsection > #_submit").click()
		driver.switch_to_default_content()

		time.sleep(5)
		print ("normal login successfully!!")

		"""
		now logout from account

		"""

		pyautogui.moveTo(1040, 120)
		pyautogui.click()
		time.sleep(3)
		pyautogui.moveTo(1040, 350)
		pyautogui.click()
		time.sleep(3)
		print (" logout successfully!!")

		driver.switch_to_default_content()
		time.sleep(10)
		driver.find_element_by_id("login_li").click()
		driver.switch_to_alert()

		"""
		Do login with credentials
		"""
		print ("i am trying to log in via google")

		time.sleep(5)

		driver.find_element_by_css_selector(".fancybox-inner > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > section:nth-child(3) > div:nth-child(2) > div:nth-child(2) > img:nth-child(1)").click()
		time.sleep(2)
		pyautogui.moveTo(650, 540)
		pyautogui.typewrite("pradeep.kumar@printvenue.com");
		pyautogui.moveTo(650, 580)
		pyautogui.click() 
		time.sleep(2)
		pyautogui.moveTo(650, 550)
		time.sleep(3)
		pyautogui.typewrite("Varanasi@123");
		pyautogui.moveTo(650, 590)
		pyautogui.click()
		print ("google login working fine")
		print ("lets check for search")


		url = "http://m.printvenue.com/m/search?search=pens"

		myResponse = requests.get(url)
		if(myResponse.ok):
		    jData = json.loads(myResponse.content)
		    if(len(jData['templatesWithOnlySearchTerm']['response']) == 3):
		        print "Search is fine"
		    else:
		    	print "Search broken"


		print ("click on business card")

		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main div.container.container_fixed div#flexinav1.flexinav.flexinav_fixed div.flexinav_wrapper ul.flexinav_menu li.flexnav_mega span.onscreen-menu.lft-mnu.mnu-hover a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main div.wrapper.clearfix div.wrapper.clearfix div.content.clearfix section.clearfix div ul.pro-new-ul li.pro-new-cat div a img#lazy-load-image-premium-business-cards.lazy").click()
		time.sleep(5)

		pyautogui.moveTo(450, 380)
		pyautogui.click() 
		time.sleep(8)
		driver.find_element_by_css_selector("html.no-js body#main div.tooltipster-base.tooltipster-punk.tooltipster-fade.tooltipster-fade-show div.tooltipster-content div.nav_btns a#safearea-ok-close").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main div.wrapper.clearfix form#formEditor div#editorcontainer div#rightEditor.right.upsell div.button-box button#proceed.rounded.button.btn-orange.buy.buy-loading").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main div.wrapper.clearfix form#formEditor div#editorcontainer div#rightEditor.right.upsell div.button-box button#buy.rounded.button.btn-orange.buy.tooltip").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main.fancybox-lock div.fancybox-overlay.fancybox-overlay-fixed div.fancybox-wrap.fancybox-desktop.fancybox-type-html.fancybox-opened div.fancybox-skin div.fancybox-outer div.fancybox-inner div.center button#confirm-approval.rounded.button.btn-blue").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main.fancybox-lock div.fancybox-overlay.fancybox-overlay-fixed div.fancybox-wrap.fancybox-desktop.fancybox-type-ajax.fancybox-opened div.fancybox-skin div.fancybox-outer div.fancybox-inner table tfoot tr td button.button.btn-blue").click()
		time.sleep(5)
		driver.find_element_by_css_selector("html.no-js body#main div#center div.wrapper div.suggestion.clearfix div.wrapper.clearfix div#cartvalue div.cart-wrapper div.crt_full_summry div.cart-rc div.cart-rc-contatint div.cart-proceed a.chkout-btn").click()
		time.sleep(8)
		driver.find_element_by_css_selector("html body#main div#center div.wrapper form#onestep_checkout_form div#one-step-checkout div#indexLoginArea.s-cartbase div#container-checkout div.column.information div#information.content div#shipping_section div.sp_shipping_left fieldset.shipping_address_selection div#checkout_onestep_payu_shippingAddress div.continue input#shipping-continue-btn.contCop").click()
		time.sleep(8)
		driver.find_element_by_css_selector("html body#main div#center div.wrapper form#onestep_checkout_form div#one-step-checkout div#indexLoginArea.s-cartbase div#container-checkout div.column.information div#payment.content div.sp-payment-tab-left div#PayTm-Wallet.pay-tab img").click()
		time.sleep(8)
		driver.find_element_by_css_selector("html body#main div#center div.wrapper form#onestep_checkout_form div#one-step-checkout div#indexLoginArea.s-cartbase div#container-checkout div.column.information div#payment.content div#blankPaymentTemplate.sp-payment-tab-right div.billing_section div.codplaceorder button#cod_order.placeOrderButton").click()
		time.sleep(5)
		print ("order successfull")

		fromaddr = 'pk.iiita2009@gmail.com'
		toaddrs  = 'saurabh.chaturvedi@printvenue.com'
		msg = 'Looks like Site Working fine!!!'
		SUBJECT = "Sanity report"
		TEXT = msg
		username = 'gmail username'
		password = 'gmale password'
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr,toaddrs,msg)
		server.quit()











