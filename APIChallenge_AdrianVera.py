
#Adrian Vera's CODE2040 API Challenge 2017
import requests
import datetime
import json

#API Endpoints
registration_endpoint = "http://challenge.code2040.org/api/register"
reverse_endpoint = "http://challenge.code2040.org/api/reverse"
reverse_validate = "http://challenge.code2040.org/api/reverse/validate"
haystack_endpoint = "http://challenge.code2040.org/api/haystack"
haystack_validate = "http://challenge.code2040.org/api/haystack/validate"
prefix_endpoint = "http://challenge.code2040.org/api/prefix"
prefix_validate = "http://challenge.code2040.org/api/prefix/validate"
dating_endpoint = "http://challenge.code2040.org/api/dating"
dating_validate = "http://challenge.code2040.org/api/dating/validate"

#API Token and Github Link
api_token = "923fe63af0e261fa9e57105dd2b7ba05"
github_link = "https://github.com/TheAdrianVera/CODE2040_API_Challenge2017"
default_json = { "token" : api_token }

#Step I: Registration
#Connect to Registration Endpoint through POST request
def registration():
	r = requests.post(registration_endpoint, json = { "token": api_token, "github": github_link })
	print(r.text)

#Step II: Reverse String
#Take in a given string an POST back the reversed string
def reverse():
	r = requests.post(reverse_endpoint, json = default_json)
	r_string = r.text
	r_string = r_string[::-1] #step backwards from last string element
	r2 = requests.post(reverse_validate, json = { "token": api_token, "string": r_string })
	print(r2.text)

#Step III: Needle in Haystack
#Find the index of a given string in an array of strings
def find_needle():
	r = requests.post(haystack_endpoint, json = default_json).json()
	r_needle = r["needle"]
	index = r["haystack"].index(r_needle)
	r2 = requests.post(haystack_validate, json = { "token": api_token, "needle": index })
	print(r2.text)

#Step IV: Prefix 
#Given a prefix return the remaining Strings in an Array that don't contain the prefix
def prefix():
    r = requests.post(prefix_endpoint, json = default_json).json()
    r_prefix = r["prefix"]
    r_list = r["array"]

    new_list = list(filter(lambda x: x.find(r_prefix) != 0, r_list))
    r2 = requests.post(prefix_validate, json = { "token": api_token, "array": new_list })
    print(r2.text)

#Step V: Dating Game
#Dating Game 
def dating_game():
	r = requests.post(dating_endpoint, json = default_json).json()
	r_interval = r["interval"]
	r_time = r["datestamp"]

	formatted_time = datetime.datetime.strptime(r_time, "%Y-%m-%dT%H:%M:%SZ") #ISO 8601 formatted time
	new_time = formatted_time + datetime.timedelta(seconds = r_interval)
	new_time = new_time.strftime("%Y-%m-%dT%H:%M:%SZ")
	r2 = requests.post(dating_validate, json = {"token": api_token, "datestamp": new_time})
	print(r2.text)

registration()
reverse()
find_needle()
prefix()
dating_game()

