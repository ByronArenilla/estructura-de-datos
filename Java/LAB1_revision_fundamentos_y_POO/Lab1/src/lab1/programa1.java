package Lab1;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class programa1 {
    public static void main(String[] args) {
        Scanner scaner = new Scanner (System.in);
        List<Integer> listaNum = new ArrayList<>(); //creando la lista
        System.out.println("Ingrese la cantidad de numeros a ingresar: ");
        int N = scaner.nextInt();
        
        for (int i = 0; i<N; i++){
            System.out.println("Ingrese el numero: ");
            int num = scaner.nextInt();
            listaNum.add(num);
            
        }
        
        //creando los valores máximos y mínimos
        int numMax = Integer.MIN_VALUE;
        int numMin = Integer.MAX_VALUE;
        int suma = 0;

        for (int num : listaNum) {
            if (num > numMax) {
                numMax = num;
            }
            if (num < numMin) {
                numMin = num;
            }
            suma += num;
        }

        double prom = (double) suma / N;

        System.out.println("El valor máximo de la lista de números que ingresó es " + numMax + ". El valor mínimo es " +            numMin + ". La suma de los números es " + suma + " y el valor promedio es " + prom);
    }
}
        
    

