class ChoqueInelastico:

    def __init__(self, x: list, y: list, z: list, w: list) -> None:
        self.x = x #Masa 1 (g)
        self.y = y #Masa 2 (g)
        self.z = z #V inicial (m/s)
        self.w = w #V final (m/s)

    def masa_a_kg(self, parameter): #Pasar de g a kg
        for i in range(len(parameter)):
            gramos = float(parameter[i])
            kg = "{:.5f}".format(gramos/1000) #Lo pasamos a kg 5 decimales precisión
            parameter[i] = kg


    def momentum_inicial(self): #Momentum inicial
        lista_1 = []
        for i in range(len(self.x)):
            kg = float(self.x[i])
            vel = float(self.z[i])
            momentum = "{:.5f}".format(float(kg*vel))

            lista_1.append(momentum)

        return lista_1

    def momentum_final(self): #Momentum final
        lista_2 = []
        for i in range(len(self.w)):
            masa_1 = float(self.x[i])
            masa_2 = float(self.y[i])
            vf = float(self.w[i])
            moment =  "{:.5f}".format(vf*(masa_1 + masa_2))
            lista_2.append(moment)

        return lista_2

    def ec_inicial(self): #Energía cinética inicial
        lista_3 = []
        for i in range(len(self.z)):
            masa = float(self.x[i])
            vel = float(self.z[i])
            energia = "{:.5f}".format((1/2)*(masa)*((vel)**(2)))
            lista_3.append(energia)

        return lista_3

    def ec_final(self):
        lista_4 = []
        for i in range(len(self.x)):
            masa_1 = float(self.x[i])
            masa_2 = float(self.y[i])
            vf = float(self.w[i])
            energia = "{:.5f}".format((1/2)*(masa_1+masa_2)*((vf)**(2)))
            lista_4.append(energia)

        return lista_4

class ChoqueElastico:

    def __init__(self, x: list, y: list, z: list, w: list, v: list) -> None:
        self.x = x #Masas 1(g)
        self.y = y #Masas 2(g)
        self.z = z #V1 inicial (m/s)
        self.w = w #V1 final (m/s)
        self.v = v #V2 final (m/s)

    def masa_a_kg(self, parameter): #Pasar de g a kg
        for i in range(len(parameter)):
            gramos = float(parameter[i])
            kg = "{:.5f}".format(gramos/1000) #Lo pasamos a kg 5 decimales precisión
            parameter[i] = kg

    def momentum_inicial(self):
        lista_1 = []
        for i in range(len(self.x)):
            kg = float(self.x[i])
            vel = float(self.z[i])
            momentum = "{:.5f}".format(float(kg*vel))
            lista_1.append(momentum)

        return lista_1

    def momentum_final(self):
        lista_2 = []
        for i in range(len(self.x)):
            masa_1 = float(self.x[i])
            masa_2 = float(self.y[i])
            v1 = float(self.w[i])
            v2 = float(self.v[i])
            momentum = "{:.5f}".format(masa_1*v1 +masa_2*v2)
            lista_2.append(momentum)

        return lista_2

    def ec_inicial(self):
        lista_3 = []
        for i in range(len(self.x)):
            masa = float(self.x[i])
            vel = float(self.z[i])
            energia = "{:.5f}".format((1/2)*(masa)*((vel)**(2)))
            lista_3.append(energia)

        return lista_3

    def ec_final(self):
        lista_4 = []
        for i in range(len(self.x)):
            masa_1 = float(self.x[i])
            masa_2 = float(self.y[i])
            v1_final = float(self.w[i])
            v2_final = float(self.v[i])
            ec_1 = (1/2)*(masa_1)*((v1_final)**(2))
            ec_2 = (1/2)*(masa_2)*((v2_final)**(2))
            energia_final = "{:.5f}".format(ec_1 + ec_2)
            lista_4.append(energia_final)

        return lista_4
