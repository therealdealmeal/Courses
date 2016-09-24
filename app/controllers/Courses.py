"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        course = self.models['Course'].get_all_courses()
        return self.load_view('index.html', all_courses=course)


    def show(self, id):
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('destroy.html', all_courses=course)


    def add(self):
        course_details = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(course_details)
        return redirect('/')


    def goback(self):
        return redirect('/')


    def destroy(self, course_id):
        self.models['Course'].delete_course(course_id)
        return redirect('/')
