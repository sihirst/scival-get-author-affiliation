
# SciVal -  Useful Scripts

## Author Affiliation
This script will return the author's affiliation information based off the SciVal's author ID. It will return the following to author_info.csv:

- Author_ID
- Affiliation_URL
- Affiliation_ID
- Affiliation_Name
- Affiliation_City
- Affiliation_Country

## Split Topics
When exporting topics from SciVal they will return in a semicolon separated array (topic1; topic2; topic3) in one field. To split this into individual rows with the paper DOI, you can run this script. It will return the following to output.csv:

- DOI
- Topic
