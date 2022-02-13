# sqa_automation_bs23
Test Automation Project BS23

Project Goal 

## Create automated scripts to test EMI Calculater mobile app

App file is located
at [Download APK File From Here](https://drive.google.com/file/d/1l4IQCf0XJfMk1nlHhKn3u8PgX3iI8LY7/view?usp=sharing)

### Key functionalities, that have to be covered:

1. Open EMI calculator
2. Navigate to the EMI Calculator screen
3. Enter <*loan*> in the amount field
4. Enter <*interest*> percent rate in the interest field
5. Enter <*period*> in the period field in years
6. Enter <*pFee*> percent for the processing fee
7. And tap on the calculate button
8. Then Verify that the detail results are correct <*mEMI*>, <*tInterest*>, <*tpFee*> and <*tPayment*>

#### Examples:

| loan    | interest | period | pFee | mEMI  | tInterest | tpFee | tPayment |
|---------|----------|--------|------|-------|-----------|-------|----------|
|  100000 |  9.0     |  2     |  2.0 |  4568 |  9643     |  2000 |  109643  |
|  325000 |  9.5     |  5     |  1.5 |  6826 |  84536    |  4875 |  409536  |
|  450000 |  11.0    |  7     |  1.8 |  7705 |  197228   |  8100 |  647228  |

### Additional functionalities, that may be covered:

1. The more, the better. Only if it makes sense. Use your imagination and write some additional tests if you feelyou can cover other important functionalities.
2. Please include any third party test reporting tools(Ex. Extent Report, Allure report) in your automation project.
3. Please use Example table data to create excel/csv file as external test data provider and your automation script have the abitlity to read and write data from excel/csv


### Using automation framework is a must:

You can feel free to choose the framework, that suits you best, along with the python programming language.

### Record a video of tests execution:

Record a video to show how your tests are interacting with the mobile app(In Emulator). Attach the video as part of your solution.
