from django.shortcuts import render
from .models import Content
from django.db import connection
from datetime import datetime



def dictfetchall(cursor):
    # Returns all rows from a cursor as a dict '''
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT *
                        FROM Content
                        WHERE Release_Date >= '2021-01-01'
                        ORDER BY Release_Date DESC;
                        """)
        sql_res = dictfetchall(cursor)
        cursor.execute("""
                        SELECT A.title
                        FROM ActedIn A
                        WHERE A.Actor = 'Adam Sandler'
                        """)
        sql_res2 = dictfetchall(cursor)

    return render(request, 'index.html', {'sql_res': sql_res, 'sql_res2': sql_res2})


def add_content(request):
    if request.method == 'POST' and request.POST:
        new_title = request.POST["title"]
        new_language = request.POST["language"]
        today = datetime.today().strftime('%Y-%m-%d')
        new_content = Content(title=new_title,
                              language=new_language,
                              release_date=today)
        new_content.save()
    return render(request, 'add_content.html')

def salary_checker(request):
    flag = 0
    if request.method == 'POST' and request.POST:
        flag = 1
        new_salary = int(request.POST["salary"])
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT title
                        FROM ActedIn
                        WHERE Salary >= %s
                        GROUP BY title
                        HAVING COUNT(title) > 0
                        """, [new_salary])
            if cursor.description is not None:
                sql_res3 = dictfetchall(cursor)
        return render(request, 'salary_checker.html', {'sql_res3': sql_res3,
                                                                          'flag': flag})
    else:
        return render(request, 'salary_checker.html', {'flag': flag})


