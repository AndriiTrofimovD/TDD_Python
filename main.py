class TestCase:

    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        try:
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result

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

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    # Arrange -> Act -> Assert

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()


class TestResult:

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()
#