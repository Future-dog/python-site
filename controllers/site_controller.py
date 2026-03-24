from views.view import View

class SiteController:
    def __init__(self):
        self.layout = "default"
        self.view = View(self.layout)

    def index(self, request, response):
        response.text = self.view.render_html('site/index.html', {'title': 'MVC framework', 'h1' : 'Главная страница'})
    
    def about(self, request, response):
        response.text = self.view.render_html('site/about.html', {'title': 'About', 'h1' : 'Онанас'})

    def hello(self, request, response, user_name):
        response.text = self.view.render_html('site/hello.html', {'title': 'Приветствие', 'h1' : 'Привет', 'user' : user_name})
        
# ----------------------------------

class TestController:
    def __init__(self):
        self.layout = "default"
        self.view = View(self.layout)

    def test(self, request, response):
        response.text = self.view.render_html('site/test.html', {'title': 'TEST', 'h1' : 'Тестовая страница'})

    def test_action(self, request, response):
        response.text = self.view.render_html('site/test-action.html', {'title': 'TEST', 'h1' : 'Информация о дейтсвии'})

    
