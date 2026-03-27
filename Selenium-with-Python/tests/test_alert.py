class TestAlertAPI:
    def test_alert_accept(self, driver):
        driver.get("https://www.google.com/")
        driver.execute_script("window.alert('This is an alert');")
        alert = driver.switch_to.alert
        assert alert.text == "This is an alert"
        alert.accept()
