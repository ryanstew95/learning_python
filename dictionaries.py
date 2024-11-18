monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"]) # November
print(monthConversions.get("Dec")) # December
print(monthConversions.get("Luv", "Not a valid key")) # Setting a default value for a key that doesn't exist