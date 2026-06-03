# README

CS257: Software Design\
Hilly Gangolf\
Spring 2026\
Git Repo: ind-flask-gangolfa

## Database Individual Deliverable | Revision Submitted June 3, 2026

### Important files:

- app.py: program for running flask application
- datasource.py: contains functions that retrieve infromation from datasets given a set of arguments
- createtable.sql: creates the data tables to copy data into
- psqlConfig.py: contains the credentials for connecting to the database
- flask_test.py: a program for testing my flask app
- artists.csv & interpol_art.csv: data files taken from my team project

### Write up:

I decided to represent my data using the same columns and headings that were in the original csv file. All of the columns were very important to the project as a whole, so I did not want to change them. Aside from removing headers, there were no other superfluous detials to remove.\
The queries I created for this assignment are central to the theme of exploring stolen artwork

- **get_artwork_given_origin(connection, origin)** --> My first query returns the titles of stolen artwork made by a given artist. This relates to the fourth user story for our team deliverable. It would be useful for those doing research into a specific artist, or for someone who wants to know what artist is most often stolen.
- **get_count_given_artist(connection, artist)** --> My second query returns the count of stolen artwork given a country of origin. This relates to the second user story we wrote for our team deliverable, and could help someone doing art research that is specific to a certain country or region.

### How to run flask app & data queries in Stearns:

1. Go to [JupyterHub server on fern](https://fern.mathcs.carleton.edu/jupyter/hub/login) and log in with Carleton credentials.

2. ssh into stearns in the terminal like so: ssh [your username]@stearns.mathcs.carleton.edu. Type in your Carleton password when prompted.

3. Navigate to the correct directory: cs257/ind-flask-gangolfa
4. The data tables (interpol_data & artist_data) may already be loaded into sterns. To check, you can use:
   <pre>
   psql 
   \dt
   </pre>
   If data tables are not already created, navigate to the correct directory:
   <pre>
   cd ProductionCode/data
   </pre>
   Then, create the data tables:
   <pre>
   psql -f createtable.sql
   </pre>
   Copy csv data into SQL data tables. My data has two files, so both will need to be copied:
   <pre>
   psql
   \copy interpol_data FROM 'interpol_art.csv' DELIMITER ',' CSV
   \copy artist_data FROM 'artists.csv' DELIMITER ',' CSV
   </pre>
5. Run app.py
   <pre>
   python3 app.py
   </pre>

   You will then be prompted by the following instructions:
   <pre>
   Welcome to the Art Tracker
   1. To find stolen art count of a given country, enter:
   http://[Host][Port]/origin/COUNTRY_NAME
   
   2. To find artwork associated with a given artist, enter:
   http://[Host][Port]/artist/ARTIST_NAME
   
   Countries to search for:
   - France
   - Spain
   - United Kingdom
   
   Artist to search for:
   - Andy Warhol
   - Jackson Pollock
   - Vincent van Gogh
   </pre>

### Test app with flask_test.py:

<pre>
python3 -m unittest Tests.flask_test
</pre>

## Flask Individual Deliverable | Revision Submitted June 2, 2026

### Important files:

- app.py: program for running flask application
- command_line.py: contains functions that retrieve infromation from datasets given a set of arguments
- flask_test.py: a program for testing my flask app
- command_line_test.py: a program for testing my command line arguments
- artists.csv & interpol_art.csv: data files taken from my team project

### How to run tests

**Test command lines with command_line_test.py:**

<pre>
python3 -m unittest Tests.command_line_test
</pre>

**Test app with flask_test.py:**

<pre>
python3 -m unittest Tests.flask_test
</pre>

### How to run app

<pre>
python3 app.py
</pre>

When you run app.py you will be greated by the following text:

    Welcome to the Art Tracker
    1. To find stolen count by a given artist, enter:
    http://[Host][Port]/artist/ARTIST_NAME

    2. To find artist of a given artwork, enter:
    http://[Host/IP][Port]/artwork/ARTWORK_TITLE

Some examples of artists and artwork to search for are as follows:

**Artists:**

- Andy Warhol
- Jackson Pollock
- Pablo Picasso
- Vincent van Gogh

**Artworks:**

- Femme Assise
- Bowl With Guitar On A Pedestal Table
- The Individual Tauromachy
- Arnold Schwartzenegger
