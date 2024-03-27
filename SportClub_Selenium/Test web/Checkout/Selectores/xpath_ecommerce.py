class Xpath_ecommerce:   
    #Form 2 
    #Datos personales
    def campo_nombre(self, driver, keys):
        campo_nombre = driver.find_element("xpath",'//*[@id="mui-1"]')
        campo_nombre.send_keys(keys)

    def campo_apellido(self, driver, keys):
        campo_apellido = driver.find_element("xpath",'//*[@id="mui-2"]')
        campo_apellido.send_keys(keys)

    def campo_celular(self, driver, keys):
        campo_celular = driver.find_element("xpath",'//*[@id="mui-4"]')
        campo_celular.send_keys(keys)  

    def dropdown_tipoDocumento(self, driver):
        dropdown_tipoDocumento = driver.find_element('xpath','//*[@id="mui-component-select-documento_tipo"]')
        dropdown_tipoDocumento.click() 
    
    def dni(self, driver):
        dni = driver.find_element('xpath','//*[@id="menu-documento_tipo"]/div[3]/ul/li[1]')
        dni.click()

    def campo_documento(self, driver, keys):
        campo_documento = driver.find_element("xpath",'//*[@id="mui-5"]')
        campo_documento.send_keys(keys) 

    def campo_email(self, driver, keys):
        campo_email = driver.find_element("xpath",'//*[@id="form-checkout__cardholderEmail"]')
        campo_email.send_keys(keys)

    #Datos de domicilio
    
    def campo_calle(self, driver, keys):
        campo_calle = driver.find_element("xpath",'//*[@id="mui-7"]')
        campo_calle.send_keys(keys)
        
    def campo_numero(self, driver, keys):
        campo_numero = driver.find_element("xpath",'//*[@id="mui-8"]')
        campo_numero.send_keys(keys)

    def campo_ciudad(self, driver, keys):
        campo_ciudad = driver.find_element("xpath",'//*[@id="mui-10"]')
        campo_ciudad.send_keys(keys)
        
    def dropdown_provincia(self, driver):
        dropdown_provincia = driver.find_element('xpath','//*[@id="mui-component-select-domicilio.provincia"]')
        dropdown_provincia.click() 

    def provincia(self, driver):
        provincia = driver.find_element('xpath','//*[@id="menu-domicilio.provincia"]/div[3]/ul/li[2]')
        provincia.click() 
        
    def boton_continuar_form2(self, driver):
        boton_continuar_form2 = driver.find_element('xpath','//*[@id="mui-11"]')
        boton_continuar_form2.click()  
    
    #Form 3 checkout
        
    def campo_nomTarjeta(self, driver, keys):
        campo_nomTarjeta = driver.find_element("xpath",'//*[@id="form-checkout__cardholderName"]')
        campo_nomTarjeta.send_keys(keys) 

    def campo_docTarjeta(self, driver, keys):
        campo_docTarjeta = driver.find_element("xpath",'//*[@id="form-checkout__identificationNumber"]')
        campo_docTarjeta.send_keys(keys) 

    def campo_numTarjeta(self, driver, keys):
        campo_numTarjeta = driver.find_element("xpath",'//*[@id="form-checkout__cardNumber"]')
        campo_numTarjeta.send_keys(keys) 
    
    def campo_mes(self, driver, keys):
        campo_mes = driver.find_element("xpath",'//*[@id="form-checkout__cardExpirationMonth"]')
        campo_mes.send_keys(keys)

    def campo_anio(self, driver, keys):
        campo_anio = driver.find_element("xpath",'//*[@id="form-checkout__cardExpirationYear"]')
        campo_anio.send_keys(keys)

    def campo_cvv(self, driver, keys):
        campo_cvv = driver.find_element("xpath",'//*[@id="form-checkout__securityCode"]')
        campo_cvv.send_keys(keys)

    def check_terminosCondiciones(self, driver):
        check_terminosCondiciones = driver.find_element('xpath','//*[@id="form-checkout"]/div[1]/div[2]/div/span/input')
        check_terminosCondiciones.click()
        
    def boton_pagar(self, driver):
        boton_pagar = driver.find_element('xpath','//*[@id="form-checkout__submit"]/span[1]')
        boton_pagar.click()
        
    #SNACKBAR
    snackbar_error_Ntarjeta_incorrectos =('//*[@id="form-checkout"]/div[1]/div[1]/div[4]')
    contenedor_mensaje_NTarjeta_incorrectos = '//*[@id="form-checkout"]/div[1]/div[1]/div[4]/div/div[2]'
 
        
