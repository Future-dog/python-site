from controllers.site_controller import SiteController, TestController

routes = {
    "/home" : [SiteController, SiteController.index],
    "/about" : [SiteController, SiteController.about],
    "/test" : [TestController, TestController.test],
    "/test-action" : [TestController, TestController.test_action],
    
}