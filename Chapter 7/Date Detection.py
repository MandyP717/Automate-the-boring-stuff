"""Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01
to 12, and the years range from 1000 to 2999. Note that if the day or month
is a single digit, it’ll have a leading zero."""

import re

text = """Coastal mangrove forests are carbon storage powerhouses, tucking away vast amounts of organic matter among their submerged, tangled root webs.
But even for mangroves, there is a “remarkable” amount of carbon stored in small pockets of forest growing around sinkholes on Mexico’s Yucatan Peninsula, 
researchers report 25/05/2021 in Biology Letters. These forests can stock away more than five times as much carbon 30/13/1963 per hectare as most other terrestrial forests.
There are dozens of mangrove-lined sinkholes, or cenotes, on the peninsula. Such carbon storage hot spots could help nations or companies achieve carbon neutrality
05/03/1992 — in which the volume of greenhouse gas emissions released into the atmosphere is balanced by the amount of carbon sequestered away (SN: 1/31/20).

At three cenotes, researchers led by Fernanda Adame, a wetland scientist at Griffith University in Brisbane, Australia, collected samples of soil at depths down to 6 meters, 
and used carbon-14 dating to estimate how fast the soil had accumulated at each site 28/02/3000. The three cenotes each had “massive” amounts of soil organic carbon, the researchers report, 
averaging about 1,500 metric tons per hectare. One site, Casa Cenote, stored as much as 2,792 metric tons per hectare, 29/02/1700.
Mangrove roots make ideal traps 33/11/1850 for organic material. The submerged soils also help preserve carbon. As sea levels have slowly risen over the last 8,000 years, 
mangroves have kept pace, climbing atop sediment ported in from rivers or migrating inland. In the cave-riddled limestone terrain of the Yucatan Peninsula, there 
are no rivers to supply sediment. Instead, “the mangroves produce more roots to avoid drowning 31/12/1950,” which also helps the trees climb upward more quickly, offering 
more space for organic matter to accumulate, Adame says.

As global temperatures increase, sea levels may eventually rise too quickly for mangroves to keep up (SN: 6/4/20). Other, more immediate threats to the peninsula’s 
carbon-rich cenotes include groundwater pollution, expanding infrastructure, urbanization and tourism. 
(source: https://www.sciencenews.org/article/mangrove-forests-carbon-storage-yucatan-climate)"""

valid_days = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}


def leap_year_check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                valid_days["02"] = 29
            else:
                valid_days["02"] = 28
        else:
            valid_days["02"] = 29
    else:
        valid_days["02"] = 28


def find_dates(text):
    regex = re.compile(
        "([0123]\d)\/([01]\d)\/([12]\d{3})"
    )  # find date format DD/MM/YYYY
    result = regex.findall(text)
    saved_dates = [
        {"day": date[0], "month": date[1], "year": date[2]} for date in result
    ]  # month remains string
    return saved_dates


def check_for_valid_dates(list_of_dates):
    checked_dates = []
    for test_date in list_of_dates:
        if test_date["month"] == "02":
            leap_year_check(int(test_date["year"]))
        if (
            int(test_date["day"]) <= valid_days.get(test_date["month"], False)
            and int(test_date["day"]) > 0
        ):  # checks for valid days in a month and valid months
            checked_dates.append({"/".join(test_date.values()): "Valid"})
        else:
            checked_dates.append(
                {"/".join(test_date.values()): "Invalid"}
            )  # no test for year because regex doesnt pick it up
    return checked_dates


print(check_for_valid_dates(find_dates(text)))
