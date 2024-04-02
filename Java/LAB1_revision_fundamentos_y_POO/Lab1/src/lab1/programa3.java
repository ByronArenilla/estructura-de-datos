
package lab1;

import java.util.Scanner;


public class programa3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[][] usuariosYContraseñas = {
            {"Juan1223","J12an*"},
            {"Maira2345","M23a*"},
            {"Pablo1459","P14a*"},
            {"Ana3456","A34a*"}
        } ;
        
        //Contador para el número de intentos fallidos
        int intentosFallidos = 0;
        while (intentosFallidos < 3){
            //Solicitar al usuiario que ingrese el usuario y contraseña
            System.out.println("Ingrese el nombre de usuario: ");
            String nombre = scanner.next();
            
            System.out.println("Ingrese la contraseña: ");
            String contraseña = scanner.next();
            
            //Verificar el nombre se usuario
            boolean accesoPermitido = false;
            for (String[] usuarioYContraseña : usuariosYContraseñas){
                if (usuarioYContraseña[0].equals(nombre) && usuarioYContraseña[1].equals(contraseña)){
                    accesoPermitido = true;
                    break;
                }
                 }
            //Mostrar el mensaje correspondiente
            if (accesoPermitido){
                System.out.println("Acceso permitido");
                break;
            }else{
                System.out.println("Datos Incorrectos");
                intentosFallidos ++;
            }if (intentosFallidos == 3){
                System.out.println("Lo siento, su acceso no es permitido");
            }
        }
    }
    
 }
        
