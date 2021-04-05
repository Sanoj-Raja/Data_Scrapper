This is Selenium Based Python Package. Which is used to scrap data from a site. It is a custom package built for a custom work. It automates the manual work and makes the copy paste work simple.


* Important Prerequisites 

1. You need to edit constants.py file.
    - You need to add username & password constants.py
    - You need to add Chromedriver path in constants.py

2. You have to download and use google chrome for this python package.

3. You have to download ChromeDriver according to you Computer OS & chrome version you are using.

4. After downloading run the chrome driver sucessfully one time before using data_scrapper.

Steps to use package.
    
    from data_scrapper.dataReaderAndWriter import FillDataInExcel 
    <!-- Import the package. -->

    dataCollector = FillDataInExcel()
    <!-- Create an instance of master class which perform all tasks. -->

    pathOfExcel = 'name_of_excel.xlsx'
    <!-- Path of raw data excel. Always keep the excel in same folder & excel should be always in xlsx form. -->
    createdExcelName = f'name_of_final_created_excel_{pathOfExcel}'
    <!-- Final created excel name. This excel will be created in same folder. -->

    dataCollector.readAndWriteRequiredCellText(pathOfExcel, columnOfRequiredElements=6, rowFromScrapingStarts=2, createdExcelName, totalThreads=20)
    * Note keep the totalTherads number lower according to you computer configuration recommended 10 or less.
    <!-- Call the method to start the execution. -->

By writing the above code you can start scraping the required data.


Features of Data Scrapper Package.

1. Make the copy paste work simple.
2. Threads has used to make the work 5x faster.
3. Auto pause and auto start scrapping while disconnected or connected to internet.
4. Saves the new excel with the given name in same folder.
5. Can scrap and save excel of 2000 Rows in 525.55 seconds or in less than 9 minutes.
