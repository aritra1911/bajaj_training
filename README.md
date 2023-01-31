# Bajaj Markets Training for Microservices Python
Code samples and SQL Notes are distributed in their respective
directories.

## SQL
The RDBMS being used is **PostgreSQL 15.1**.  The terminal
output log of the first two days are stored in their respective files
with dated filenames.

## HTML
This directory consists of purely HTML and CSS files.  All
audio and video assets have been removed in order to preserve the
sanity of this git repository.

## Python
The plethora of standalone python (ver. 3) scripts demo
the very basics of the python features and OOP concepts.
There aren't any multi-module scripts in this directory.

### Flask
Simple standalone web programs equipped with debug flags which
demonstrate majority of the Flask webframework for Python.

#### URL Shortner
A simple flask project to shorten long URLs by keeping a record of
the URL and it's short form in a file. The short form is calculated
through hashes and hence is the same for the same URL everytime. A
URL cache is maintained so that lookup of the actual URL happens
in O(1) time given the short form. The short form is 6 characters
long and it always starts with an upper case or a lower case alphabet.
Once lookup is successful, it redirects automatically to the desired
URL, otherwise if lookup fails, it aborts with a 404.

#### Pet Animal Registration Form
This project allows you to register pets one by one into a PostgreSQL
database table. The details of each pet are editable and it is
possible to delete all the pets too. The index page shows all the
registered pets in a grid format.

### Mockito
Some monkey patching codes using Mockito are included.

### Postgres
Test programs involving the psycopg2 connection library.

## JS
Some basic javascript test codes are included.

