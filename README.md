# cicd-assignment-FA23-BCT-034

CSC418 Cloud Computing - Lab Assignment 3 (FA 2026)
Sadat Ali, FA23-BCT-034

A small web page served by nginx, tested with Selenium (pytest, Chromium, ChromeDriver)
inside a Docker test agent, and deployed by a multi-stage Jenkins pipeline:
Checkout -> Package -> Start Staging -> Test -> Deploy.
