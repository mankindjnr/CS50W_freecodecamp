# Foreign keys 
## ===================================================
are a fundamental concept in relational databases and are used to establish relationships between tables. In the context of Django models, a foreign key is a field that refers to the primary key of another model, creating a link between the two models.

Let's use a Twitter-like example to explain foreign keys:

Suppose we have two models: `User` and `Tweet`.

1. User Model:
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.username
```

2. Tweet Model:
```python
from django.db import models

class Tweet(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} - {self.content[:50]}"
```

In this example, we have two models: `User` and `Tweet`. The `User` model represents a Twitter user, and the `Tweet` model represents a tweet made by a user. Here's how foreign keys are used:

- In the `Tweet` model, the `author` field is a foreign key to the `User` model. This establishes a relationship between tweets and users, indicating that each tweet is authored by a user.

- The `on_delete` parameter specifies what should happen when a referenced user is deleted. In this case, `models.CASCADE` means that if a user is deleted, all their tweets will also be deleted.

Now, let's see how you might use these models:

```python
# Creating a new user
user = User(username="john_doe", bio="I love coding!")
user.save()

# Creating a new tweet
tweet = Tweet(content="Hello, Twitter!", author=user)
tweet.save()

# Retrieving tweets by a specific user
user_tweets = Tweet.objects.filter(author=user)

# Retrieving the author of a tweet
tweet = Tweet.objects.get(pk=1)  # Assuming you have a tweet with primary key 1
author = tweet.author
```

In this example, you can see that the foreign key (`author`) creates an association between the `Tweet` and `User` models. This allows you to retrieve tweets made by a specific user and also find out the author of a particular tweet.

Foreign keys are a powerful way to represent relationships between data in a database, and they are commonly used to build more complex and interconnected data structures in applications like social media platforms.