"""Lab 3: Regexes and reformatting."""
import re


#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################
sorted_list = []
arranged_name = ""
arranged_phone = ""

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

for contact in contacts:
    # first break up individual contact information into smaller arrays to hold full name, phone number, and location
    contact_info = re.split(",", contact)

    # add data to variables within array positions
    full_name = contact_info[0]
    phone_num = contact_info[1]
    location = contact_info[2]

    # test individual contact info array
    # print(full_name, '', phone_num, '', location)
    # print(full_name)

    # break up individual parts of name into array
    pattern = re.compile(r"\s")
    name_parts = pattern.split(full_name)

    # print(name_parts)

    # add parts to variables
    if len(name_parts) == 3:
        first = name_parts[0]
        middle = name_parts[1]
        last = name_parts[2]
        arranged_name = last + ", " + first + ", " + middle
    else:
        first = name_parts[0]
        last = name_parts[1]
        arranged_name = last + ", " + first

    # break up individual parts of phone number into array
    pattern = re.compile(r"[\d]")
    phone_parts = pattern.findall(phone_num)
    # print(phone_parts)

    if len(phone_parts) > 10:
        last4 = phone_parts[7] + phone_parts[8] + phone_parts[9] + phone_parts[10]
        mid3 = phone_parts[4] + phone_parts[5] + phone_parts[6]
        first3 = phone_parts[1] + phone_parts[2] + phone_parts[3]
        arranged_phone = "(" + first3 + ") " + mid3 + "-" + last4
    else:
        last4 = phone_parts[6] + phone_parts[7] + phone_parts[8] + phone_parts[9]
        mid3 = phone_parts[3] + phone_parts[4] + phone_parts[5]
        first3 = phone_parts[0] + phone_parts[1] + phone_parts[2]
        arranged_phone = "(" + first3 + ") " + mid3 + "-" + last4

# extra credit
    new_contact = [arranged_name, location, arranged_phone]
    sorted_list.append(new_contact)
sorted_list.sort()

for sorted_contact in sorted_list:
    print(sorted_contact[0])
    print(sorted_contact[1])
    print(sorted_contact[2])

    # adding in a separator for output readability
    print("------------------")



