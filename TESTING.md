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

| Filename        | Results           | Comments  |
| ------------- |:-------------:| -----:|
|   base.css  |  Pass, no errors |  |
|   checkout.css  |  Pass, no errors|  |

![homepage](/media/readme/testing/css/css.png)


<br>

## User Testing

During the development of the site, a third-party user was asked to navigate the menus and links while being observed. I asked them to carry out some tasks, such as purchase a product or bring up a blog post. After carrying out a number of operations, I requested feedback on the usability and aesthetics of the site.

After doing this 3 times with different users, the main feedback I noted was:
* Most users are familiar with the idea of an online shop or blog, and don't need to have the fundamental concepts explained
* For tasks that are similar to how most large website operate, for exmpale, adding an item to a cart and checking out, there were few problems encountered.
* Most feedback was of an aesthetic nature. All users expressed a preference for clean fonts that were not too heavyweight in appearance. They also liked simpler colour schemes and clear contrast to indicate menu items.

This feedback was noted and incorporated into the development process.


## Acceptance Criteria Measurement

The original acceptance criteria laid out in the user stories before development began are examined here to determine if they were met in a satisfactory fashion.


####

*   USER STORY: Set up S3 Storage #23
    * Given that I upload a file or image to the website
    * When file is uploaded
    * Then it is stored in secure cloud storage
| Criteria Met       | Comments           | 
| ------------- |:-------------:| 
|   Yes  |  Cloudinary used in place of S3 |  

###

## Test Cases

###