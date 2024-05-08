# library-LEDs
This project will setup for an LED light system that will light up searched for books within a personal library. 

The final goal will be to have image captures taken of the book shelves, image processing to determine what books are on the shelves and their positions in relation to the LED light strips, and be able to then search for these books through a mobile application. 

### General Overview Diagram
![image](https://github.com/jdclark905/library-LEDs/assets/76894714/703b7103-9187-4098-bb2c-87a06dc8f02b)

### Book Detection
Here is the proposed flow for the book detection piece
![image](https://github.com/jdclark905/library-LEDs/assets/76894714/4b796b2d-3daa-43ce-a207-cab41e5751d4)

### LED Controller
Will be written in Python using Flask to support the API endpoints to search for books within the database to find their positions on the shelf. 

### Database
Will utilize a NoSQL database (MongoDB) so that additional information can easily be captured for books to allow for more searchable options as more information is found on books.

### App
A web application for the initial build but will be followed up with an iOS and Android applications to control from a mobile device. 

## Application Setup and Run
1. Clone repository
2. Install dependencies with
```
pip install -r requirements.txt
```
3. Run the application with
```
python run.py
```
