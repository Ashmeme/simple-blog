A simple Blog backend.

used technologies:

django
djangorestframework
requests
djangorestframework-simplejwt


API Endpoints:

api/blog/posts/
            GET
            : Allowed for everyone, retrieves a serialized list of posts
            
            POST
            : Allowed for authorized users, creates a post
            {"title": string, "content":string, "publish_date": date and time}

            UPDATE
            : Allowed for authorized users, updates a post

            DELETE
            : Allowed for authorized users, deletes a post
            
         
         
         comments/
            GET
            : Allowed for everyone, retrieves a serialized list of comments
            
            POST
            : Allowed for authorized users, creates a comment
            {"post": id, "author_name":string, "comment_text":string, "created_date": date and time}

            UPDATE
            : Allowed for authorized users, updates a comment

            DELETE
            : Allowed for authorized users, deletes a comment
            

api//token/             // only POST: {"user":"", "Password":""} for token 
          /refresh/
          /verify/


