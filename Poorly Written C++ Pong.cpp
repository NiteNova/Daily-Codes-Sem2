// Demonstrate primitve drawing in SFML
#include<iostream>
using namespace std;


#include "SFML/Graphics.hpp"

int main() {

    //game set up 
    sf::RenderWindow renderWindow(sf::VideoMode(500, 500), "Pong Paddle"); //set up screen
    sf::Event event; //set up event queue

    //paddle1 set up
    sf::RectangleShape paddle1(sf::Vector2f(30.0f, 200.0f));
    paddle1.setFillColor(sf::Color::Blue); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    paddle1.setPosition(460.0f, 135.0f); 
    //paddle2 set up
    sf::RectangleShape paddle2(sf::Vector2f(30.0f, 200.0f));
    paddle2.setFillColor(sf::Color::Green);
    paddle2.setPosition(10.0f, 135.0f); 

    //ball set up
    float ballX = 237;
    float ballY = 220;
    float xVel = .08;
    float yVel = .08;

    sf::CircleShape ball(20);
    ball.setFillColor(sf::Color(200, 50, 50));
    ball.setPosition(ballX, ballY);

    


    //-----------------------------------------------------------GAME LOOP-----------------------------------------------------------
    while (renderWindow.isOpen()) {//keep window open until user shuts it down
        while (renderWindow.pollEvent(event)) { //look for events

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                renderWindow.close();

            //KEYBOARD INPUT (just one key to start
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) { //checks if "W" is pressed
                paddle1.move(0, -5); //move the rectangle 5 pixels UP on the y axis

            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) { //checks if "W" is pressed
                paddle1.move(0, 5); //move the rectangle 5 pixels DOWN on the y axis

            }
            //KEYBOARD INPUT (just one key to start
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::W)) { //checks if "Arrow UP" is pressed
                paddle2.move(0, -5); //move the rectangle 5 pixels UP on the y axis

            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) { //checks if "Arrow DOWN" is pressed
                paddle2.move(0, 5); //move the rectangle 5 pixels DOWN on the y axis


            }
        }

        //physics section

        if (ballX + 10 > paddle1.getPosition().x - 30 && ballY > paddle1.getPosition().y && ballY < paddle1.getPosition().y + 200) {
            xVel *= -1;
        }
        if (ballX - 10 < paddle2.getPosition().x + 20 && ballY > paddle2.getPosition().y && ballY < paddle2.getPosition().y + 200) {
            xVel *= -1;
        }


        if (ballX + 10 < 0 || ballX + 10 > 500) {
            xVel *= -1;
        }
        if (ballY + 10 < 0 || ballY + 10 > 500) {
            yVel *= -1;
        }

        ballX += xVel;
        ballY += yVel;
        ball.setPosition(ballX, ballY);


     
        //render section-----------------------------------------
        renderWindow.clear(); //wipes screen, without this things smear
        renderWindow.draw(paddle1);
        renderWindow.draw(paddle2); 
        renderWindow.draw(ball);
        renderWindow.display(); //flips memory drawings onto screen

    }//----------------------------------------------------END OF GAME LOOP-----------------------------------------------------------

    cout << "goodbye!" << endl;
} //end game
