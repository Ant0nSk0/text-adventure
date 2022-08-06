# Text Adventure Game
This is a text-based choose-your-own-adventure game running in the terminal.  
Players get to make decisions in the game by typing in their answers, each answer leading to a different outcome.  
![mock-up](images/pp3-mockup.PNG)  
## Features  

+ Game Start  
When the programme is run, the intro screen shows, welcoming the player and ask them if they would like to play.  
![intro-screen](images/intro-page-pp3.PNG)  
Followed by a request for the player to enter their name.  
![enter-name](images/name-pp3.PNG)  
After that the game starts to tell the story and asking the players to make choices. Each answer will lead to a different outcome. Some choices makes the game progress and some ends in a game over. The game over screen asks the player if they want to restart.  
![game-over](images/game-over-pp3.PNG)  
+ Dice mini game  
Depending on the players choices, they might end up getting to play dice in a mini game halfway through the story.  
![dice-screen](images/dice-act-pp3.PNG)  
+ The End  
If the player manages to reach one of the endings they will be given a 'thank you for playing' message and the option to play again.  
![the-end](images/the-end-pp3.PNG)
+ Choices  
There's plenty of choices that changes how to story goes and depend on previous choices. There is two key elements that will affect the story depending on the players choices. The lucky dice and how you are introduced to Griff.  
### Road Map  
![roadmap](images/roadmap-pp3.PNG)  
____
### Future Features  
Future features might include a more fleshed out dice mini game, with score. Also a health / life system to make the game more forgiving, smoother transitions and general improvements.  

## Testing  
*Tests included but are not limited to:*  
+ Tested both in Gitpods terminal and the mock terminal on Heroku. Also did additional testing in PyCharm.  
+ Tested both on computer and mobile.

+ Playing through the game several times:  
    + Making the wrong decisions  
    + Making the wrong inputs  
    + Making the right inputs
    + Making the right decisions 
    
### Detailed Manual Testing:  
> w = win.  
> x = lose.  
> o = loop until other input.  
> ? = random chance w/x  
> Does not count 'start new game' as a question. Answers start from 'answer voice'

| Q1<br>A | Q2<br>A | Q3<br>A | Q4<br>A | Q5<br>A | Q6<br>A | Q7<br>A | Q8<br>A | Q9<br>A | Q10<br>A | Q11<br>A | Q12<br>A | Expected<br>Result | Actual<br>Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| yes | yes | yes | town | tavern | b | yes | no | ask | a | a | luck | W | W |
| yes | yes | yes | town | tavern | b | yes | no | ask | a | a | spirit | x | x |
| yes | yes | yes | town | tavern | b | yes | no | ask | a | b |  | w | w |
| yes | yes | yes | town | tavern | b | yes | no | ask | b |  |  | x | x |
| yes | yes | yes | town | tavern | b | yes | no | fight |  |  |  | x | x |
| yes | yes | yes | town | tavern | b | yes | yes |  |  |  |  | o | o |
| yes | yes | yes | town | tavern | b | no |  | ask | a | a | spirit | x | x |
| yes | yes | yes | town | tavern | b | no |  | ask | a | b |  | w | w |
| yes | yes | yes | town | tavern | b | no |  | ask | b |  |  | x | x |
| yes | yes | yes | town | tavern | b | no |  | fight |  |  |  | x | x |
| yes | yes | yes | town | tavern | a | yes |  | griff | a | a | griff | ? | ? |
| yes | yes | yes | town | tavern | a | yes |  | griff | b | a | spirit | x | x |
| yes | yes | yes | town | tavern | a | yes |  | griff | a | b |  | w | w |
| yes | yes | yes | town | tavern | a | yes |  | fight |  |  |  | x | x |
| yes | yes | yes | town | tavern | a | no |  |  |  |  |  | x | x |
| yes | yes | yes | town | market |  |  |  |  |  |  |  | x | x |
| yes | yes | yes | forest |  |  |  |  |  |  |  |  | o | o |
| yes | yes | no |  |  |  |  |  |  |  |  |  | x | x |
| yes | no |  |  |  |  |  |  |  |  |  |  | x | x |
| no |  |  |  |  |  |  |  |  |  |  |  | x | x |


### Validation
+ The code goes through the [PEP8 Checker](http://pep8online.com/) without any issues.  

## Bugs  
### Fixed bugs:  
+ While going through the game, making certain decisions in a certain order would leave the while loop of the dice game open, resulting in parts of the game jumping in where it shouldn't have. I fixed the issue by adding a variable and setting it to a boolean value depending on input, making the loop stop correctly when the player chooses to stop playing.  
### Unfixed bugs:  
+ There is no currently known bugs left unfixed.  

## Deployment  
This project was deployed onto Heroku using Code Institutes mock terminal. I did that by:  
1. Going to the dashboard on Heroku.
2. Clicking 'New' then 'Create new app'.
3. Choosing a name for the app, setting region to Europe and clicking on 'Create'.
3. Going to the Settings tab.
4. Setting the config vars with PORT : 8000
5. Add buildpacks 'Python' and 'Node.js' in that order.
6. Going to the Deploy tab.
7. Clicking on GitHub and Connect it.
8. Search for this repository and connect to it.
9. Activating Automatic and then Manually Deploy.
10. Waiting for it to build, then clicking on 'View'.  

Live link can be found here: https://textbased-adventure.herokuapp.com/  

## Credits  
+ Code Institute for the deployment terminal
+ [Colorama](https://pypi.org/project/colorama/) for a bit of color.
