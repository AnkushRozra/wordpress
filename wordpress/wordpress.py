import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class WPBase:
    def __init__(self, site_url, auth):
        self.base_url = site_url.rstrip("/")
        self.auth = auth

    def _make_request(self, method, endpoint, data=None, files=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method, url, json=data, files=files, headers=headers, auth=self.auth
            )
            if response.status_code in [200, 201]:
                return response.json()
            logging.error(f"Request failed: {response.status_code}, {response.text}")
            return None
        except Exception as e:
            logging.exception(f"Error during request to {url}: {e}")
            return None


class Page(WPBase):
    def fetch_all(self):
        """Fetches all pages."""
        return self._make_request("GET", "/wp-json/wp/v2/pages")

    def create(self, title, content, status="publish"):
        """Creates a new page."""
        data = {"title": title, "content": content, "status": status}
        return self._make_request("POST", "/wp-json/wp/v2/pages", data=data)

    def delete(self, page_id):
        """Deletes a page by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/pages/{page_id}")

    def fetch(self, page_id):
        """Fetches a specific page by ID."""
        return self._make_request("GET", f"/wp-json/wp/v2/pages/{page_id}")


class Post(WPBase):
    def fetch_all(self):
        """Fetches all posts."""
        return self._make_request("GET", "/wp-json/wp/v2/posts")

    def create(self, title, content, status="publish"):
        """Creates a new post."""
        data = {"title": title, "content": content, "status": status}
        return self._make_request("POST", "/wp-json/wp/v2/posts", data=data)

    def delete(self, post_id):
        """Deletes a post by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/posts/{post_id}")

    def fetch(self, post_id):
        """Fetches a specific post by ID."""
        return self._make_request("GET", f"/wp-json/wp/v2/posts/{post_id}")


class Media(WPBase):
    def fetch_all(self):
        """Fetches all media items."""
        return self._make_request("GET", "/wp-json/wp/v2/media")

    def upload(self, file_path):
        """Uploads media to WordPress."""
        headers = {"Content-Disposition": f"attachment; filename={file_path}"}
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self._make_request("POST", "/wp-json/wp/v2/media", files=files, headers=headers)

    def delete(self, media_id):
        """Deletes a media item by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/media/{media_id}")


class Category(WPBase):
    def fetch_all(self):
        """Fetches all categories."""
        return self._make_request("GET", "/wp-json/wp/v2/categories")

    def create(self, name, description=""):
        """Creates a new category."""
        data = {"name": name, "description": description}
        return self._make_request("POST", "/wp-json/wp/v2/categories", data=data)

    def delete(self, category_id):
        """Deletes a category by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/categories/{category_id}")


class User(WPBase):
    def fetch_all(self):
        """Fetches all users."""
        return self._make_request("GET", "/wp-json/wp/v2/users")

    def create(self, username, email, password):
        """Creates a new user."""
        data = {"username": username, "email": email, "password": password}
        return self._make_request("POST", "/wp-json/wp/v2/users", data=data)

    def delete(self, user_id):
        """Deletes a user by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/users/{user_id}")

    def fetch(self, user_id):
        """Fetches a specific user by ID."""
        return self._make_request("GET", f"/wp-json/wp/v2/users/{user_id}")


class Comment(WPBase):
    def fetch_all(self):
        """Fetches all comments."""
        return self._make_request("GET", "/wp-json/wp/v2/comments")

    def create(self, post_id, content):
        """Creates a new comment."""
        data = {"post": post_id, "content": content}
        return self._make_request("POST", "/wp-json/wp/v2/comments", data=data)

    def delete(self, comment_id):
        """Deletes a comment by ID."""
        return self._make_request("DELETE", f"/wp-json/wp/v2/comments/{comment_id}")


class Connect:
    def __init__(self, site_url, username, password):
        self.base_url = site_url.rstrip("/")
        self.auth = (username, password)
        # Authenticate
        response = requests.get(f"{self.base_url}/wp-json/wp/v2/users/me", auth=self.auth)
        if response.status_code != 200:
            logging.error("Authentication failed: %s", response.text)
            raise Exception("Authentication failed")
        # Initialize modules
        self.page = Page(self.base_url, self.auth)
        self.post = Post(self.base_url, self.auth)
        self.media = Media(self.base_url, self.auth)
        self.category = Category(self.base_url, self.auth)
        self.user = User(self.base_url, self.auth)
        self.comment = Comment(self.base_url, self.auth)
