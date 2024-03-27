from selenium.webdriver.common.action_chains import ActionChains

class Xpath_landing:   

    def boton_asociate_mensual_verde(self, driver):
        boton_asociate_mensual_verde = driver.find_element("xpath",'//*[@id="root"]/div[4]/div[1]/div[2]/div/div[1]/div/a/button')
        actions = ActionChains(driver)
        actions.move_to_element(boton_asociate_mensual_verde).click().perform()

