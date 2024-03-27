import time

class Helpers:
    def validar_url_actual(self, driver, url_esperada):
        url_actual = driver.current_url
    # return 'TEST OK: Las urls son iguales: ', url_actual == url_esperada
        assert url_esperada == url_actual, f"La URL actual '{url_actual}' no coincide con la esperada '{url_esperada}'"
        print("TEST OK: La URL actual coincide con la esperada")

    def validar_mensaje_esperado(self, driver, xpath_error, mensaje_esperado, xpath_text):
        try:
            time.sleep(10)
            snackbar_error = driver.find_element('xpath',xpath_error)
            if snackbar_error.is_displayed():
                print("TEST OK: Snackbar de error encontrado.")
                snackbar_text = driver.find_element('xpath',xpath_text)
                if snackbar_text.is_displayed():
                    print("TEST OK: Contenedor de texto del Snackbar de error encontrado.")
                    mensaje_actual = snackbar_text.text

                    if mensaje_esperado in mensaje_actual:
                        print("TEST OK: El mensaje de error esperado está presente en el Snackbar.")
                        return True
                    else:
                        print("TEST FAIL: El mensaje de error esperado no está presente en el Snackbar.")
                        return False
                else:
                    print("TEST FAIL: Contenedor de texto del Snackbar de error no encontrado.")
                    return False
            else:
                print("TEST FAIL: Snackbar de error no encontrado.")
                return False

        except Exception as e:
            print("TEST FAIL: Ocurrió un error al buscar el Snackbar de error:", e)
            return False

