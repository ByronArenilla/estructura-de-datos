
package lab1;

import java.io.BufferedReader;
import java.io.FileReader;


public class programa2 {


    public static void main(String[] args) {
        // Ruta del archivo a leer
        String rutaArchivo = "C:/Users/ASUS/Documents/Universidad/Semestre 2024-1/estructura-de-datos/Java/LAB1_revision_fundamentos_y_POO/test_pr2.txt";
        
        FileReader archivo;
        BufferedReader lector;
        
        try{
            //Crear archivo para leerlo
            archivo = new FileReader(rutaArchivo);
            //Leer el BufferedReader para leer las lineas de texto de manera eficiente
            lector = new BufferedReader(archivo);
            
            //Creando el contador
            int contador = 0;
            //Leer las lineas de texto
            String linea;
            while ((linea = lector.readLine()) != null){
                //Dividir la linea en palabras
                String[] palabras = linea.split("\\s+");
                
                //Iterar sobre las palabras de la linea
                for (String palabra : palabras){
                    //comparar con la palabra "en"
                    if (palabra.equals("el")){
                        contador++;
                    }
                }
            }
            
            //cerrar el BufferedReader y el FileReader
            archivo.close();
            lector.close();
            
            //Imprimir el resultado
            System.out.println("La palabra 'el' se repite "+ contador + " veces en el texto");
            
            
        } catch (Exception e){
            System.out.println("Error; "+ e.getMessage());
        }
    }

}
