# Python3 program to sort the dates in a string array

# Map to store the numeric value of each month depending on
# its occurrence i.e. Jan = 1, Feb = 2 and so on.
monthsMap = dict()
# Function which initializes the monthsMap
def sort_months():

    monthsMap["Jan"] = 1
    monthsMap["Feb"] = 2
    monthsMap["Mar"] = 3
    monthsMap["Apr"] = 4
    monthsMap["May"] = 5
    monthsMap["Jun"] = 6
    monthsMap["Jul"] = 7
    monthsMap["Aug"] = 8
    monthsMap["Sep"] = 9
    monthsMap["Oct"] = 10
    monthsMap["Nov"] = 11
    monthsMap["Dec"] = 12


def cmp(date):
    date = date.split()
    return (
        int(date[2]),  # year
        monthsMap[date[1]],  # month
        int(date[0]),  # day
    )


if __name__ == "__main__":

    dates = [
        "24 Jul 2017",
        "25 Jul 2017",
        "13 Feb 2016",
        "11 Jun 1996",
        "01 Jan 2019",
        "12 Aug 2005",
        "01 Jan 1997",
    ]
    # Order the months
    sort_months()
    # Sort the dates
    dates.sort(key=cmp)  # return type is tuple.
    # Print the sorted dates
    for i in range(len(dates)):
        print(dates[i])
