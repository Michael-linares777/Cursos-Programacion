@MVP (Producto Mínimo Viable) @Android @Web @iOS  // Ejemplo Tags @ / Fines didacticos / Esto no va aqui en este ejemplo.
Feature: Feature name  /  Login

    Feature Description  /  Como cliente, yo quiero logearme con email y password,
    para asi yo poder usar la aplicacion.

    Rule: Rule name  / Mayor de 18 años  // Fines didacticos / Esto no va aqui en este ejemplo

        # Background: Cuando un accion Given se repite en mas de un Scenario
        Background:
            Given Background name  / Que estoy en la pagina de login

        @PantallasGrandes // Ejemplo Tags @ / Fines didacticos / Esto no va aqui en este ejemplo.
        Scenario: Scenario name  / Loguearme cuando mis credenciales son validas
            Given Que estoy en la pagina de login
            When Yo ingreso en el campo de email el valor "Admin@admin.com"
            And yo ingreso en el campo de password la contraseña "1234"
            And Damos clic en el boton de login
            Then Estoy en la home de la aplicacion
            And El titulo de esta pagina es "Global Position"
            But El boton de login no esta presente

                """
                EJ: Doc Strings
                Informaccion adicional:
                - Nombre: Michael Linares
                - Nro cuenta
                - Y mas informaion que quieras
                """

        Scenario:  Scenario name  / Loguearme cuando mis credenciales no son validas
            Given Que estoy en la pagina de login
            When Yo ingreso en el campo de email el valor "AdminiNoValido@admin.com"
            And Yo ingreso en el campo de password la contraseña "incorrect"
            And Damos click en el boton de login
            Then El sistema muestra mensaje de error no puedes ingresar, email y password incorrectos

        Scenario Outline: Scenario Outline name  / Loguearme cuando mis credenciales son validas
            Given Que estoy en la pagina de login.
            When Yo ingreso en el campo de email el valor <email>
            And yo ingreso en el campo de password la contraseña <password>
            And Damos clic en el boton de login
            Then Estoy en la home de la aplicacion
            And El titulo de esta pagina es "Global Position"
            But El boton de login no esta presente

            Examples:
                | email             | password | Header 3 |
                | admin@company.com | 1234     | Value 3  |
                | user@company.com  | ASDF     | Value 3  |