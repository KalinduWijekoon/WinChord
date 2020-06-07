# WinChord
WinChord is an app that allows you to upload and store all of your music on the cloud.
First, you need to create a new account and then a new album by filling out the form on the "Add Album" page. Once an album is created you will be able to add songs.
## How to deploy for testing
* Use `pip3 install -r requirements.txt` to install required python libraries   <br>
* Use `python3 manage.py runserver` to start a local test server in port 8000 (127.0.0.1:8000) or you can specify the required port.<br> 
(example `python3 manage.py runserver 0.0.0.0:<CustomPort>` or `python3 manage.py runserver 127.0.0.1:<CustomPort>`)<br>
* Use your web browser (Chrome preferred) to test the application by typing the URL <br> (example `http://127.0.0.1:8000` or `http://localhost:<port>`)   
