DOI_PREFIX = '99.9999'
DOI_DEPOSIT_URL = 'https://doi.crossref.org/servlet/deposit' # live submission URL
VALIDATE_XML_URL = 'https://apps.crossref.org/XSDParse/'

JOURNAL_TITLE = 'Academic Journal'
ABBREV_TITLE = "QQ"
ISSN = "01234567"   # taken from https://www.scimagojr.com/journalsearch.php?q=36276&tip=sid

# depositor
DEPOSITOR_NAME = 'John Doe' # name of depositor
EMAIL = 'email@example.com' # each submission recieves an email. It will describe any XML formatting errors you may have.

# submission to Crossref
DOI_BATCH_START = '<doi_batch xmlns="http://www.crossref.org/schema/4.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="4.4.0" xsi:schemaLocation="http://www.crossref.org/schema/4.4.0 http://www.crossref.org/schemas/crossref4.4.0.xsd">'
DOI_BATCH_END = '</doi_batch>'
