<h1 align=center> The Diplomat | Bar & Grill</h1>
<img src="docs/image-am-i-responsive.PNG">

Developer: **Arron Beale**

Deployed: [The Diplomat | Bar & Grill](https://ci-pp4-the-diplomat.herokuapp.com/)
(Note: Ctrl + click to open in a new tab)  
  



## Table of Content
1. [Project Goals](#project-goals)
   1. [User Goals](#user-goals)
   2. [Site owner Goals](#site-owner-goals)
2. [User Experience](#User-Experience)
   1. [Target Audience](#target-audience)
   2. [User Requirements and Expectations](#user-requirments-and-expectations)
   3. [Manual](#manual)
   4. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
   1. [Flowcharts](#flowcharts)
   2. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
   1. [Languages](#Languages)
   2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
7. [PEP8 Validation](#pep8-validation)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#ackowledgements)

## Project Goals
To Create a web app for a fictional local restaurant that has a booking system to allow users to book a table online.

### User Goals
- To be able to book a table using an online booking system
- To be able to view a food menu
- To be able to view a drinks menu
- To be able to edit, or cancel bookings
- To be able to view all bookings made

### Site Owner Goals
- 
- 
- 
- 

[Back to Top](<#table-of-content>)
## User Experience

### Target Audience
- 

### User Requirments and Expectations
- 
- 
- 
- 


[Back to Top](<#table-of-content>)  
## User Stories

### User
1. As a User I can 
2. As a User I can 
3. As a User I can 
4. As a User I can 
5. As a User I can 
6. As a User I can 
7. As a User I can 
 
### Admin/Authorised User
8. As an Admin/Authorised User I can 
9. As an Admin/Authorised User I can 
10. As an Admin/Authorised User I can 
11. As an Admin/Authorised User I can 
12. As an Admin/Authorised User I can 
13. As an Admin/Authorised User I can 
14. As an Admin/Authorised User I can 
15. As an Admin/User I can 

### Site Owner
16. As a Site Owner I can v
17. As a Site Owner I can 
18. As a Site Owner I can 
 
[Back to Top](<#table-of-content>)
## Technical Design


### Flow Charts

<details><summary>Flow</summary>
<img src="">
</details>  


### Wireframes

<details><summary>Home & Article Page</summary>
<img src="">
</details>  



   
## Technologies Used

### AI
- [Blog Text Generation](https://inferkit.com/docs/generation)
- [Image Generation](https://openai.com/dall-e-2/)
  
  
### Languages
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)



### Resources Used
- [Canva](https://www.canva.com/)
- [Colors.co](https://coolors.co/)


### Frameworks and Tools
- [Bootstrap](https://getbootstrap.com//)

- [Balsamiq](https://balsamiq.com/)

- [GitPod](https://gitpod.io/)

- [GitHub](https://github.com/)

[Back to Top](<#Table-of-Content>)

### Libraries

#### Python Libraries
- [OS](https://docs.python.org/3/library/os.html)
- [Date time](https://docs.python.org/3/library/datetime.html)



## Features
  
<details><summary>Home</summary>
</details>  
  
<details><summary>Feature</summary>
</details>  
  
<details><summary>Feature</summary>
</details>  
  
<details><summary>Feature</summary>
</details>  
  
<details><summary>About</summary>
</details>  

<details><summary>Contact</summary>
</details> 
 

[Back to Top](<#table-of-content>)
## Validation

### PEP8 Validation
<details><summary>page</summary>
<img src="">
</details>

<details><summary>Page</summary>
<img src="">
</details>

<details><summary>Page</summary>
<img src="">
</details>  


## Testing

* 
* 
* 
* 
* 


### Manual Testing

<details><summary>View manual testing</summary>

### Testing User Stories

 User:
1. As a User, I would like to...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|||||
|Navbar|Click links|Direction to page|Navigation is successful|
<details><summary>Images</summary>
![](https://)

</details>
</details>



Site Owner
8. As the site owner, I would like...

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Responsivness|Site viewport is resized|Good view on mobile|Site is responsive|
|Validation|Form data entered|Errors are displayed where applicable| Success |

<details><summary>Images</summary>

</details>

### Automated Testing
 
 <details><summary>View automated testing</summary>

- Automated testing was done using the unittest and coverage librararies for Python.


### Unit Tests
- Test...

<img src="">

- Test results....

<img src="">

### Coverage 

- Coverage was installed via the terminal, pip install coverage
<img src="">


- Coverage was then used to test using the following...
<img src="">


- The results of the test were the following:
<img src="">

- A HTML report was also generated using the command, coverage html
<img src="">

</details>






[Back to Top](<#table-of-content>)
## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| **Bug** | **Fix** |
| Bug I had | I fixed it by... |



[Back to Top](<#table-of-content>)
## Deployment
### Heroku / Firebase

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
1. Log in to your account at heroku.com.
2. Create a new app, add a unique app name and choose your region.
3. Click on create app.
4. Go to "Settings".
5. Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to buid your app from.
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

[Back to Top](<#table-of-content>)
## Credits


### Media
- [Favicon](https://favicon.io/): Witch Icon</a>
- [Card Images](https://www.pexels.com/)</a>

### Code
- [Site](https://www.google.com)


## Acknowledgements

### Special thanks to the following:
- Code Institute
- 
- 
- 

[Back to Top](<#table-of-content>)
