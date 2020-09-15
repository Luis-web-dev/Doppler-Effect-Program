print("bienvenido/a al programa efecto dopler")
print("....................................")
print("elija que desea hacer")
print("presione 1 para calcular frecuencia")
print("presione 2 para calcular velocidad")
opciones = int(input())
if opciones == (1):
  print("presione 1 para calcular la fuente en reposo y el observador en movimiento.")
  print("presione 2 para calcular el observador en reposo y la fuente en movimiento.")
  print("presione 3 para calcular el observador en movimiento y la fuente en movimiento.")
  print("..................................................")
  opcion2 = int(input())
  if opcion2 == (1):
    print("..................................................")
    print("presione 1 si el observador se acerca a la fuente ")
    print("presiona 2 si el observador se aleja de la fuente")
    print("..................................................")
    opcion3 = int(input())

    if opcion3 == (1):
      Velocidadsonido = (340)
      VelocidadObservador = float(input("ingrese la velocidad del observador "))
      frecuenciaEmitidaPorFuente = float(input("ingrese la frecuencia de la fuente "))
      ResultadoOpcion31 = Velocidadsonido + VelocidadObservador
      Division = ResultadoOpcion31 / Velocidadsonido
      Multiplicacion = Division * frecuenciaEmitidaPorFuente
      print("................................................")
      print(f"la frecuencia que capta el observador es {Multiplicacion}Hz")


    elif opcion3 == (2):
      Velocidadsonido = (340)
      VelocidadObservador = float(input("ingrese la velocidad del observador."))
      frecuenciaEmitidaPorFuente = float(input("ingrese la frecuencia de la fuente"))
      ResultadoOpcion31 = Velocidadsonido - VelocidadObservador
      Division = ResultadoOpcion31 / Velocidadsonido
      Multiplicacion = Division * frecuenciaEmitidaPorFuente
      print("................................................")
      print(f"la frecuencia que capta el observador es {Multiplicacion}Hz")

  elif opcion2 == (2):

    print("..................................................")
    print("presione 1 si la fuente se acerca al observador")
    print("presiona 2 si la fuente se aleja de observador")
    print("..................................................")
    opcion3 = int(input())

    if opcion3 == (1):
      Velocidadsonido = (340)
      VelocidadFuente = float(input("ingrese la velocidad de la fuente"))
      frecuenciaEmitidaPorFuente = float(input("ingrese la frecuencia de la fuente "))
      ResultadoOpcion31 = Velocidadsonido - VelocidadFuente
      Division = Velocidadsonido / ResultadoOpcion31
      Multiplicacion = Division * frecuenciaEmitidaPorFuente
      print("................................................")
      print(f"la frecuencia que capta el observador es {Multiplicacion}Hz")


    elif opcion3 == (2):
      Velocidadsonido = (340)
      VelocidadFuente = float(input("ingrese la velocidad de la fuente"))
      frecuenciaEmitidaPorFuente = float(input("ingrese la frecuencia de la fuente "))
      ResultadoOpcion31 = Velocidadsonido + VelocidadFuente
      Division = Velocidadsonido / ResultadoOpcion31
      Multiplicacion = Division * frecuenciaEmitidaPorFuente
      print("............................................................")
      print(f"la frecuencia que capta el observador es {Multiplicacion}Hz")

  elif opcion2 == (3):

    print("..................................................")
    print("presiona 1 si ambos se acercan")
    print("presiona 2 si ambos se alejan")
    print("presiona 3 si la fuente se aleja y el observador se acerca")
    print("")
    print("..................................................")

elif opciones == (2):
 VelocidadSonido = (340)
 Frecuencia = float(input("ingrese Frecuencia de onda original "))
 FrecuenciaObservada = float(input("Ingrese frecuencia observada "))
 DivisionVelocidadFuente = VelocidadSonido / Frecuencia 
 MultiplicacionVelocidadFuente = DivisionVelocidadFuente * FrecuenciaObservada
 Resta = MultiplicacionVelocidadFuente - VelocidadSonido
 print(f"La velocidad de la fuente es {Resta}m/s")
