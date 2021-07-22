# xeneta_task
Xeneta Task

# Creating a HTTP based API using Flask

This project was a Xeneta task 

## Setup

I did not use docker so i installed pg admin and postgres using the link attached
You can learn more in the [Install postgresql and pg admin to run the database](https://tecadmin.net/how-to-install-postgresql-in-ubuntu-20-04/) if you prefer atool for easy script running


Alternatively, you can only install postgres and run the commands in the terminal.
Here are some commands to help after postgres is installed

sudo su postgres

#psql

\l                  -lists all databases

\c xeneta2          -use xeneta2 database

\dt                  -show all tables

## Available Scripts
In the project run

### Run `pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)`

Runs the app in the development mode.\

Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

The page will reload \

### `routing and APIS`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `Project challenges`

Postgres connection to the Flask Framework was not straight forward in the Flask documentation.

Failure to bulk import the data into the tables .. so i used bulk inserts in phases.

Query returning not desired output as seen in the task example.

### `Duration`

This assignment has taken me Close to 5 hours.



To learn Flask, check out the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/).

