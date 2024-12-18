"""
Create README file for each ISO 3166-2 country subfolder, listing the name of 
each country's subdivision (including those with no associated flags), its
subdivision code and a link to the flags in the repo.
"""
import os
from os import listdir
import argparse
import iso3166_
import flag
import pycountry

#base URL to iso3166-2-icons folder in repo
baseURL = 'https://github.com/amckenna41/iso3166-flag-icons/blob/main/iso3166-2-icons'
subdivisionURL = "https://en.wikipedia.org/wiki/ISO_3166-2:"

def createReadMe(country, code, url, outputFolder):
    """
    Create custom README for each countrys subdivision folder in the output folder. The
    README will list all of the country's subdivisions, their filename on the repo and 
    links to download them on the repo.

    Parameters
    ----------
    :country : string 
      country name.
    :code : string 
        2 letter ISO code of country.
    :url : string
        source url for where subdivisions were pulled from.
    :outputFolder : string
        filepath to output folder to write README
    Returns
    -------
    None 
    """  
    #get filepath to readme file in each output folder
    filepath = "{}/{}".format(outputFolder, code)
    readMeFilepath = os.path.join(filepath, 'README.md')

    #get list of all files in country's subfolder
    allFiles = sorted([f.lower() for f in listdir(filepath) if os.path.isfile(os.path.join(filepath, f))], key=str.casefold)
    
    #get list of country's subdivisions
    allSubdivisions = list(pycountry.subdivisions.get(country_code=code))

    #remove readme file from list of files
    if ("README.md" in allFiles):
        allFiles.remove("README.md")

    #append subdivision name, flag emoji and source url to readme
    outputStr = ""
    outputStr+= "# {} Subdivisions {}\n\n".format(country, flag.flag(code)) #flag doesnt work on Windows 10
    outputStr+= "Source: {}\n\n".format(url)

    subdName = ""

    #iterate through all file names, appending to the output string 
    for file in allFiles:
        if (file.lower() == ".ds_store" or file.lower() == "readme.md"): #skip non-subdivision files
            continue
        outputStr+= "*"
        for subd in allSubdivisions:
            if (subd.code.lower() == os.path.splitext(os.path.basename(file))[0].replace('_', ' ').lower()):
                subdName = subd.name
        
        outputStr += " " + os.path.splitext(os.path.basename(file))[0].replace('_', ' ').upper()
        if (subdName != "" and subdName != None):
            outputStr += " (" + subdName.title() + ")"

        #ensure filename is in uppercase
        file = os.path.splitext(file)[0].upper() + os.path.splitext(file)[1]

        outputStr += " -> [{}]({}/{}/{})\n".format(file, baseURL, code, file)

    #get list of all filenames in folder
    allFiles = [os.path.splitext(file)[0] for file in allFiles]

    #delete readme file if exists
    if (os.path.isfile(readMeFilepath)):
        os.remove(readMeFilepath)
    
    allFileSubdivisions = []
    missingSubdivisions = []

    #get list of missing subdivision flags not present in country subfolder
    if (pycountry.subdivisions.get(country_code=code) != None):
        allFileSubdivisions = [subdivision.code.lower() for subdivision in pycountry.subdivisions.get(country_code=code)]
        for subd in allFileSubdivisions:
            if (subd not in allFiles):
                missingSubdivisions.append(subd)
        
    #print list of country's subdivisions that dont have any associated flags
    if len(missingSubdivisions) != 0:
        outputStr += f'\n{country} ISO 3166-2 subdivisions with no available flags (https://en.wikipedia.org/wiki/ISO_3166-2:{code}):\n'
        for subd in sorted(missingSubdivisions):
            for subdiv in pycountry.subdivisions.get(country_code=code):
                if (subdiv.code.lower() == subd):
                    outputStr += "\n* {}: {} ({})".format(subd.upper(), subdiv.name, subdiv.type)

    #create new readme file
    open(readMeFilepath, mode='a').close()

    #append output string to readme
    with open(readMeFilepath, "a") as readmeFile:
        readmeFile.write(outputStr)

if __name__ == '__main__':

    #parse input arguments using ArgParse 
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-countryInputFolder', '--countryInputFolder', type=str, required=False, default="../iso3166-2-icons", help='Input folder of ISO3166-2 flag icons, ../iso3166-2-icons by default.')

    #parse input args
    args = parser.parse_args()
    countryInputFolder = args.countryInputFolder

    #invalid country folder input
    if not (os.path.isdir(countryInputFolder)):
        raise ValueError(f'Country folder not found at path {countryInputFolder}.')

    #get list of ISO 3166-2 country dirs
    iso3166_2_folder = sorted([i for i in os.listdir(countryInputFolder) if os.path.isdir(os.path.join(countryInputFolder, i))])

    #iterate over all ISO 3166-2 folders and create custom readme file
    for folder in iso3166_2_folder:
        createReadMe(iso3166_.countries_by_alpha2[folder].name, folder, subdivisionURL + folder, countryInputFolder)