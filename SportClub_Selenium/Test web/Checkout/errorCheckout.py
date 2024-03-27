from selenium import webdriver
from Helpers.helpers import Helpers
from Selectores.xpath_landing import Xpath_landing
from Selectores.xpath_ecommerce import Xpath_ecommerce
from Helpers.mensajes import Mensajes
from Helpers.urls import URLs
import time

driver = webdriver.Chrome()
url = URLs()
validaciones = Helpers()
xpath_landing = Xpath_landing()
xpath_ecommerce = Xpath_ecommerce()
mensajes = Mensajes()

try:
    #Ingresar a la web
    driver.get(url.homeURL)
    time.sleep(5)   

    #Seleccionar plan mensual 
    xpath_landing.boton_asociate_mensual_verde(driver)

    #Navegar a la pagina de eccomerce
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    validaciones.validar_url_actual(driver, url.plan_total_mensualURL)

    #Completar form info personal
    xpath_ecommerce.campo_nombre(driver, "Juan Carlos")
    xpath_ecommerce.campo_apellido(driver, "Bodoque")
    xpath_ecommerce.campo_celular(driver,"1139393939")
    xpath_ecommerce.dropdown_tipoDocumento(driver)
    xpath_ecommerce.dni(driver)
    xpath_ecommerce.campo_documento(driver,"40404040")
    xpath_ecommerce.campo_email(driver,"test@gmail.com")

    #Completar form domicilio
    xpath_ecommerce.campo_calle(driver,"Necochea")
    xpath_ecommerce.campo_numero(driver,"1234")
    xpath_ecommerce.campo_ciudad(driver,"Ramos Mejia")
    xpath_ecommerce.dropdown_provincia(driver)
    xpath_ecommerce.provincia(driver)

    #Continuar al form 3
    xpath_ecommerce.boton_continuar_form2(driver)
    time.sleep(2)

    #Form 3 - Info de Pago
    xpath_ecommerce.campo_nomTarjeta(driver,"JuanCa Bodoque")
    xpath_ecommerce.campo_docTarjeta(driver,"40404040")
    xpath_ecommerce.campo_numTarjeta(driver,"4660577777777777")
    xpath_ecommerce.campo_mes(driver,"12")
    xpath_ecommerce.campo_anio(driver,"30")
    xpath_ecommerce.campo_cvv(driver,"1111")
    #Confirmar pago
    xpath_ecommerce.check_terminosCondiciones(driver)
    xpath_ecommerce.boton_pagar(driver)

    #Validar que el error sea el esperado
    validaciones.validar_mensaje_esperado(driver, xpath_ecommerce.snackbar_error_Ntarjeta_incorrectos, mensajes.mensaje_error_tarjeta_erronea_ecommerce, xpath_ecommerce.contenedor_mensaje_NTarjeta_incorrectos)
    
finally:
    driver.quit()
