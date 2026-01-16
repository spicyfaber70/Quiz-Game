**Description:**
This project is a desktop trivia application that tests the user's general knowledge through a graphical user interface (GUI). Unlike basic quiz programs that rely on hardcoded question lists, this project connects to the Open Trivia Database API to fetch a fresh set of questions every time the app launches.

**Purpose of project:**
I built this project to create a kind of study engine that never runs out of content. I wanted to learn how to bridge the gap between a local application and the internet, essentially creating a "test generator" that could pull endless questions from the cloud. It was an attempt at moving away from static data structures (like lists) and learning to work with live JSON data.

**Tech Stack:**
Language: Python
GUI: Tkinter
Networking: Requests Library (HTTP/REST API)
Data Format: JSON parsing & HTML Entity decoding

**Difficulties:**
When I first connected to the API, the text appeared broken (e.g., quotes looked like &quot;). I learned that raw data from the web often needs cleaning before display. I implemented the html library to get rid of these characters.

**Changes for the future:**
The API supports specific subjects (e.g., "Science," "History"). I plan to add a settings menu so users can filter questions to focus on their weak areas.
