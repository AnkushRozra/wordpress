# Wordpress Python Library

The `wordpress` Python library provides a simple interface to interact with the WordPress REST API. It allows you to manage various aspects of your WordPress site, including pages, posts, categories, media, users, and comments.

## Download stats
[![Downloads](https://static.pepy.tech/badge/Wordpress)](https://pepy.tech/project/Wordpress)
## Features

- Fetch, create, update, and delete `pages`
- Fetch, create, update, and delete `posts`
- Fetch, create, update, and delete `categories`
- Upload and manage `media`
- Fetch and manage `users`
- Fetch and manage `comments`

## Installation

You can install the library using pip:

```bash
pip install wordpress
```

## Usage
Importing the Library
```python
import wordpress
```

## Connecting to WordPress
To use the library, create an instance of the wordpress.Connect class by providing the base URL of your WordPress site and authentication details (username and password).

```python
site_url = "https://yourwordpresssite.com"
username = "yourusername"
password = "your_application_password" #read documentation https://wordpress.com/support/security/two-step-authentication/application-specific-passwords/
wp = wordpress.Connect(site_url, username, password)
```

## Pages
### Fetch All Pages
```python
wp.page.fetch_all_pages()
```
### Create a New Page
```python
wp.page.create_page(title="About Us", content="This is the About Us page.")
```
### Fetch a Specific Page
```python
wp.page.fetch_page(page_id=123)
```
### Delete a Page
```python
wp.page.delete_page(page_id=123)
```
## Posts
### Fetch All Posts
```python
wp.post.fetch_all_posts()
```
### Create a New Post
```python
wp.post.create_post(title="New Blog Post", content="This is a new blog post.")
```
### Fetch a Specific Post
```python
wp.post.fetch_post(post_id=123)
```
### Delete a Post
```python
wp.post.delete_post(post_id=123)
```
### Categories
### Fetch All Categories
```python
wp.category.fetch_all_categories()
```
### Create a New Category
```python
wp.category.create_category(name="New Category")
```
### Fetch a Specific Category
```python
wp.category.fetch_category(category_id=123)
```
### Delete a Category
```python
wp.category.delete_category(category_id=123)
```
## Media
### Upload Media
```python
wp.media.upload_media(file_path="path/to/your/image.jpg")
```
### Fetch All Media
```python
wp.media.fetch_all_media()
```
### Fetch a Specific Media Item
```python
wp.media.fetch_media(media_id=123)
```
### Delete Media
```python
wp.media.delete_media(media_id=123)
```
## Users
### Fetch All Users
```python
wp.user.fetch_all_users()
```
### Fetch a Specific User
```python
wp.user.fetch_user(user_id=123)
```
## Comments
### Fetch All Comments
```python
wp.comment.fetch_all_comments()
```
### Fetch a Specific Comment
```python
wp.comment.fetch_comment(comment_id=123)
```
