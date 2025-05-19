# cs361-microserviceA
Parses a JSON file that contains data of TV shows to return the rating, genre, and episode duration for a particular TV series.

**REQUIREMENTS PRIOR TO USE** <br/>
Update line 11 of microserviceA.py to reflect the name of the JSON file to be used.

Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call. Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.

**REQUEST DATA**
To send a request, ensure the microservice is running and when prompted, input the title of the TV series you are interested in receiving data on.

Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call.

**RECEIVE DATA**
You will receive a JSON object containing the requested show's rating, genre, and episode duration: 

{
  "rating": "9.5",
  "genre": "drama",
  "episode duration": "55 minutes"
}

You may receive a response of 'No show found with the title '[user_input]', if the title was not found within the JSON.

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
**UML SEQUENCE DIAGRAM**
