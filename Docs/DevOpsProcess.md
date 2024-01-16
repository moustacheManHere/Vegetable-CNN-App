# DevOps Process

This Document is used to document the things I did with regards to DevOps in my project.

Branches:
    - Main: Used as a development branch -> Merge features in and integrate before finalising
    - Releases: Working Product Branch -> Deploy to Render from this branch 
    - Feature Branches: Branches to implement single feature -> Merged into Main and Deleted after completion

Stages of Development (See Milestones):
    - Model Development: Develop and Deploy Deep Learning Model for image prediction 
    - Minimum Viable Product: Create a complete but simple working product that can predict
    - Vegetable Database: Simple Database Setup and use CRUD operations to show info in UI
    - User System: Add Complete Login/Signup functionality with User Profile 
    - Complete Database System: Allow user to save information & find info in DB
    - Advanced Features: Add-on to Application to have additional features

Issues Flow:
    1. Issue will be in backlog until it's sprint is started
    2. Issue moves to "Current Spring" section indicated it has to be done before moving to next spring
    3. Issue moves to "To Do" section indicating I will be working on it today
    4. Issue moves to "In progress" Section indicating it is being worked on
    5. Issue moves to "Documentation" Section indicating it is complete and need to document the methodology under Docs/ 
        -> If issue is trivial and doesn't need documentation it will go straight to Closed
    6. Issue is closed -> Can automate by committing with "git commit -m "Finished x Closes #72"
