score = int(input("Score: "))
#if score >= 90 and score <= 100:
# En Python se puede hacer, algo que en C o en C++ no se puede hacer y es;
# if <= 90 score <= 100:
#    print("Grade: A")
#elif 80 <= score < 90:
#    print("Grade: B")
#elif  70 <= score < 80:
#    print("Grade: C")
#elif 60 <= score < 70:
#    print("Grade: D")
#else:
#    print("Grade : F")
# Para simplificar el código tambien puedo cambiar el rango a:
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade : F")
# Si se usasen sólamente IF en cada pregunta, al colocar el valor de SCORE, todas las notas serían= ABCDF, porque todas las condicionales son ciertas
