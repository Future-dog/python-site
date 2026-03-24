from controllers.site_controller import SiteController, TestController

routes = {
    r"^/home$" : [SiteController, SiteController.index],
    r"^/about$" : [SiteController, SiteController.about],
    r"^/test$" : [TestController, TestController.test],
    r"^/test-action$" : [TestController, TestController.test_action],
    r"^/hello/(.*)$" : [SiteController, SiteController.hello],
}