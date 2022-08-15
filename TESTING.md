# Testing Report

## Validation Testing

## Python Validation

All Python code was run through the online validator found at http://pep8online.com/



### Bag App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   admin.py   | Pass |  |
| apps.py      |   Pass    |    |
| contexts.py |   Pass    |    |
| models.py | Pass      |    |
| tests.py | Pass      |    |
| urls.py |   Pass    |    |
| views.py |  Pass     |    |

### Blog App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   admin.py   | Pass |  |
| apps.py      |     Pass  |    |
| models.py |   2 lines too long    | Cloudinary URLS for image references, cannot be shortened   |
| tests.py |   Pass    |    |
| urls.py |   Pass    |    |
| views.py |    Pass   |    |

### Dashboard App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   admin.py   |  Pass|  |
| apps.py      |    Pass   |    |
| models.py |  Pass     |    |
| tests.py |   Pass    |    |
| views.py | Pass      |    |

### Electric Dreams App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   settings.oy   | 5 lines too long | due to password validator names, cannot be shortened |
| urls.py      |   Pass    |    |
| models.py |    Pass   |    |
| wsgi.py |   Pass    |    |
| views.py |   Pass    |    |

### Home App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   admin.py   |  Pass|  |
| apps.py      |    Pass   |    |
| forms.py      |    Pass   |    |
| models.py |  Pass     |    |
| tests.py |   Pass    |    |
| urls.py      |   Pass    |    |
| views.py | Pass      |    |

### Profiles App
| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   admin.py   |  Pass|  |
| apps.py      |    Pass   |    |
| forms.py      |    Pass   |    |
| models.py |  Pass     |    |
| tests.py |   Pass    |    |
| urls.py      |   Pass    |    |
| views.py | Pass      |    |



### HTML Validation

Due to the nature of Django and the tenplating used, it is not simple to test for HTML errors. I manually anvigated to each fiel path in the site and pasted the source code for each page into the HTML validator at https://validator.w3.org

There are a number of errors that are flagged due to the use of the HTMX.js library. This is used for allowing user interaction without full page refreshes, and it uses a number of tags and classes that set off validation errors. On the blog page there was also an error caused by a new line symbol coming through in the blog text and being interpreted as a close paragraph tag. This would be fixable by chaging the blog post text field to use a rich text field instead.

| Filepath        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   /  |  Pass, no errors | incorrect tag on newsletter form, fixed |
|   /products/  |  Pass, no errors|  |
|   /products/22  |  Pass, no errors |  |
|   /blog/  |  Pass, no errors |  |
|   /blog/post/27  |  Pass, no errors | newline from blog text model causing stray p tag |
|   /artrequest/  |  Pass, no errors |  |
|   /profile/myorders/  |  Pass, no errors | stray div tag on orders table, fixed |
|   /profile/wishlist/  |  Pass, no errors |  |
|   /dashboard/products/  |  Pass, no errors |  |
|   /dashboard/orders/  |  Pass, no errors |  |
|   /dashboard/blog/  |  Pass, no errors |  |
|   /dashboard/customerrequests/  |  Pass, no errors |  |


### CSS Validation

CSS validation was carried out using https://jigsaw.w3.org/css-validator/

| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   base.css  |  Pass, no errors |  |
|   checkout.css  |  Pass, no errors|  |


### JS Validation

JS files were evaluated on https://jshint.com

| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   stripe_elements.js  |  Pass, no errors |  |





<br>

## User Testing

During the development of the site, a third-party user was asked to navigate the menus and links while being observed. I asked them to carry out some tasks, such as purchase a product or bring up a blog post. After carrying out a number of operations, I requested feedback on the usability and aesthetics of the site.

After doing this 3 times with different users, the main feedback I noted was:
* Most users are familiar with the idea of an online shop or blog, and don't need to have the fundamental concepts explained
* For tasks that are similar to how most large website operate, for example, adding an item to a cart and checking out, there were few problems encountered.
* Most feedback was of an aesthetic nature. All users expressed a preference for clean fonts that were not too heavyweight in appearance. They also liked simpler colour schemes and clear contrast to indicate menu items.

