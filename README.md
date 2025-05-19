# cs361-microserviceA
Parses a JSON file that contains data of TV shows to return the rating, genre, and episode duration for a particular TV series.

**REQUIREMENTS PRIOR TO USE** <br/>
Update line 11 of microserviceA.py to reflect the name of the JSON file to be used.<br/>

**REQUEST DATA** <br/>
To send a request, ensure the microservice is running and when prompted, input the title of the TV series you are interested in receiving data on.<br/>
<img width="318" alt="image" src="https://github.com/user-attachments/assets/37e07318-3291-4d3b-a5d1-cee588ca2fcd" />

**RECEIVE DATA** <br/>
You will receive a JSON object containing the requested show's rating, genre, and episode duration: <br/>
<img width="312" alt="image" src="https://github.com/user-attachments/assets/1d8f8cb1-5395-477d-9403-69438281d7e9" />


You may receive a response of 'No show found with the title '[user_input]', if the title was not found within the JSON.

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
**UML SEQUENCE DIAGRAM** <br/>
