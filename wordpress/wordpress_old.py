import requests


class Page:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_pages(self):
        """Fetches all pages."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/pages"
        response = requests.get(endpoint, auth=self.auth)
        pages = []
        if response.status_code == 200:
            fetch_pages = response.json()
            for page in fetch_pages:
                pages.append(page)
            return pages
        else:
            print(f"Failed to fetch pages: {response.status_code}")

    def create_page(self, title, content, status="publish"):
        """Creates a new page."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/pages"
        data = {
            "title": title,
            "content": content,
            "status": status
        }
        response = requests.post(endpoint, json=data, auth=self.auth)
        if response.status_code == 201:
            print(f"Page created successfully: {response.json()}")
        else:
            print(f"Failed to create page: {response.status_code}, {response.text}")

    def delete_page(self, page_id):
        """Deletes a page by its ID."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/pages/{page_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"Page with ID {page_id} deleted successfully.")
        else:
            print(f"Failed to delete page with ID {page_id}: {response.status_code}, {response.text}")

    def fetch_page(self, page_id):
        """Fetches a specific page by its ID."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/pages/{page_id}"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            page = response.json()
            print(page)
        else:
            print(f"Failed to fetch page with ID {page_id}: {response.status_code}")

class Post:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_posts(self):
        """Fetches all posts."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/posts"
        response = requests.get(endpoint, auth=self.auth)
        posts = []
        if response.status_code == 200:
            fetch_posts = response.json()
            for post in fetch_posts:
                posts.append(post)
            return posts
        else:
            print(f"Failed to fetch posts: {response.status_code}")

    def create_post(self, title, content, status="publish"):
        """Creates a new post."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/posts"
        data = {
            "title": title,
            "content": content,
            "status": status
        }
        response = requests.post(endpoint, json=data, auth=self.auth)
        if response.status_code == 201:
            print(f"Post created successfully: {response.json()}")
        else:
            print(f"Failed to create post: {response.status_code}, {response.text}")

    def delete_post(self, post_id):
        """Deletes a post by its ID."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/posts/{post_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"Post with ID {post_id} deleted successfully.")
        else:
            print(f"Failed to delete post with ID {post_id}: {response.status_code}, {response.text}")

    def fetch_post(self, post_id):
        """Fetches a specific post by its ID."""
        endpoint = f"{self.base_url}/wp-json/wp/v2/posts/{post_id}"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            post = response.json()
            print(post)
        else:
            print(f"Failed to fetch post with ID {post_id}: {response.status_code}")

class Category:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_categories(self):
        endpoint = f"{self.base_url}/wp-json/wp/v2/categories"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            categories = response.json()
            for category in categories:
                print(category)
        else:
            print(f"Failed to fetch categories: {response.status_code}")

    def create_category(self, name, description=""):
        endpoint = f"{self.base_url}/wp-json/wp/v2/categories"
        data = {
            "name": name,
            "description": description
        }
        response = requests.post(endpoint, json=data, auth=self.auth)
        if response.status_code == 201:
            print(f"Category created successfully: {response.json()}")
        else:
            print(f"Failed to create category: {response.status_code}, {response.text}")

    def delete_category(self, category_id):
        endpoint = f"{self.base_url}/wp-json/wp/v2/categories/{category_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"Category with ID {category_id} deleted successfully.")
        else:
            print(f"Failed to delete category with ID {category_id}: {response.status_code}, {response.text}")

class Media:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_media(self):
        endpoint = f"{self.base_url}/wp-json/wp/v2/media"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            media_items = response.json()
            for item in media_items:
                print(item)
        else:
            print(f"Failed to fetch media: {response.status_code}")

    def upload_media(self, file_path):
        endpoint = f"{self.base_url}/wp-json/wp/v2/media"
        headers = {
            "Authorization": f"Bearer {self.auth[0]}",
            "Content-Disposition": f"attachment; filename={file_path}"
        }
        with open(file_path, 'rb') as file:
            response = requests.post(endpoint, headers=headers, files={'file': file})
        if response.status_code == 201:
            print(f"Media uploaded successfully: {response.json()}")
        else:
            print(f"Failed to upload media: {response.status_code}, {response.text}")

    def delete_media(self, media_id):
        endpoint = f"{self.base_url}/wp-json/wp/v2/media/{media_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"Media with ID {media_id} deleted successfully.")
        else:
            print(f"Failed to delete media with ID {media_id}: {response.status_code}, {response.text}")

class User:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_users(self):
        endpoint = f"{self.base_url}/wp-json/wp/v2/users"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                print(user)
        else:
            print(f"Failed to fetch users: {response.status_code}")

    def create_user(self, username, email, password):
        endpoint = f"{self.base_url}/wp-json/wp/v2/users"
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        response = requests.post(endpoint, json=data, auth=self.auth)
        if response.status_code == 201:
            print(f"User created successfully: {response.json()}")
        else:
            print(f"Failed to create user: {response.status_code}, {response.text}")

    def delete_user(self, user_id):
        endpoint = f"{self.base_url}/wp-json/wp/v2/users/{user_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"Failed to delete user with ID {user_id}: {response.status_code}, {response.text}")

    def fetch_user(self, user_id):
        endpoint = f"{self.base_url}/wp-json/wp/v2/users/{user_id}"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            user = response.json()
            print(user)
        else:
            print(f"Failed to fetch user with ID {user_id}: {response.status_code}")

class Comment:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip('/')
        self.auth = auth

    def fetch_all_comments(self):
        endpoint = f"{self.base_url}/wp-json/wp/v2/comments"
        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            comments = response.json()
            for comment in comments:
                print(comment)
        else:
            print(f"Failed to fetch comments: {response.status_code}")

    def create_comment(self, post_id, content):
        endpoint = f"{self.base_url}/wp-json/wp/v2/comments"
        data = {
            "post": post_id,
            "content": content
        }
        response = requests.post(endpoint, json=data, auth=self.auth)
        if response.status_code == 201:
            print(f"Comment created successfully: {response.json()}")
        else:
            print(f"Failed to create comment: {response.status_code}, {response.text}")

    def delete_comment(self, comment_id):
        endpoint = f"{self.base_url}/wp-json/wp/v2/comments/{comment_id}"
        response = requests.delete(endpoint, auth=self.auth)
        if response.status_code == 200:
            print(f"Comment with ID {comment_id} deleted successfully.")
        else:
            print(f"Failed to delete comment with ID {comment_id}: {response.status_code}, {response.text}")

class Connect:
    def __init__(self, site_url, username, password):
        self.base_url = site_url.rstrip('/')
        self.auth = (username, password)
        url = f'{self.base_url}/wp-json/wp/v2/users/me'
        response = requests.get(url, auth=self.auth)
        if response.status_code != 200:
            print('Error while authenticating')
            print(response.json())
            raise Exception('Authentication failed')
        self.page = Page(self.base_url,self.auth)
        self.post = Post(self.base_url,self.auth)
        self.category = Category(self.base_url,self.auth)
        self.media = Media(self.base_url,self.auth)
        self.user = User(self.base_url,self.auth)
        self.comment = Comment(self.base_url,self.auth)