This feedback was noted and incorporated into the development process.


## Acceptance Criteria Measurement

The original acceptance criteria laid out in the user stories before development began are examined here to determine if they were met in a satisfactory fashion. Note: not all user stories had acceptance criteria, some were simply task lists.



 #### USER STORY: Set up S3 Storage #23
* Given that I upload a file or image to the website
* When file is uploaded
* Then it is stored in secure cloud storage

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  Cloudinary used in place of S3 |  




 #### USER STORY: Create User Profile #17
 * Acceptance Criteria 1
	* Given that I am a new user without an account
	* When I visit the homepage
	* Then I can click the account button and see a link to register a new profile
* Acceptance Criteria 2
	* Given that I clicked on the register button
	* When I enter my details such as name and email address
	* Then my account is created and I am automatically signed in
* Acceptance Criteria 3
	* Given that I am a registered user
	* When I visit the homepage
	* Then the menu changes to no longer show a register button

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |   |  



 #### USER STORY: Email Login instead of Username #18
 * Acceptance Criteria 1
    * Given that I register for an account on the site
    * When I input my details on the registration form
    * Then I only need to use my email address to register

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |   |  



#### USER STORY: View User Profile #19
* Acceptance Criteria 1
    * Given that I have logged into the site
    * When I view the menu in the navbar
    * Then I see a link which will take me to my own profile page
* Acceptance Criteria 2
    * Given that I have clicked on the menu option to view my profile
    * When the profile page loads
    * Then I can view my wishlist, past orders and addresses stored on the site

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |   |  



#### USER STORY: Update User Profile #20
* Acceptance Criteria 1
    * Given that I am logged into the site and viewing my profile page
    * When I see my email address displayed
    * Then I can see a link to update my email address
* Acceptance Criteria 2
    * Given that I am viewing my profile page
    * When I see my personal addresses
    * Then I can edit the details of these addresses
* Acceptance Criteria 3
    * Given that I am not logged in to the site
    * When I attempt to view my user profile
Then I am redirected to the login page

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Only one address is stored rather than multiple  |  



#### USER STORY: Delete User Profile #21
* Acceptance Criteria 1
    * Given that I am registered on the site and logged in to my account
    * When I click on my profile page link
    * Then I can see a button allowing me to delete my account
* Acceptance Criteria 2
    * Given that I click the button to delete my profile
    * When a confirmation dialog is shown
    * Then I can confirm or reject the option to delete my account
* Acceptance Criteria 3
    * Given that I confirmed my desire to delete the account
    * When the account is successfully deleted
    * Then I am logged out and returned to the home page

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Implemented to satisfy GDPR compliance  |  



#### USER STORY: Store Multiple Addresses #22
* Acceptance Criteria 1
    * Given that I am checking out my cart on the site
    * When the checkout form appears
    * Then I have the option to select from a a number of saved addresses
* Acceptance Criteria 2
    * Given that I am viewing my profile page
    * When I access the addresses section
    * Then I have the option to add and store multiple addresses

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | Deferred for future development |  



#### USER STORY: Authenticate User Login/Logout #24
* Acceptance Criteria 1
    * Given that I am not logged in to the site
    * When I click the login button
    * Then I can enter my personal login details and log into the site with the correct name and password
* Acceptance Criteria 2
    * Given that I am logged in to the site as a user
    * When I click the logout button
    * Then my account is fully signed out and I am redirected to the home page

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Social Media Login #25
* Acceptance Criteria 1
    * Given that I select the register account button on the navbar
    * When I see the registration form
    * Then I am given the option to sign in with alternative account providers such as Google or Twitter
* Acceptance Criteria 2
    * Given that I have logged in with my social account
    * When the login process is complete
    * Then I am redirected to the homepage

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | For future release |  



#### USER STORY: Reset User Password #26
* Acceptance Criteria 1
    * Given that I attempt to log in to the site with my credentials
    * When I enter a wrong password 
    * Then I can select a link to reset my password
* Acceptance Criteria 2
    * Given that I click on the link to reset my password
    * When I confirm my email address
    * Then I am sent a link to my email address to allow resetting the password
