# Website login credientials. 
# These details should be filled after installation to make this script run.
userName = ""  # Needed to be filled after Installation.
password = ""  # Needed to be filled after Installation.

# This detail should be needed to run the program if not provide you will face an Attributer Error.
chromeDriverPath = ""   # Needed to be filled after Installation.

# Website Details.
websiteUrl = "https://misc.placementindia.com/marketing-panel/marketing_view_seeker.php?id=member" 
autoLoginWebsiteUrl = f"https://{userName}:{password}@misc.placementindia.com/marketing-panel/marketing_view_seeker.php?id=member" 

searchBoxName = "kword"
detailsClassName = "templateTableHead"

# Key name for final Dictionary of Candidate details
name =  "Name"
emailId = "Email ID"
phoneNumber = "Phone Number"
status = "Status"
address = "Address"
state = "State"
country = "Country"
field = "Field"

# List of Field to be added in raw excel at Row 1. This is prerequisite cell text for first Row.
prerequisiteFirstRowTextList = [name, emailId, phoneNumber, status, address, state, country, field]