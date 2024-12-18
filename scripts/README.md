# Scripts for downloading all ISO3166-2 country subdivision flags

[![pytest](https://github.com/amckenna41/iso3166-flag-icons/workflows/Building%20and%20Testing/badge.svg)](https://github.com/amckenna41/iso3166-flag-icons/actions?query=workflowBuilding%20and%20Testing)
[![Platforms](https://img.shields.io/badge/platforms-linux%2C%20macOS%2C%20Windows-green)](https://pypi.org/project/pySAR/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
<!-- [![CircleCI](https://circleci.com/gh/amckenna41/pySAR.svg?style=svg&circle-token=d860bb64668be19d44f106841b80eb47a8b7e7e8)](https://app.circleci.com/pipelines/github/amckenna41/pySAR) -->
[![codecov](https://codecov.io/gh/amckenna41/iso3166-flag-icons/branch/master/graph/badge.svg?token="")](https://codecov.io/gh/amckenna41/iso3166-flag-icons)

Motivation
----------
After browsing through the likes of GitHub and Kaggle I found that there wasn't any solid and reliable dataset for ISO3166-2 icons. There existed several repos and datasets for the ISO3166-1 flags, mainly due to there being a much smaller amount (~270) compared to the >3100 that are available in the ISO3166-2 folder of this repo. 
Several scripts were required to automate the collection, downloading, processing and cleaning of the thousands of ISO3166-2 flag images, generating a pipeline that starts with a web-scraping function and ends with the creation of the custom CSS and JSON files also present in the repo.

The exact purpose of each script can be seen below, as well as in the comments of each file:
* `getAllSubdivisionFlags.py` - downloading all ISO3166-2 subdivision flags from the main subdivisions wiki (https://en.wikipedia.org/wiki/Flags_of_country_subdivisions) as well as using country's respective wiki URL's. 
* `generateReadMe.py` - create README file for each ISO3166-2 subfolder, listing all the subdivisions per country.
* `generateCSS.py` - create CSS files with respective CSS selectors/classes for both ISO3166-2 and ISO3166-2 flag icons.
* `generateJSON.py` - create JSON files of flag files, their name and ISO code for both ISO3166-1 and ISO3166-2 folders. 
* `iso3166_.py` - list of all ISO3166 country names, alpha2 and alpha3 codes.
* `svgCompress.sh` - script for compressing folder of image flags in SVG format.

Requirements
------------

* [Python][python] >= 3.6
* [requests][requests] >= 1.16.0
* [pandas][pandas] >= 1.4.3
* [tqdm][tqdm] >= 4.55.0
* [beautifulsoup4][beautifulsoup4] >= 4.10.0
* [scour][scour] >= 0.38.2
* [pycountry][pycountry] >= 22.3.5
* [emoji-country-flag][emoji-country-flag]>= 1.3.0
* [fuzzywuzzy][fuzzywuzzy] >= 0.18.0
* [pyWikiCommons][pyWikiCommons] >= 0.0.1

Usage
-----

## Download all ISO3166-2 subdivision flags

```bash
python3 getAllSubdivisionFlags.py --output="../iso3166-2-icons" 

--output: output folder to downloaded flag files
--url_csv: using default value of iso3166-2_urls.csv
--no_flags_csv: using default value of noISO3166-2Flags.csv
```

## Compress all SVG flag icon files in output folder

```bash
./svgCompress.sh --input="../iso3166-2-icons/" --output="../output/" --filesize=50

--input: input folder of SVG files to compress
--output: output folder to store compressed SVG files
--filesize_threshold: all SVG files above this threshold will go through the compression algorithm. 
```

## Create CSS files for both ISO3166-1 and ISO3166-2 icons

```bash
python3 generateCSS.py --countryFolder="../iso3166-1-icons" --cssFileName="iso3166-1-icons.css" --iso3166Type="iso3166-1"

--countryFolder: input folder of flag files to create CSS tags and references to
--cssFileName: output filename of CSS
--iso3166Type: create ISO3166-1 or ISO3166-2 CSS file
```

## Create ISO3166-1 or ISO3166-2 JSON files containing all flag and subdivision info per country/jurisdiction

```bash
python3 generateJSON.py --countryFolder="../iso3166-2-icons" --jsonFileName="iso3166" --iso3166Type=""

```

## Create README files for each ISO3166-2 country in iso3166-2-icons dir, listing contents of dir and subdivision info

```bash
python3 generateReadme.py --country
```

Tests
-----
Several Python test scripts were created using [unittest][unittest] framework. These tests test the full pipeline from getting the flags via web-scraping to exporting the flag & country info to json. 
To run all tests, from the <i>scripts</i> repo folder run:
```
python3 -m unittest discover -v
```

To run tests for specific module, from the main <i>scripts</i> repo folder run:
```
python -m unittest tests.MODULE_NAME -v
-v : verbose output
```

<!-- 3511 seconds total-->
[python]: https://www.python.org/downloads/release/python-360/
[pandas]: https://pandas.pydata.org/
[tqdm]: https://tqdm.github.io/
[requests]: https://requests.readthedocs.io/
[beautifulsoup4]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[scour]: https://github.com/scour-project/scour
[pyWikiCommons]: https://github.com/amckenna41/pyWikiCommons
[flag-icons-repo]: https://github.com/lipis/flag-icons
[pycountry]: https://github.com/flyingcircusio/pycountry
[emoji-country-flag]: https://pypi.org/project/emoji-country-flag/
[fuzzywuzzy]: https://pypi.org/project/fuzzywuzzy/
[unittest]: https://docs.python.org/3/library/unittest.html