* Acceptance Criteria 3
    * Given I have clicked this link and successfully reset my password
    * When I attempt to log in
    * Then my new password should work properly

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Authenticate User Actions #27
* Acceptance Criteria 1
    * Given that a user is not logged in
    * When they attempt to carry out operations such as adding or editing a comment or review
    * Then they will be redirected to the user login/registration page
* Acceptance Criteria 2
    * Given that a user is not logged in
    * When they attempt to carry our any CRUD operations through URL access
    * Then they will be denied and redirected to the home page

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: View Store Items #28
* Acceptance Criteria 1
    * Given that I have clicked the link to view the shop
    * When I open the shop page
    * Then I can view a list of all items for sale in the shop
* Acceptance Criteria 2
    * Given that I have selected a category of product
    * When items are displayed
    * Then only items from the selected category are shown
* Acceptance Criteria 3
    * Given that I select a method of ranking the items such as price, alphabetically
    * When items are presented to me
    * Then they are in the correct order

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: View Product Details #29
* Acceptance Criteria 1
    * Given that I am viewing a list of products for sale on the site
    * When I click on the thumbnail of a particular product
    * Then I can see a new page with in-depth details of the product
* Acceptance Criteria 2
    * Given that I am viewing the Product page
    * When product details are presented to me
    * Then I can select size, quantity options before adding to the shopping cart

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Edit Products #30
* Acceptance Criteria 1
    * Given that I am in administrator on the site
    * When I login to the site
    * Then I can see edit buttons on the product pages
* Acceptance Criteria 2
    * Given I have clicked the product edit button
    * Then I am presented with a form to make these edits
* Acceptance Criteria 3
    * Given that I have adjusted the details of the product
    * When the form is submitted
    * Then the new details appear on product listing

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Edit functionality is present, although moved from product page to the management dashboard |  



#### USER STORY: Delete Products #31
* Acceptance Criteria 1
    * Given that I am a site administrator
    * When I view a product page
    * Then there is a delete button available
* Acceptance Criteria 2
    * Given I have clicked the delete product button
    * When the dialogue prompt is confirmed
*    Then the product was deleted

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Products are deleted from the product overview page rather than the detail page |  



#### USER STORY: Add New Product #32
* Acceptance Criteria 1
    * Given that I am a logged in administrator on the site
    * When I view the navbar menu
    * Then there is a link to add a new product
* Acceptance Criteria 2
    * Given I have clicked the link to add new product
    * Then I am presented with a form to enter the product details
* Acceptance Criteria 3
    * Given I have entered these details and uploaded any required images
    * When the submit button is clicked
    * Then the new product is created and appears on the site

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Search Functionality #33
* Acceptance Criteria 1
    * Given that I am a user on the site
    * When I examine the navbar menu
    * Then I can access a search box
* Acceptance Criteria 2
    * Given that I have entered a term into the search box
    * When the button is clicked or I hit return
    * Then a list of products matching my query is displayed

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Live search was implemented for instant user feedback |  



#### USER STORY: Add Product to Cart #34
* Acceptance Criteria 1
    * Given that I am browsing the site as a registered or unregistered user
    * When I click the add to cart button on a product I wish to purchase
    * Then the product is added to my shopping cart
* Acceptance Criteria 2
    * Given I am a customer on the site
    * When I add a product for the second time
    * Then the shopping cart updates to increase the quantity of the item

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Edit/Remove Shopping Cart Items #35
* Acceptance Criteria 1
    * Given that I am viewing my shopping cart
    * When I click to adjust the quantity of items in the cart
    * Then the cart updates to reflect these changes
* Acceptance Criteria 2
    * Given that I click delete on an item in the shopping cart
    * Then the item is removed from the cart
* Acceptance Criteria 3
    * Given that an item has been removed from the cart
    * When item is gone an undo link appears in its place
    * Then it is possible to undo the removal of the item

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Partial  | Edit and delete are working, undo delete was deferred for future development |  



#### USER STORY: View Shopping Cart #36
* Acceptance Criteria 1
    * Given that I am user on the site
    * When I click the shopping cart link in the navbar
    * Then I can see all the items in my cart at a glance

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |  



