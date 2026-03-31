from controllers.controller import Controller

class TestController(Controller):
    def test(self, request, response):
        response.text = self.view.render_html('site/test.html', {'title': 'TEST', 'h1' : 'Тестовая страница'})

    def action(self, request, response):
        response.text = self.view.render_html('site/test-action.html', {'title': 'TEST', 'h1' : 'Информация о дейтсвии'})
