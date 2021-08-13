# flask_api
## Target
- Quickly create API by flask
- Understanding the diferent between the API and RESTful API
- Deploying the API on the  main current platform
    - [x] Heroku
    - [ ] GCP
    - [ ] Azure
- Using Postman to test the API

---
## requirement
see the [requirements.txt](/requirements.txt)

---

## content
- Create API
    1. create the CRUD
    2. the point
----
- Deploy the API by Heroku
    Sign in  the website of Heroku and click the "Create a new app".
    <img src="image\create.png">
    Name your new app and choose the location of server.
    <img src="image\create2.png">
    Click the Deploy on the Headbar , choose the resource of program.
    Search your name of repository in your Github.
    <img src="image\deploy.png">
    "Enable Automatic Deploys "will  autoly update and deploy your each repository by pushed.

    Click the  "Deploy Branch"  to  Deploy your API.
    <img src="image\deploy2.png">

    You could see the log of deploy in the "More > View Log".
    <img src="image\deploy3.png">

    If deploying successfuly ,you could find the new "port" and  "Build succeeded "in the log.
    <img src="image\deploy4.png">

- Deploy the API by GCP

    coming soom...
- Deploy the API by Azure

    coming soom...
---
- Test by Heroku
    Enter the "Setting"\
    The "Domains" offer a link which you could use to develop or test. You can also change to your own domainanme.
    <img src="image\test.png">
    Text the link in browser and test the other path.
    <img src="image\test2.png">

- Test by Postman
    Text the link in Postman.
    <img src="image\test3.png">