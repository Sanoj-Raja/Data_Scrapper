from data_scrapper import constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Extractor:
    
    def start(self, siteUrl, isHeadless=True):
        self.siteUrl = siteUrl
        self.isHeadless = isHeadless        
        
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('detach', True)
        # Keeps the browser open if it quits by default.
        
        opt.add_argument('--no-sandbox') 
        # Solves the Error - unknown error: unable to discover open pages
        # Bypass OS security model. 
        
        opt.headless = self.isHeadless
        # Keeps the chrome invisible without heads.  
        
        # Sometime this (below given) error comes bydefualt so to remove this errror we have used while loop.
        # Solves the Error - unknown error: unable to discover open pages
        while True:
            try:
                self.browser = webdriver.Chrome(options=opt, executable_path=constants.chromeDriverPath)
                self.browser.get(self.siteUrl)
                
            except Exception as e:
                # Sometime while quiting browser another error comes that is 
                # AttributeError: 'Extractor' object has no attribute 'browser'
                # So to handle this we have used anothe try except block.
                try:
                    # sleep(1)
                    # print(f'There is an error: {e}')
                    self.isBrowserRunning = False
                    self.browser.quit()
                    
                except AttributeError as ae:
                    print(f'There is a Attributer Error : {ae}')
                    
                except Exception as e:
                    print(f'This is a custom errror line : {e}')
               
            else:
                self.isBrowserRunning = True
                return
            
        
    def extractRequiredFeildData(self, requiredInputText):
        if self.isBrowserRunning:
            
            # This is Resume Id.
            self.requiredInputText = requiredInputText
            
            while True:
                try:
                    self.rawDataList = self.extractor()
                    
                except Exception:
                    self.isRawDataScrapped = False
                    print(f'Error Occurred: Internet has been disconnected or Something went wrong.')
                    print('Waiting for internet...')
                    self.browser.refresh()
                
                else:                
                    # Finally returning the Raw Data List.
                    self.isRawDataScrapped = True
                    return self.rawDataList
                
                
    def extractor(self):
        self.searchBoxName = constants.searchBoxName
        self.detailsClassName = constants.detailsClassName
        
        # Finding & clearing the search box to fill the Resume Id. 
        self.searchBox = WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable((By.NAME, self.searchBoxName)))
        self.searchBox.clear()
        # currentTime1 = time.perf_counter()
        # if currentTime1 - startingTime > 10:
        #     raise Exception
        self.searchBox.send_keys(self.requiredInputText)
        self.searchBox.send_keys(Keys.RETURN)
        
        # Extracting the raw data List using class name after search & return a list of details.
        # self.browser.find_elements_by_class_name(self.detailsClassName) not working line.
        self.candidateDetailsList = WebDriverWait(self.browser, 3).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, self.detailsClassName))) 
        
        return self.candidateDetailsList

        
    def shutDownBrowser(self):
        try:
            self.browser.quit()
            # Quit will shut the chrome.
        except Exception as ex:
            print(f'Error occured while closing the Chrome. Error : {ex}')
        else:
            print("Quiting the chrome.\n")
    
    # Not in use. 
    def closeTheTab(self):
        print("Closing the current tab.")
        self.browser.close()
        # Close will close the current tab of chrome.
        