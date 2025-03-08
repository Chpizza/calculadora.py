# definicio de la calse de la  calculadora
class Calculadora:
    # metodo suma de dos numeron
    def suma(self, a, b):
        return a + b   
    def resta(self, a, b):
        return a - b
    def multiplicacion(self, a, b):
        return a * b
    def division(self, a, b):
        if b == 0:
            return "No se puede dividir por cero"
        else:
            return a / b