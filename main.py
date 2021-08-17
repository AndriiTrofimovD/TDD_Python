
class TestCase:

    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def setUp(self):
        pass

    def tearDown(self):
        pass


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1
        self.log += "testMethod "

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    # Arrange -> Act -> Assert

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert "setUp testMethod tearDown " == self.test.log


TestCaseTest("testTemplateMethod").run()
