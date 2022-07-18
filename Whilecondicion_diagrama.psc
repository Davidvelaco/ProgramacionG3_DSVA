Algoritmo sin_titulo
numero1=100
sumainter=0
contador1=0
contador2=1
suma1=0
Mientras Verdadero
	Escribir "ingrese el primer numero: ",num1
	Escribir "ingrese el segundo numero: ",num2
	Si num1=num2 Entonces
		Escribir "error los numeros son iguales"
	SiNo
	Fin Si
FinMientras
Mientras numero1 <> 0 Hacer
	Escribir "Ingrese el numero: "
	Si numero1>minimo y numero1<maximo Entonces
		sumainter<-numero1
		Si numero1<minimo o numero1>maximo Entonces
			suma1<-numero1
			contador1<-1
		SiNo
			
		fin si
		Si numero1=minimo o numero1=maximo
			contador2<-1
		SiNo
			
		FinSi
	Fin Si
Fin Mientras
Escribir "la suma de los numeros que estan dentro es:",sumainter
Escribir "el promedio de los numeros fuera del intervalo son: ",suma1/contador1
Escribir "la cantidad de los numeros ingresados iguales a los limites: ",contador2
Escribir "fin del programa"
FinAlgoritmo
