# A Server Side Rendered Chat-Room Web-App based on Django

test user credentials:

```code
username: rajat
password: rajat311201@
```

```code
username: vishal
password: rajat311201@
```

-   HTML, CSS used for frontend
-   Django used in backend
-   Default database used - sqlite3
-   Based on MVT (Model View Template) Architecture

## Description

> -   Has functionality of user login, signup and supports all CRUD operations
> -   Logged in user can create, update and delete rooms, create a new topic for rooms, also delete their messages
> -   When a user messages in a room then it automatically becomes participant of that room
> -   Home page shows list of all topics, recent activities
> -   User can click on a particular topic to see the rooms of only that topic.

<hr>

> -   The App contains two sub apps namely <strong>base</strong> and <strong>chatBud</strong>
> -   chatBud is the main app which includes all configurations
> -   base app contains all html templates, urls, models, views and forms

<hr>

## Modules used in views.py

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Room, Topic, Message
from .forms import RoomForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
```

rajatverma
rajat@test.com
rajat@test
