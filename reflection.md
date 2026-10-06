# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
-(Answer): There were many many issues with the game; The guessing part functioned mostly correctly but I could not restart games, the hints were wrong, the scoring made no sense, and may other issues but the game itself worked upon initiation. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
-(Answer): 
    - The hints were wrong; They would say the the opposite of what they were     supposed to. 
    - The Game did not restart when i clicked new game
    
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior     | Console Output / Error |
|-------|-------------------|---------------------|------------------------|
| | | | |Hint telling me if | The hint told me    |
| | | |my guess was lower   | to go lower when    |
| | | | | or higher         | I needed to go      |
                            | higher and higher   | 
                            |  when I needed to   |
                            |  lower              |
                            |                     |
         New Game Option    |When I selected the  | 
         allows user to     |"New Game" option;   |
         start a new game   |no changes happened  |
                            |and I am repeatedly  |
                            |shown a message      |
                            |saying "Game over.   |
                            |Start a new game     |
                            |to try again."       |
                            |                     |
        blue box at the top |The number of entries|
        shows a consistant  |a user is prompted to|
        number of entries   |make are inconsistant|
        available           |                     |
                            |                     |
                            |

                          

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

- (ANSWER): I Used Co-pilot. The first bug I used the agent for was the Lower/Higher Hint bug, The issue was simple, it just needed two string edits to fix but the Agent suggested changes to variables and strings that would not have affected the issue, I rejected that change and asked it to narrow down to the most minimal possible channge; thats when it made those 2 string changes. I found the two lines where the changes had been made, I left comments to denote them for myself and ran to the code. The issue had been resolved
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
(ANSWER): It depended on the specific bug but in the end I relied on seeing if the issue was no longer appearing in the game nor in the terminal after running the tests. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- (ANSWER): For the Lower/Higher Hint bug I simply changed the strings to nonsensical letters to see what would happen during a game run, as per my hunch it changed the hint and so I knew the AI's suggestion was correct. 

- Did AI help you design or understand any tests? How?
(ANSWER): AI helped me understand my tests, I gave it context on what the game was doing and I simply asked it to explain its changes, it broke them down for me and helped me understand what was being tested. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- (ANSWER): Asking the AI agent to propose the minimal possible change kept things quiet simple.

- What is one thing you would do differently next time you work with AI on a coding task?
- (Answer): I would keep in mind that the time zones of EST and EDT are different, as my innatention has led me to submit this late. 
I would also pace myself better, take breaks , drink water.  

- In one or two sentences, describe how this project changed the way you think about AI generated code.
- (ANSWER): It is not as simple as I thougt, there is real need for human input, the machine needs experienced guidance pr it will run with any number of over-engineered ideas. 