#### USER STORY: Coupon Code #60
* Acceptance Criteria 1
    * Given that I am a user at the checkout page
    * When I enter a coupon code in the provided box
    * Then the total of my shopping cart amount is reduced my the amount of the coupon
* Acceptance Criteria 2
    * Given that I am an admin user on the site
    * When I log in to the admin dashboard
    * Then I have the option to add, edit or delete coupon codes

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | Deferred for future development | 



#### USER STORY: Purchase Recommendations #61
* Acceptance Criteria 1
    * Given that I am a customer on the site
    * When I view a product detail page
    * Then I can see a short list of other products that other customers have purchased at the same time as the product I am looking at
* Acceptance Criteria 2
    * Given that I am viewing this shortlist of recommended purchases
    * When I click the thumbnail of one of the recommendations
    * Then I am taken to the product page where I can add it to my cart

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | To be implemented at a later date  | 




#### USER STORY: Checkout Page #37
* Acceptance Criteria 1
    * Given that I am user on the site
    * When I am on the shopping cart page
    * Then I can click to proceed to the checkout

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  | 




#### USER STORY: View Order Details #38
* Acceptance Criteria 1
    * Given that I have entered my payment details and clicked Order
    * When the payments has completed
    * Then I can see the details of my order
* Acceptance Criteria 2
    * Given that I am user on the site
    * When the order has been successfully processed
    * Then the order will appear on my profile page and I will receive a confirmation email

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  | 



#### USER STORY: PDF Receipt #39
* Acceptance Criteria 1
    * Given that I am a user on the site
    * When I view the order confirmation page
    * Then I can see a link to download a PDF receipt of my order
* Acceptance Criteria 2
    * Given that I have placed a successful order
    * Then I will receive a copy of my PDF receipt in my email confirmation

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | PDF generation worked on local machine, but has many dependencies and did work reliably on heroku, often hanging, so feature was removed | 



#### USER STORY: Add Product Review #40
* Acceptance Criteria 1
    * Given that I am a logged in user on the site
    * When I am viewing a product I previously purchased
    * Then I can see a link to add a review
* Acceptance Criteria 2
    * Given that I have clicked the link to add a review
    * When the review is submitted
    * Then the review appears on the site

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  | 



#### USER STORY: Edit/Delete Reviews #41
* Acceptance Criteria 1
    * Given I am a logged in user on the site
    * When I am viewing a review I have written
    * Then I will see buttons allowing me to edit or delete my reviews
* Acceptance Criteria 2
    * Given that I have clicked to edit my review
    * Then I will be presented with a form allowing me to make changes to my review
* Acceptance Criteria 3
     Given that I have clicked to delete my review
    * When the prompt to delete is confirmed
    * Then the review will be deleted from the product page

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Partial  | Comments left on the site can be deleted but not edited |



#### USER STORY: Calculate Product Ratings #42
* Acceptance Criteria 1
    * Given that I am a user on the site
    * When I leave a review with a star rating
    * Then this rating is added to the product database
* Acceptance Criteria 2
    * Given that I am user browsing the site
    * When the product thumbnails are presented to me
    * Then the review scores of each product are shown in the product details

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | Reviews were switched so comments, with no rating elemnt |



#### USER STORY: Read Blog #43
* Acceptance Criteria 1
    * Given that I am customer on the site
    * When I click the blog button in the navbar
    * Then I can access the blog section of the site
* Acceptance Criteria 2
    * Given that I have clicked the blog button in the navbar
    * Then I will see a dropdown menu offering a choice of blog categories to browse
* Acceptance Criteria 3
    * Given that I am a user browsing the blog
    * When I click on the article thumbnail
    * Then I can read the individual blog post

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Create, Edit, Delete Blog Entries #44
* Acceptance Criteria 1
    * Given that I am an admin user on the site
    * When I click the blog section in the navbar
    * Then I have the option to create a new blog post
* Acceptance Criteria 2
    * Given that I have selected the option to create a new blog post
    * When the details of the post have been submitted
    * Then the new post appears on the site
