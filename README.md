# Electric Dreams

## Introduction



Intro

<br>

![Screenshot of homepage](./media/readme/screenshotfrontpage.png)

<br>

[Visit the live website on Heroku here](https://electric-dreams.herokuapp.com/)

<br>

View information about testing in the [testing.md file here](TESTING.md)

<br>

## Table of Contents


  * [Introduction](#introduction)
  * [UX](#ux)
    + [Strategy](#strategy)
      - [Epics](#epics)
      - [Translation to User Stories](#translation-to-user-stories)
      - [Agile Management](#agile-management)
    + [Scope](#scope)
    + [Structure](#structure)
      - [Design Structure - Site layout](#design-structure---site-layout)
      - [Information Structure - Database Models](#information-structure---database-models)
    + [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    + [Surface](#surface)
  * [Features](#features)
  * [Future Features](#future-features)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Notable Bugs](#notable-bugs)
  * [Security](#security)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## UX

### Strategy

The overall aim of the project is to develop a platform that allows users to create and share book reviews with others around the world.

* Site Goals
    * To enable users to write their own reviews and publish them online
    * To let users browse exsiting reviews for reading ideas
    * To have a design with pleasing visuals and functional layout

* User Goals
The ideal user is excited about reading, looking for new books to read, willing to share their recommendations and wants to interact with with other readers.


#### Epics

At the beginning of the project, ten Epics were created and can be viewed at the [Kanban board here](https://github.com/neil314159/portfolio-project-4/projects/1).
* Installation and Setup
* Profiles
* User Authentication
* Reviews
* Comments
* Wishlist
* Search
* Site Interface
* Admin Features
* Testing Strategy

#### Translation to User Stories

1. Installation and Setup
    * US11: Setup and Install Django - As a developer, I can set up django and the necessary software packages, so that I can deploy the site and begin development
    * US12: Set up environmental variables securely - As a developer, I want to set up the secret keys and database variable in a secure manner, so that they are kept hidden when deployed and not accidentally exposed through github
    * US13: Deploy to Heroku - As a developer, I want to ensure that the deployment pipeline is functioning, so that I can commence development on the project and test on heroku as well as the local environment
1. Profiles
    * US14: Create a User Profile - As a user, I can create a new account on the Book Barn website, so that I have the permissions required to publish my own reviews on the site
    * US15: View User Profile - As a user, I can log into the site and view my own profile page, so that I can see a list of all reviews I have written and edit or delete them
    * US16: Update User Profile - As a user, I can view my own profile page and edit my username, so that I can change the name displayed on my reviews that is displayed to other users and site visitors
    * US17: Delete User Profile - As a user, I can delete my own account, so that I can remove my information and content from the site if I desire
    * US18: Change User Password - As a user, I can change my password, so that my account remains secure
    * US19: Reset USer Password - As a user, I can reset my password, so that can access my account if my password is forgotten
1. User Authentication
    * US20: Authenticate user login/logout - As a user, I can log and and out of the site, so that my personal details and content are kept secure
    * US21: Restrict actions to allowed users - As a developer, I want to only allow certain actions when the user is logged in, so that users are unable to access data from other users
    * US22: Social Login - As a user, I can sign into the site using another account such as Google or Facebook, so that do not have to sign up for a new account and remember another password
1. Reviews
    * US45: Create new book review - As a user, I can write and save a new book review on the site, so that other users may see it and get ideas about new books to read
    * US46: Edit review - As a user, I can edit my published book reviews, so that update my reviews with new information or correct any errors
    * US47: Display Reviews - As a user, I can view articles reviewing books on the site, so that I can learn about new books I might like to read
    * US48: Delete reviews - As a user, I can delete a review that I have written, so that it is removed from the site
    * US49: Book cover image - As a user, I can upload a cover image for the book review, so that the book cover can be shown on the site when users browse or search for reviews
    * US50: Book cover API - As a user, I can search books by title, so that a book cover image is automatically found and added to my review
    * US51: AJAX category editing - As a user, I can create a new category when writing a review, so that my article is published under the most suitable genre
1. Comments
    * US26: Leave user comments on reviews - As a user, I can write a comment on my own or other reviews, so that I can interact with other users on the site
    * US27: Moderation for comments in admin panel - As a site owner, I can view all comments on the site through the admin interface and delete them if required, so that inappropriate comments are not publicly displayed
    * US28: Allow users to manage comments on their own reviews - As a user, I can delete comments left by other users on my own reviews, so that inappropriate comments are not displayed next to content I have written and the administrative burden is lightened for the site owner
1. Wishlist
    * US23: Add/remove books from wishlist - s a user, I can click on a like button on each review, so that the book is saved to my wishlist and I can keep track of new books to read
    * US24: View wishlist on profile page - As a user, I can click on my wishlist link, so that I can see at a glance a list of all the books on my wishlist
    * US25: External purchase link - As a user, I can view my wishlist of saved books and click on a purchase link, so that I can easily buy books I am interested in
1. Search
    * US29: Sitewide search - As a user, I can type text into the search box in the navigation bar, so that I can find matching text in any reviews on the site
    * US30: AJAX live search - As a user, I can type text into the search box in the navigation bar, so that I see a continuously updated set of search results as I type
    * US31: Category-based view - As a user, I can select a category from a drop-down menu in the navbar, so that I can view books that interest me the most in a particular genre
1. Site Interface
    * US39: Install and configure Bootstrap - As a developer, I want to use a flexible framework, so that the user interface of the site can be made consistent and usable
    * US40: Night Mode - As a user, I can select the choice between normal and dark mode, so that I can use the site with the colour scheme I prefer
    * US41: Responsive layout on different devices - As a user, I want to have the site be responsive across different devices, so that I can enjoy a consistent experience and access the site from laptop, phone or tablet
    * US42: Form styling - As a site owner, I want all forms on the site to be styled in a similar fashion, so that the user interface is consistent across the whole site
    * US43: Accessibility - As a user, I can make use of accessibility features on the site, so that I can navigate and use the site without difficulty
    * US44: User feedback messages - As a user, I can receive clear and unambiguous feedback about my actions, so that I can be sure that each operation was carried out successfully
1. Admin Features
    * US32: Admin area data formatting - As a site owner, I can log into the admin area and see all comments, reviews and wishlists, so that I can monitor the overall operation of the site and keep an overview of all content posted
    * US33: Category Managment - As a site owner, I can log into the admin area and add, edit and delete the categories for book reviews, so that book reviews on the site are properly organised
    * US34: Review of the week - As a site owner, I can select a book review to be highlighted on the main home page, so that high quality content is presented to new users
1. Testing Strategy
    * US35: Automated Testing - As a developer, I want to deploy automated testing with high code coverage, so that I can reduce the number of bugs in the site and improve the user experience
    * US36: Manual testing - As a developer, I want to manually test every aspect of the interface and functionality of the site, so that users can have a bug-free and consistent experience 
    * US37: Third party testing - As a developer, I can ask an independent person to test out the site while I watch, so that note any bugs or any part of the interface which is not easily understood
    * US38: Code Validation - As a developer, I want all of the code in the site to conform to best practices, so that it is clear, readable and bug-free



All of the completed user stories are available on the Kanban board found [here](https://github.com/users/neil314159/projects/1), where the acceptance criteria and implementation actions for each story are visible by clicking on each individual issue. For example, the user story [US14](https://github.com/neil314159/portfolio-project-5/issues/14) is as follows:
<br>
<br>
Title: US49: Book Cover Image

User Story: As a user, I can upload a cover image for the book review, so that the book cover can be shown on the site when users browse or search for reviews

Acceptance Criteria:
- Acceptance Criteria 1
	Given that I am logged in and registered on the site
	When I am creating a review
	Then I will see a field to upload an image for the book cover
- Acceptance Criteria 2
	Given that I have written a book review on the site
	When I do not upload an accompanying cover
	Then a default image is provided

Tasks:
- [x] link cloudinary API in the templates and setting files
- [x] resize the image to appropriate dimensions and ration before using
- [x] add a default cover if no image is uploaded

Epic: #4 

<br>
<br>


#### Agile Management
Throughout the development process, these epics and user stories were managed using the Kanban Board functionality built into Github. The Epics were created, developed into user stories using the Project interface in Github. The User Stories were created as issues with attached task lists and acceptance criteria, and were moved between columns to designate progress on a particular task. Once an issue was completed it was closed and moved to the Done column. The milestone tracker was also used to indicate overall progress and the project backlog.

The label function for Github issues was used to assign Must Have, Could Have and Should Have status, and unfinished tasks were assigned Won't Have at the end of the sprint. Labels were also used to indicate the number of user points assigned to each User Story.

Overall, 82% of issues/User Stories were completed and marked closed, with a number of features remaining for future sprints.

<br>

![points chart](./media/readme/agile/Chart.png)

<br>

![kanban](./media/readme/agile/kanban_board.png)

<br>

![milestone](./media/readme/agile/milestone.png)


### Scope

After creating the Epics and translating them into User Stories, this now leads to a list of concrete features to implement
* Reviews - can be viewed by all users
* Reviews - can be created, viewed, edited and deleted by users
* Categories - can be created by an administrator and applied by users to their reviews
* Comments - can be created, viewed, edited and deleted by users
* Wishlist - items can be added, removed and edited by users
* Users - can register, login, change password and reset password
* Users - can search the site
* Users - all operations can only be carried out with proper permissions

### Structure

#### Design Structure - Site layout
* A simple and straightforward site layout was adopted to make the site easy for users to navigate.
* All forms for creating, editing, viewing and deleting information are simply presented and easy to understand.

#### Information Structure - Database Models

A number of custom models were created for this project:

![full model](./media/readme/models/usermodel.png)
* Custom User model - the original project used in the course utiised a One-to-One profile model to store customer data such as telephone address etc. One of the features I really wanted to implement is the ability for a user to sign on using only their email address instead of a username. This makes things easier for the user since they don't have to remember or record an extra username. This is only possible by extending the standard Django user model and altering the authentication to use an email address instead of a username when signing up.  The user model was based off Django AbstractUSer and added extra fields to be stored in the database.

![full model](./media/readme/models/wishlistcomment.png)
* Wishlist item - this model links users and products and allows them to store a lost of possible future purchases

![full model](./media/readme/models/blog.png)
* Blog Post - for representing posts made on the website blog
* Blog Category - to allow for categorisation of the posts
* Comment - to allow for user comments and reviews, connected to the product model

![full model](./media/readme/models/request.png)
* ArtRequest - stores messages sent in by users from the comment form making suggestions or requests

The entire schema is visible here:

![full model](./media/readme/models/graphviz.png)




### Skeleton

#### Wireframes
Balsamiq was used to create the wireframes for this project. The initial layout of the site remained largely the same during the development process, except for the profile page and the wishlist being separated into two pages rather than combined into one. The wireframe for the review index page was also used for the search results and category view pages as they are functionally very similar.

* Homepage
![homepage](/media/readme/wireframes/homepage.png)

* Review Listing
![homepage](/media/readme/wireframes/review_list.png)

* Review Detail
![homepage](/media/readme/wireframes/review_detail.png)

* Profile/Wishlist Page
![homepage](/media/readme/wireframes/profile_page.png)

### Surface

* Fonts - 
Initially I wanted to use a standard system font in keeping with the general technological theme of the site, but after user testing feedback I moved to using Nunito Sans, which provides a slightly more refined look for the user interface and works well for an ecommerce site such as this.

* Images - 
Since the purpose of the site is to sell visual posters and prints, no other extraneous images were used elsewhere as they would distract from the products for sale.

* Colours - 
The colour scheme was kept extremely clear and simple so as not to take away from the artwork images being displayed. A clean white background was deemed the best after testing various colour combinations to allow the images to stand out most clearly.

## Features

#### Static Homepage
The homepage explains the purpose of the site to new users, and explains that they can register for an account for extra advantages, or else start browsing the site directly.

![homepage](/media/readme/features/screenshotfrontpage.png)

#### Navbar
The navbar appears at the top of every page on the site, giving users access to every section of the site. Only logged in users will see the links for adding a review, the profile page and the wishlist page. Logged out users will see links to register and login instead of the logout link here.

![navbar](/media/readme/features/navbar2.png)

#### Dropdown and Search Menu
On the right hand side of the navbar are the drop-down category list and the search box. The category list is populated from the database and directs users to a page showing books from each genre. The search box takes the user's search term when they hit enter and provides a page of matching results.

![navbar](/media/readme/features/dropdown_search.png)

#### Reviews Index
This page provides the main functionality of the site, it shows a paginated list of all the reviews published on the site in reverse chronological order. The user can see all the reviews available here at a glance. The use of the cover images from the books makes the page more engaging and attractive.

![index](/media/readme/features/indexpage.png)

#### Create Review
This form allows the user to create their own review for publication on the site. The instructions at the top let them know which fields are mandatory. They enter the book details, upload a photo of the cover if they wish and click submit.

![index](/media/readme/features/create_review.png)

#### Book Review Card
This UI element gathers all the data about a book and presents it to the user in a variety of contexts, for example in the reviews index, in the search page, in the category listing. It shows the book cover, the author and title of the book, the reviewer and the number of stars the reviewer gave the book. Both the cover image and the Read Review button provide a link to a detailed view of the book review.

![index](/media/readme/features/book_card.png)

#### Detailed Review
When the user clicks on an individual review, this page shows them the full details including the text of the review. The user is also given the option to add the book to their wishlist or purchase it if the reviewer included a link. If the user is logged in and looking at one of their own reviews, they will also be presented with buttons to edit or delete the review.

![index](/media/readme/features/review_detail.png)

#### Login/Signup
These two forms let unregistered users sign up for a new account, or registered users log back in. If the user forgets their password, there is a link for them to reset it if they have supplied an email account.

![index](/media/readme/features/signup.png)

![index](/media/readme/features/login.png)

#### Search and Category Views
These pages have a similar layout and function. They display the results of the user clicking on a category view from the drop down menu in the navbar, or from searching for a term in the search box in the navbar.

![index](/media/readme/features/search_results.png)
![index](/media/readme/features/category.png)

#### Profile Page
This page has two main functions. First, it allows the user to manage their email and password preferences. They can change their email address and their password. The user can also choose to delete their own account.

Below this section the user can also see a table listing all of the articles they have written, which can be clicked on to bring them to the article.

![index](/media/readme/features/profile.png)

#### Wishlist Page
Here the user can see a listing of all the books they have added to their wishlist. They can remove the book if they choose. If the original reviewer included a purchase link in their form, then the link will appear here and will be opened in a new window. 

Books in this list can also be marked as read or unread. Toggling this state with the Mark as Read button will add a strikethrough to the title to signal that the book has been read.

![index](/media/readme/features/wishlist.png)

#### Comments
The commenting system appears on individual review pages. Any logged in user can leave a comment on any review. They can also later edit or delete this comment. Additionally, the original author of any review page has the ability to remove comments on their pages if they wish, in order to provide a level of user moderation.

![index](/media/readme/features/comments.png)
![index](/media/readme/features/add_comment.png)

#### Footer
This footer appears at the bottom of every page on the site and provides easy access to the social media links for the project.

![index](/media/readme/features/footer.png)



## Future Features

There are a number of features which I would like to implement in the future for this website. They were left out due to being beyond the scope of this project in terms of time and complexity. The Kanban project board for this site tracks all the features and you can see a list of which issues have beenleft for future devleopment. [Kanban Board](https://github.com/neil314159/portfolio-project-4/projects/1) 

* Product Recommendation - most large-scale e-commerce retailers owe a large part of their success to recommending additional products to users which they are likely to buy. The main additional feature I would like to implement for this project is an affective algorithm to recommend purchases based on previous purchase history and the products in the shopping cart right now. Most real-world implementations of this feature use a databse to store a matrix of all lproducts, and then look for patterns of products clustered together. Some recommendation engines are quite complex and sophisticated, but can obviously lead to extra additional profits for any retailer.

* Artwork via API - the core idea of the site is selling artwork that have been generated by artificial intelligence. Currently, using these generator engine requires you to login directly to the website of the company supplying it. These services are not yet available via API, but when they eventually are, it means that a customer could enter a prompt or description of the poster they want to buy and have it generated dynamically for them on the spot before buying. The only downside is that the image can sometimes take a minute or two to generate, which may be too long for a casual customer. It should be noted that the text equivalents of these services such as GPT-3 are already avaialble via API, so I expect the visual services to follow suit.

* PDF generation - a feature that I really wanted to implement for this site is the ability to generate PDFs dynamically, so that the customer can download the receipt or have it emailed to them after their purchases. The generation of PDFs is dependent on a large number of third-party libraries, and while the feature worked locally on my own machine it proved unstable and resource-hungry when deployed to Heroku. The libraries could not be guaranteed to work every time and sometimes were very slow to generate the PDF, leaving the user waiting.

* Twitter API Integration - when adding new products to the site it is a good opportunity for the site owner to also automatically promote the product on social media. It is relatively easy to integrate with Twitter and send pictures and text programmatically. I signed up for the API and was able to send tweets when adding products to the database, e.g. automatically link back to the site with a picture of the newly added product, but unfortunalty due to a programming error I sent out thousands of duplicate tweets in a short time and got my developer account limited for review. I believe this would be a useful feature in the future and could be easily implemented. The Tweepy library for Django works well here. Unfortunately most other social media networks do not allow content to be posted directly via API.

* Charts for Dashboard - the administrative dashboard for the site was a large part of the project, allowing management of products and blog posts. It would be possible to integrate a charting library and display a visual record of sales for the last month for example.







## Technologies Used

* Python
    * These Python modules were used for the project:
       * asgiref==3.5.2
       * cloudinary==1.29.0
       * *crispy-bootstrap5==0.6
       * dj-database-url==1.0.0
       * dj3-cloudinary-storage==0.0.6
       * Django==3.2.15
       * django-allauth==0.51.0
       * django-countries==7.2.1
       * django-crispy-forms==1.14.0
       * django-htmx==1.12.1
       * gunicorn==20.1.0
       * mailchimp-marketing==3.0.75
       * oauthlib==3.2.0
       * Pillow==9.2.0
       * psycopg2==2.9.3
       * PyJWT==2.4.0
       * python3-openid==3.2.0
       * pytz==2022.1
       * requests-oauthlib==1.3.1
       * sqlparse==0.4.2
       * stripe==4.0.2

* Midjourney
    * all of the genrative art used on the site was created using the Midjourney engine. This is a recently developed platform, similar to the more widely known Dall-e@, which allows the user to enter a prompt or description and have visual art created for them on the spot. While there are some teething issues, in general the quality is extremely high and surprising to casual users.
* Heroku
    * The project was deployed using Heroku's cloud-based platform
* Heroku PostgreSQL
    * The database functionality was provided by the Heroku Postgres Add-on, in this case the free hobby-level package
* Django
    * Django is a high-level Python framework used to develop and deploy websites, noted for easily handling user authentication and handling user data
* Stripe
    * payment handling is essential for any store, and the Stripe library allows for the easy processing of payments to be integrated into the site. They have extensive documentation and developer tutorials
* Sendgrid
    * The SendGrid API allows Django to send out emails for user account operations. A service like this is essential as a store scales up and personal email setups can no longer be used to deliver large volumes of email.
* Mailchimp
    * In contrast to Sendgrid, which is used for large-volume transactional email, Mailchimp is used fo rnewsletter managemnt. It is capable of quite sophisticated stratgeies to segment customer lists, send out automated marketing and offers conditonal on user behaviour.
* Cloudinary
    * used fo rhandling static storage and well-known for their image-processing abilities
* AllAuth
    * used fo rhandling user registration and authorisation management. It takes over these tasks from the Django native impelementation, and makes it much easier to handle tasks such as verifying email addresses  and resetting passwords.
* HTML
    * HTML was used mainly to style the templates used by Django for displaying the front end of the site.
* CSS
    * A small amount of CSS was written to style the background and fonts for the project.
* Bootstrap
    * A comprehensive CSS framework used to quickly provide layout and styling for web pages
* Font Awesome
    * The Font-Awesome icon library was used for the social media links in the footer of the site.


#### Other Resources Used
* [Github](https://github.com) 
    * GitHub is used for version control and as a repository for the code of the project.
* [Gitpod](https://gitpod.io) 
    * Gitpod was the development environment for this site and linked to Github for storage and deployment.
* [MacOS Preview](https://support.apple.com/guide/preview/welcome/mac)
    * All screenshots were captured and edited with this program.
* Balsamiq
    * Used to develop and refine wireframe images in the planning stage of the project.
* Cloudinary API Reference
    * This was used to understand how to apply image transformations when uplaoding and storing images on their service.


## Testing


A comprehensive manual testing plan was used for this project. A full description of all of the procedures and methods used can be found in the [testing.md file here](TESTING.md). All functionality relating to user actions and CRUD operations was carefully examined. Wherever possible, testing was also related back to the acceptance criteria in the original Epics defined before development began.


## Notable Bugs

1. Slug Creation
    * P

1. Slug Creation
    * P

1. Slug Creation
    * P





# Deployment

## Creating the Project
1. A new repository was created for the project on GitHub by clicking 'New Repository' on the GitHub user page, giving a name to the project.
1. The GitPod link created by the Chrome extension was clicked on the Code Institute Python template found [here](https://github.com/Code-Institute-Org/python-essentials-template).
1. This created a virtual workspace which was then linked to my GitHub account.
1. After writing code for the project, I used git commands add, commit and push which sent all the project files from GitPod to my GitHub repository.

## Deploying to Heroku
The project was deployed on the Heroku site by using these steps:
1. Create a new account on Heroku.
1. Log into your account.
1. Click on the 'New' button and click 'Create New App'.
1. Choose a new name for your app, which must be globally unique to your app.
1. Select the Resources menu option from the top of the page.
1. Search in the Add-ons search box for Heroku Postgres.
1. Select the Heroku Postgres Add on from the results list and accept the hobby level tier.
1. Click on the settings tab and go to the hidden variables section.
1. Here you can add your SECRET_KEY variable which is hidden within the env.py in your Django project. It is a good idea to generate a new secret key rather than using the default one.
1. Make a note of the DATABASE_URL so that you can use it in your own env.py to connect directly to the Heroku databse during development.
1. You can also add a key for static storage such as Cloudinary or S3.
1. Click the Deploy tab in Heroku.
1. Connect your project to your Github Repository and select automatic deployment. This will deploy your project after every time you push your changes to Github.
1. For an e-commerce project such as this, you will need to use Stripe or another payment provider. 
1. Once you sign up with a payment provider, add their API keys to the secret variables section on Heroku and in your own env.py file.


## Local Deployment

#### Forking the repo on GitHub
1. Navigate to the Github page and log into your GitHub account.
1. Navigate to the project page found [here](https://github.com/neil314159/portfolio-project-5).
1. Click on the 'Fork' icon on the upper right hand side of the screen.
1. This makes a copy of the code in your own repo so you can examine it or open it in an IDE.

#### Download a zip file of the source code
1. Click this [link](https://github.com/neil314159/portfolio-project-5) to the project home page.
1. Click the 'Code' button on the right hand side.
1. Select "Download Zip' option from the menu.
1. Unzip the files on your own machine.
1. Open them in the development environment of your choice.

# Credits

## Pictures

* All pictures used on the site as product photos were generated using the Midjourney AI picture generator. This is available to the public and operates through a discord server. [Midjourney](https://www.midjourney.com)


## Coding Inspiration

[Bug Bytes](https://www.bugbytes.io/) - this website and YouTube channel provided a good overview of Django development and the techniques on how to use HTMX in the context of designing websites <br>
[William Vincent Django for Professionals](https://wsvincent.com/) - His book Django for Professional gives a good overview of how to implement custom user models and incorporate them into the signup flow for the website.<br>
[Bootstrap Examples](https://getbootstrap.com/docs/5.2/examples/) - The example code provided here gave ideas on how to lay out and refine the presentation of the site. <br>
[Stack Overflow](https://stackoverflow.com/questions/65365131/letting-users-delete-their-own-accounts-in-django) - this was used for many queries relating to jungle, for example this question on how to allow the user to delete their own account.

# Acknowledgements

* Thanks to Code Institute mentor Daisy McGirr for all of her advice and guidance.