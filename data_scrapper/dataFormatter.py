from data_scrapper import constants

class DataFormatter:
    @staticmethod
    def formatter(dataList):
        # Key value pairs of candidate Details are stored in candidateDetailsDictionary.
        candidateDetailsDictionary = {}
        
        # Scraping 6 Index from row data that is Name, Email & Status
        # This is the 6 index of master data list which contains the name, email & user status.
        nameEmailAndStatus = dataList[6].text
        indexOfPipeInNameEmailAndStatus = nameEmailAndStatus.index("|", 0)
        
        # Sometimes '[' is present in the raw string. 
        if '[' in nameEmailAndStatus:
            indexOfFirstSquereBracketInNameEmailAndStatus = nameEmailAndStatus.index("[", 0)
        
            # Slicing the nameEmail&Staus we can get name and email & status details seprately. 
            candidateName = nameEmailAndStatus[0 : indexOfPipeInNameEmailAndStatus - 1]
            candidateEmail = nameEmailAndStatus[indexOfPipeInNameEmailAndStatus + 2 : indexOfFirstSquereBracketInNameEmailAndStatus]
            candidateStatus = nameEmailAndStatus[indexOfFirstSquereBracketInNameEmailAndStatus + 2 : -2]
        
            # Adding first 3 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.name] = candidateName    
            candidateDetailsDictionary[constants.emailId] = candidateEmail
            candidateDetailsDictionary[constants.status] = candidateStatus
                                            
        # Sometimes '[' not is present in the raw string and 
        if '[' not in nameEmailAndStatus:
            indexOfServicesDetailText = nameEmailAndStatus.index("Services Detail", 0)
            
            # Slicing the nameEmail&Staus we can get name and email & status details seprately. 
            candidateName = nameEmailAndStatus[0 : indexOfPipeInNameEmailAndStatus - 1]
            candidateEmail = nameEmailAndStatus[indexOfPipeInNameEmailAndStatus + 2 : indexOfServicesDetailText - 2]
        
            # Adding first 3 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.name] = candidateName
            candidateDetailsDictionary[constants.emailId] = candidateEmail
            candidateDetailsDictionary[constants.status] = 'Paid Member'    
        
        # Candidate Phone Number
        # Somtimes phone number is more than 10 digits. For example - 91^9898828288 or  ^9971516278. 
        # Some times 13 digits & some time 11 digits.
        candidatePhoneNumber = dataList[8].text
        
        if len(candidatePhoneNumber) == 10:
            candidateDetailsDictionary[constants.phoneNumber] = candidatePhoneNumber
            
        if len(candidatePhoneNumber) >= 11 and candidatePhoneNumber.find('^') != -1: 
            indexOfSymbolInPhoneNumber = candidatePhoneNumber.index('^', 0)
            correctedPhoneNumber = candidatePhoneNumber[indexOfSymbolInPhoneNumber + 1 : len(candidatePhoneNumber)]
            candidateDetailsDictionary[constants.phoneNumber] = correctedPhoneNumber
    
        # As sometimes ^ is not available in phone number but lenght of phone number is 11 or more.
        else: 
            candidateDetailsDictionary[constants.phoneNumber] = candidatePhoneNumber
        
        # Scraping 7 Index from row data that is Address, State, Country, Resume Uploads & Field.
        addressStateCountryNoOfResumeUploadsAndCandidateField = dataList[7].text.splitlines()
        
        # First Line - Address 
        # Second Line - State
        # Third Line - Country
        # Forth Line - Total Resume Uploads
        # Fifth Line - Field
        
        # Sometimes Adress is not available so it may casuse error.
        # Sometimes Fied is not available so it may casuse error.
        # We Don't need Total Resume Uploads as it doesnot make any sence for us.
        
        # If adress is provided in 2 lines. Sometimes address takes 2 lines.
        if len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 6:
            candidateAddress = addressStateCountryNoOfResumeUploadsAndCandidateField[0] + addressStateCountryNoOfResumeUploadsAndCandidateField[1]
            candidateState = addressStateCountryNoOfResumeUploadsAndCandidateField[2]
            candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[3]
            candidateField = addressStateCountryNoOfResumeUploadsAndCandidateField[5]
            
            # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.address] = candidateAddress
            candidateDetailsDictionary[constants.state] = candidateState
            candidateDetailsDictionary[constants.country] = candidateCountry
            candidateDetailsDictionary[constants.field] = candidateField
        
        # If address & field are available in the data.
        elif len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 5:
            candidateAddress = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
            candidateState = addressStateCountryNoOfResumeUploadsAndCandidateField[1]
            candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[2]
            candidateField = addressStateCountryNoOfResumeUploadsAndCandidateField[4]
            
            # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.address] = candidateAddress
            candidateDetailsDictionary[constants.state] = candidateState
            candidateDetailsDictionary[constants.country] = candidateCountry
            candidateDetailsDictionary[constants.field] = candidateField
            
        # If address is not available in the data.
        # Some time there is only 4 rows are available but Adress is available and field is not available.
        # As shown below.
        # J4/35B,Gupta Colony Malviya Nagar,Delhi.
        # Delhi/NCR
        # India
        # Total Resumes Uploaded :- [ 1 ]
        
        elif len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 4:
            # If adress is not available and field is available.
            if "Total Resumes Uploaded" not in addressStateCountryNoOfResumeUploadsAndCandidateField[-1]:
                candidateAddress = "Not Available"
                candidateState = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
                candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[1]
                candidateField = addressStateCountryNoOfResumeUploadsAndCandidateField[3]
                
                # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
                candidateDetailsDictionary[constants.address] = candidateAddress
                candidateDetailsDictionary[constants.state] = candidateState
                candidateDetailsDictionary[constants.country] = candidateCountry
                candidateDetailsDictionary[constants.field] = candidateField
            
            # If adress is available and field is not available.
            elif "Total Resumes Uploaded" in addressStateCountryNoOfResumeUploadsAndCandidateField[-1]:
                candidateAddress = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
                candidateState = addressStateCountryNoOfResumeUploadsAndCandidateField[1]
                candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[2]
                candidateField = "Not Available"
                
                # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
                candidateDetailsDictionary[constants.address] = candidateAddress
                candidateDetailsDictionary[constants.state] = candidateState
                candidateDetailsDictionary[constants.country] = candidateCountry
                candidateDetailsDictionary[constants.field] = candidateField
            

        # If address & field both are not available in the data.
        elif len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 3:
            candidateAddress = "Not Available"
            candidateState = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
            candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[1]
            candidateField = "Not Available"
            
            # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.address] = candidateAddress
            candidateDetailsDictionary[constants.state] = candidateState
            candidateDetailsDictionary[constants.country] = candidateCountry
            candidateDetailsDictionary[constants.field] = candidateField
            
            
        elif len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 2:
            candidateAddress = "Not Available"
            candidateState = "Not Available"
            candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
            candidateField = "Not Available"
            
            # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.address] = candidateAddress
            candidateDetailsDictionary[constants.state] = candidateState
            candidateDetailsDictionary[constants.country] = candidateCountry
            candidateDetailsDictionary[constants.field] = candidateField
           
           
        elif len(addressStateCountryNoOfResumeUploadsAndCandidateField) == 1:
            candidateAddress = "Not Available"
            candidateState = "Not Available"
            candidateCountry = addressStateCountryNoOfResumeUploadsAndCandidateField[0]
            candidateField = "Not Available"
            
            # Adding last 4 keys and values of candidate details in candidateDetailsDictionary.   
            candidateDetailsDictionary[constants.address] = candidateAddress
            candidateDetailsDictionary[constants.state] = candidateState
            candidateDetailsDictionary[constants.country] = candidateCountry
            candidateDetailsDictionary[constants.field] = candidateField
              
        return candidateDetailsDictionary
    



# This is the raw data text scraped from the website and looped using for loop. 
# "Element at index {index number} is" used for getting the index of elements.
'''Element at index 0 is Sl. No.


Element at index 1 is Member Name
Member Username / Pass


Element at index 2 is Member Address
Member State
Member Country


Element at index 3 is Member Phone
Member Mobile Number


Element at index 4 is Option


Element at index 5 is 1 .


Element at index 6 is Sharad Kumar Singh |
niit.meet@gmail.com[ Active Free Member ]


Element at index 7 is J4/35B,Gupta Colony Malviya Nagar,Delhi.
Delhi/NCR
India
Total Resumes Uploaded :- [ 1 ]
Sales/Marketing


Element at index 8 is 9643800491


Element at index 9 is Active

View Details

View Login Log

[Admin Login]

Manage Coupons

Update Address'''