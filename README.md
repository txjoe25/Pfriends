# Pfriends
Create an application that will perform all the CRUD operations on the friends resource:

- In Index.html, each friend should have an "edit" button that will take the user to the '/friends/<id>/edit' URL which should display the edit page for that particular user
- The edit page form should send a POST request to '/friends/<id>' which will actually update the user in the database with the new inputs
- In Index.html, each friend should have a "delete" button (part of a form) that should POST to '/friends/<id>/delete'. This route should delete the user from the database
