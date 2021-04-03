# High Level Approach

- We began by implementing the GET request to receive the login page HTML and retrieving the csrfmiddleware token
- Then we implemented the POST request to login in to Fakebook
- Once we were able to log in, we abstracted our GET request to then request the HTML for each page
- Then we built a parser for the html code to retrieve all of the links to other pages and also searches for the secret flags
- We built a crawler method that creates a queue of all the links that need to be crawled
- Once all the links are crawled we returned the secret flags
-

# To test

We called the webcrawler on both our login username and passwords and checked to ensure that the 5 secret flags were returned.
