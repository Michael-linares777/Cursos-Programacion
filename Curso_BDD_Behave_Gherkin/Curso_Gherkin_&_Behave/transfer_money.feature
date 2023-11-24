Feature: Transferir dinero

    Como cliente bancario, quiero transferir fondos entre mis cuentas, para
    que targeta de credito tenga fondos.

    Background:
        Given El cliente esta en la pagina de transferencia

    Scenario: Cliente tiene fondos suficientes
        Given Que la cuenta bancaria tiene fondos suficientes
        When El cliente quiere transferir dinero entre sus cuentas
        And El cliente da click en el boton de transferir
        Then Se ha transferido el dinero entre las cuentas correctamente

    Scenario: Cliente no tiene fondos suficientes.
        Given Que la cuenta bancaria no tiene fondos suficientes
        When El cliente quiere transferir dinero entre sus cuentas
        And El cliente da click en el boton transferir
        Then El sistema muestra mensaje "No tienes fondos suficientes para realizar la transferencia"

    Scenario Outline: Cliente tiene fondos suficientes
        Given Que la cuenta bancaria tiene fondos suficientes <cuentaDinero>
        When El cliente quiere transferir <dinero> entre sus cuentas
        And El cliente da click en el boton de transferir
        Then Se ha transferido el dinero entre las cuentas correctamente

        Examples:
            | cuentaDinero | dinero | Header 3 |
            | $ 10000      | $ 100  | Value 3  |
            | $ 100        | $ 50   | Value 3  |

