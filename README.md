# README

CS257: Software Design\
Hilly Gangolf\
Spring 2026\
Git Repo: ind-flask-gangolfa

## Database Individual Deliverable | May 8, 2026

### Write up:

I decided to represent my data using the same columns and headings that were in the original csv file. All of the columns were very important to the project as a whole, so I did not want to change them. Aside from removing headers, there were no other superfluous detials to remove.\
The queries I created for this assignment are central to the theme of exploring stolen artwork

- **get_artwork_given_origin(connection, origin)** --> My first query returns informations reguarding stolen artwork made by a given artist. This relates to the fourth user story for our team deliverable. It would be useful for those doing research into a specific artist, or for someone who wants to know what artist is most often stolen.
- **get_artwork_given_artist(connection, artist)** --> My second query returns all stolen artwork given a country of origin. This relates to the second user story we wrote for our team deliverable, and could help someone doing art research that is specific to a certain country or region.

### How to run data set in Sterns:

1. Go to [JupyterHub server on fern](https://fern.mathcs.carleton.edu/jupyter/hub/login) and log in with Carleton credentials.
2. Navigate to the correct directory: cs257/ind-flask-gangolfa
3. Load data tables\
   The files createtable.sql and datasource.py are located in the ProductionCode/Data directory. The tables, interpol_data & artist_data may already be loaded into sterns. To check, you can use:
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
4. To run datasource:
   <pre>
   python3 datasource.py
   </pre>
   Further editing of **origin** and **artist** variables in datasource.py can be done in order to adjust what data is returned.

## Flask Individual Deliverable | April 29, 2026

#### Important files:

- app.py: program for running flask application
- command_line.py: contains functions that retrieve infromation from datasets given a set of arguments
- flask_test.py: a program for testing my flask app
- command_line_tests.py: a program for testing my command line arguments
- artists.csv & interpol_art.csv: data files taken from my team project

### How to run tests

Command line tests:

<pre>
python3 -m Tests.command_line_tests
</pre>

Flask app test:

<pre>
python3 -m Tests.flask_test
</pre>

#### How to run app

<pre>
python3 app.py
</pre>

When you run app.py you will be greated by the following text:

    Welcome to the Art Tracker
    1. To find stolen count by a given artist, enter:
    http://127.0.0.1:5100/artist/[ARTIST_NAME]

    2. To find artist of a given artwork, enter:
    http://127.0.0.1:5100/artwork/[ARTWORK_TITLE]

Some examples of artists and artwork to search for are as follows:

Artists:

- Andy Warhol
- Jackson Pollock
- Pablo Picasso
- Vincent van Gogh

Artworks:

- Femme Assise
- Bowl With Guitar On A Pedestal Table
- The Individual Tauromachy
- Arnold Schwartzenegger
