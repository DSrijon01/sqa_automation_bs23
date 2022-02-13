from appium import webdriver
import pytest
import allure
import openpyxl


desired_cap = {
  "automationName": "UiAutomator2",
  "platformName": "Android",
  "appium:app": "C:\\Users\\BS726\\Downloads\\emi-calculator.apk",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.continuum.emi.calculator",
  "appium:appWaitActivity": "com.finance.emicalci.activity.AdActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_id('com.continuum.emi.calculator:id/btnStart').click()

# Getting Data from Excel Files
def get_data():

  workbook = openpyxl.load_workbook(r"C:\Users\BS726\Desktop\Allure-Test-Report\data_for_emi.xlsx")
  sheet = workbook["Sheet1"]
  totalrows = sheet.max_row
  totalcolums = sheet.max_column
  mainList = []


  for i in range(2,totalrows+1):
    dataList = []
    for j in range(1, totalcolums+1):
      data = sheet.cell(row=i, column=j).value
      dataList.insert(j,data)
    mainList.insert(i,dataList)
  return mainList



@pytest.mark.parametrize("ammount,interest,periody,periodm,pfee", get_data())
@allure.testcase('Emi-cal Test Solution')
def test_case(ammount,interest,periody,periodm,pfee):

    ## Enter Values In the Ammount Filed
    search_element_ammount = driver.find_element_by_id('com.continuum.emi.calculator:id/etLoanAmount')
    search_element_ammount.send_keys(ammount)

    ##Enter Value in the interest field
    search_element_interest = driver.find_element_by_id('com.continuum.emi.calculator:id/etInterest')
    search_element_interest.send_keys(interest)

    ##Enter Values in the period field - (YEARS)
    search_element_period_year = driver.find_element_by_id('com.continuum.emi.calculator:id/etYears')
    search_element_period_year.send_keys(periody)

    ##(Months)
    search_element_period_month = driver.find_element_by_id('com.continuum.emi.calculator:id/etMonths')
    search_element_period_month.send_keys(periodm)

    ## Enter Values in the processing Fees Section
    search_element_fee = driver.find_element_by_id('com.continuum.emi.calculator:id/etFee')
    search_element_fee.send_keys(pfee)

    ##Click the Calcualte Button
    driver.find_element_by_id('com.continuum.emi.calculator:id/btnCalculate').click()

    ## Click Reset Button to load Other Values
    driver.find_element_by_id('com.continuum.emi.calculator:id/btnReset').click()

    ## 30 seconds wait again
    driver.implicitly_wait(30)


