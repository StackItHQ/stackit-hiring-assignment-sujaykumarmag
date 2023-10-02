[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_IojtdoU)
# StackIt Hiring Assignment

### Welcome to StackIt's hiring assignment! 🚀

**If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨**


We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:
- We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances :P
- You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
- We love out of the box solutions. We prefer to call it *Jugaad* 
- This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.

## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Today, you are going to make their lives better.**

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

You get brownie points 🍪 if you can make it even easier by allowing them to filter the data as well before importing it into Google Sheets 🔍.

**Other pointers**:
- Import to Sheet – After validation and mapping, devise a method to populate the data into a chosen Google Sheet, either appending to existing data or creating a new sheet 📥📋.
- Optimize for Large Files – Large datasets are common in analytics. Your solution should effectively handle large CSV files (~15MB CSV file) without causing performance issues or prolonged waiting times 📈📦.

## Submission ⏰
The timeline for this submission is: **9AM, 30th Sept, 2023 - 12PM, 2nd Oct, 2023**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [x] My code's working just fine! 🥳
- [x] I have recorded a video showing it working and embedded it in the README ▶️
- [x] I have tested all the normal working cases 😎
- [x] I have even solved some edge cases (brownie points) 💪
- [x] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore 😛

## Developer's Section

```
  _________ __                 __     .___  __       _____                                                     __   
 /   _____//  |______    ____ |  | __ |   |/  |_    /  _  \   ______ ______ ____   ______ _____   ____   _____/  |_ 
 \_____  \\   __\__  \ _/ ___\|  |/ / |   \   __\  /  /_\  \ /  ___//  ___// __ \ /  ___//     \_/ __ \ /    \   __\
 /        \|  |  / __ \\  \___|    <  |   ||  |   /    |    \\___ \ \___ \\  ___/ \___ \|  Y Y  \  ___/|   |  \  |  
/_______  /|__| (____  /\___  >__|_ \ |___||__|   \____|__  /____  >____  >\___  >____  >__|_|  /\___  >___|  /__|  
        \/           \/     \/     \/                     \/     \/     \/     \/     \/      \/     \/     \/      
                                                                                                                    
```


### File Structure


```

Repository Name
│
├── README.md
├── LICENSE
├── assets/images               (Optional: For Plots and Images)
│   ├── pair_plot.png
│  
│
├── frontend/                
│   ├── gs_files/
│   │   ├── code.gs        (Source Code - Solution 1 (full))
│   │   ├── filePicker.html
│   │   └── uploadCSV.html
│   │
│   ├── index.html     (Source Code - Solution 2 (frontend)
|   ├── box_plot.html 
│  
│
├── input_testcases/              (Optional: Test files)
│   ├── mnist_test.csv
│   ├── titanic.csv
│   └── ...
│
├── main.py (Source Code - Solution 1 (backend App)           
│   ├── data.json
│   ├── data.csv
│   └── ...
│
├── .gitignore          (Gitignore file)

```


####  LINK TO VIDEOS = https://drive.google.com/drive/folders/1NW97Ge4ocpaR44yNko0oJgxJu6wSLPdd?usp=share_link

~ Note : First Video 1.3 Mins and Second is 4.5 mins but I tried to reduce it, Sorry for breaking the Protocol

                                                                                                                    
### Solution One -- Aproach

A Simple Solution to work on the frontend itself like the AppsScript Google API to create menus , dialogboxes etc... This integration enhances frontend functionality within Google Apps Script, making it easier for users to navigate and interact with your applications.

Highlights 
   - Created a Menu for whenever, the user wants to upload the .csv file
   - Made the Menu Functionality as a Trigger, so that I would stay when the sheet opens.
   - Created OAuth Scopes and deployed the Project
   - Filtering Techniques depending on the Value


<img width="1440" alt="Screenshot 2023-10-02 at 7 00 11 AM" src="https://github.com/StackItHQ/stackit-hiring-assignment-sujaykumarmag/assets/75253527/44d84cd6-5f7e-4d7a-866b-cb9689162df4">


Video 

[![Watch the video](https://i.stack.imgur.com/Vp2cE.png)](https://drive.google.com/drive/u/1/folders/1NW97Ge4ocpaR44yNko0oJgxJu6wSLPdd)




                                           
### Solution Two -- Aproach

After researching through different Github Repositories and Workshops 

Highlights 
   - Created a FastAPI Python App
   - The number of Request-Response Cycle has been reduced through the front-end functionality. (Jugaad)
   - Deployed on EC2 (Elastic-Compute-Cloud)

ALternative Solutions Opted (Jugaad)
   - Created a GKE cluster and deployed my API end-point
   - Deployed on Koyeb WebApp and tested directly on the Google Sheets AppsScript API (Python-Alpine Problem)
   - Continuous with 3 GET/ and 2 POST/ Services has been Optimized to 1 POST/ with only one end point 



<img width="1440" alt="Screenshot 2023-10-02 at 7 09 22 AM" src="https://github.com/StackItHQ/stackit-hiring-assignment-sujaykumarmag/assets/75253527/ec7fe5ed-483b-459f-b19b-4c6bc971fc43">

Video
[![Watch the video](https://i.stack.imgur.com/Vp2cE.png)](https://drive.google.com/drive/u/1/folders/1NW97Ge4ocpaR44yNko0oJgxJu6wSLPdd)

                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    

