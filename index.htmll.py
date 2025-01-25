<html>
<head>
    <title>Todo List</title>
</head>
<body>
    <h1>Todo List</h1>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Add new todo">
        <input type="submit" value="Add">
    </form>
    <ul>
    {% for todo in todos %}
        <li>
            {{ todo.title }}
            {% if todo.completed %}
                <span style="text-decoration: line-through;">(Completed)</span>
            {% else %}
                <a href="/update/{{ todo.id }}">Mark as completed</a>
            {% endif %}
            <a href="/delete/{{ todo.id }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
