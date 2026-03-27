class TestBrowserDimensions:
    def test_set_custom_window_size(self, driver):
        driver.get("https://www.wikipedia.org/")
        driver.set_window_size(1024, 768)
        size = driver.get_window_size()
        assert size["width"] == 1024
        assert size["height"] == 768

    def test_maximize_window(self, driver):
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
        size = driver.get_window_size()
        assert size["width"] > 0
        assert size["height"] > 0

    def test_resize_to_multiple_dimensions(self, driver):
        driver.get("https://www.wikipedia.org/")
        driver.set_window_size(1280, 720)
        size = driver.get_window_size()
        assert size["width"] == 1280
        assert size["height"] == 720
