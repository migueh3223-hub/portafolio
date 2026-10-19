# --- INICIO ---
print("--- BIENVENIDO AL SISTEMA DE COMPRAS ---")

# Variables para simular los datos de entrada del diagrama
# (Aquí usamos variables y la función print)
presupuesto = float(
    input("Ingresa el dinero total que tienes disponible: ")
)
costo_esenciales = float(
    input("Ingresa el costo total de los alimentos esenciales: ")
)

# Comprar los alimentos esenciales (restamos el costo al presupuesto)
vuelto_sobrante = presupuesto - costo_esenciales

print(f"Te sobran: {vuelto_sobrante} pesos.")

# CONDICIÓN 1: ¿Vuelto (sobrante) > 10k?
if vuelto_sobrante > 10000:
  print(
      "¡Tienes más de 10k de vuelto! Puedes escoger un solo dulce de la"
      " lista."
  )

  # Supongamos el costo del dulce que escoge
  costo_dulce = float(input("¿Cuánto cuesta el dulce que escogiste?: "))

  # CONDICIÓN 2: ¿Cuesta > 5k?
  if costo_dulce > 5000:
    print("El dulce es muy caro (> 5k). Agarro uno más barato.")
    # El resto del dinero va para el ahorro
    dinero_ahorrado = (vuelto_sobrante - costo_dulce) if (vuelto_sobrante >= costo_dulce) else vuelto_sobrante
  else:
    print("¡Excelente! Lo agarro y guardo lo que queda para ahorrar.")
    dinero_ahorrado = vuelto_sobrante - costo_dulce

else:
  # NO (si el vuelto es menor o igual a 10k)
  print("No sobra suficiente para dulces. Lo guardo para ahorrar.")
  dinero_ahorrado = vuelto_sobrante

 #--- FIN / MOSTRAR RESULTADO ---

print("---------------------------------")
print(f"Dinero total ahorrado: {dinero_ahorrado} pesos")
print("--- FIN ---")