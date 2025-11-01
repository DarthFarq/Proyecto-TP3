class Envio:
    def __init__(self, cod, dp, tip, fp):
        self.codigo = cod
        self.direccion = dp
        self.tipo = tip
        self.pago = fp

    def __str__(self):
        cad = 'Código postal: {:<10} | Direccion: {:<20} | Pais: {:<12} | Tipo de envio: {:<2} | Forma de pago: {:<3}'
        cad = cad.format(self.codigo, self.direccion, self.country(), self.tipo, self.pago)
        return cad

    def country(self):
        cp = self.codigo
        n = len(cp)
        if n < 4 or n > 9:
            return 'Otro'

        if n == 8:
            if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'

        if n == 9:
            if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'

        if cp.isdigit():
            if n == 4:
                return 'Bolivia'

            if n == 7:
                return 'Chile'

            if n == 6:
                return 'Paraguay'

            if n == 5:
                return 'Uruguay'

        return 'Otro'