* Acceptance Criteria 3
    * Given that I am an admin user on the site
    * When viewing a post I can see buttons to edit or delete the post
    * Then after selecting these options the post can be updated or removed

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Add, Edit and Delete Blog Categories #45
* Acceptance Criteria 1
    * Given that I am a logged in admin user
    * When I am viewing the blog admin page
    * Then I can see buttons allowing me to add, edit and remove categories for the blog
* Acceptance Criteria 2
    * Given that I have selected to add a new category
    * Then a new category is added to the form for creating a new blog post
* Acceptance Criteria 3
    * Given that I am in the blog admin page
    * When I select to edit or remove a blog category
    * Then this action is reflected in the navbar menu and the new post form

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Add/Remove Wishlist Items #46
* Acceptance Criteria 1
    * Given that I am a logged in user viewing a product page
    * When I click the icon to add an item to my wishlist
    * Then the item is added to my wishlist
* Acceptance Criteria 2
    * Given that I am a logged in user viewing a product page
    * When I click the toggle button to remove the item from the wishlist
    * Then the item is removed and the icon toggles to reflect this

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: View Wishlist on Profile Page #47
* Acceptance Criteria 1
    * Given that I am a logged in user on the site
    * When I click my profile page
    * Then I can see a section detailing all my wishlist items
* Acceptance Criteria 2
    * Given that I am viewing my wishlist on the profile page
    * When viewing the list
    * Then I can see buttons to remove any item from the wishlist

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Admin Dashboard #48
* Acceptance Criteria 1
    * Given that I am a logged in admin user
    * When I click the admin link in the navbar
    * Then I am presented with an admin dashboard for the site
* Acceptance Criteria 2
    * Given that I am viewing the admin dashboard
    * Then I can see shortcut buttons for adding, editing and removing blog posts or categories
* Acceptance Criteria 3
    * Given that I am viewing the admin dashboard
    * Then I can see shortcut buttons for adding, editing and removing products
* Acceptance Criteria 4
    * Given that I am viewing the admin dashboard
    * Then I can see a list overview of all products and blog posts on the site

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  | Dashboard switched to admin menu in navbar with direct links to admin functions |



#### USER STORY: Set Order Status #49
* Acceptance Criteria 1
    * Given that I am logged into the admin dashboard
    * When viewing a list of all orders on the site
    * Then I can see by colour-coding which ones have been shipped
* Acceptance Criteria 2
    * Given that I click on an individual order
    * When viewing the order details
    * Then I can click a button to update the status as shipped/unshipped

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Order Chart #50
* Acceptance Criteria 1
    * Given that I am a logged in admin user
    * When I am viewing the admin dashboard
    * Then I can see a bar chart showing all sales over the last week/month

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | Feature left for future development |



#### USER STORY: Printable Shipping Labels #51
* Acceptance Criteria 1
    * Given that I am a logged in admin user
    * When viewing the admin dashboard
    * Then I can click a link to generate a PDF download with the shipping details of all open orders

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Partial  | Had same problem as above with PDF receipts, but switched to visual indicator on order overview page showing shipped/unshipped orders |



#### USER STORY: Custom Product Form #53
* Acceptance Criteria 1
    * Given that I am a user on the site
    * When viewing the navbar or footer menu
    * Then I can click a link to a custom request form
* Acceptance Criteria 2
    * Given that I have clicked the link
    * When I have filled out my details
    * Then the form is sent to the database and a copy sent to the email address of the site owner

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  |



#### USER STORY: Twitter API Integration #56
* Acceptance Criteria 1
    * Given that I am an admin user creating a new product
    * When I tick the box to post the product to twitter
    * Then when the product is created on the site a link will be posted to Twitter automatically, linking back to the product
* Acceptance Criteria 1
    * Given that I am an admin user creating a new blog post
    * When I tick the box to post the blog to twitter
    * Then when the post is created on the site a link will be posted to Twitter automatically, linking back to the post

| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   No  | Was functioning as a proof-of-concept, but my developer account was locked for review due to accidentally sending too many tweets due to a bug, so couldn't be sure it would work when deployed |



