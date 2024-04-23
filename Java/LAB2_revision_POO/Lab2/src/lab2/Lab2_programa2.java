
package lab2;

import java.util.Scanner;


public class Lab2_programa2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        //Creando el objeto usuario
        Usuario usuario = new Usuario();
        
        //Nombre
        System.out.println("Escriba su nombre: ");
        String nombre = scanner.next();
        usuario.setNombre(nombre);
        
        //Id
        System.out.println("Escriba su Id: ");
        long id = scanner.nextLong();
        usuario.setId(id);
        
        //Pidiendo los datos de la fecha de nacimiento
        System.out.println("FECHA DE NACIMIENTO (DÍAS-MES-AÑO)");
        System.out.println("Escriba el día de nacimiento: ");
        short dd = scanner.nextShort();
        System.out.println("Escriba el mes de nacimiento: ");
        short mm = scanner.nextShort();
        System.out.println("Escriba el año de nacimiento");
        short aa = scanner.nextShort();
        
        //Creando la fecha
        Fecha fecha_nacimiento = new Fecha(dd,mm,aa);
        usuario.setFecha_nacimiento(fecha_nacimiento);
        //Ciudad de nacimiento
        System.out.println("Escriba su ciudad de nacimiento: ");
        String ciudad_nacimiento = scanner.next();
        usuario.setCiudad_nacimiento(ciudad_nacimiento);
        
        
        //Teléfono
        System.out.println("Escriba un telefono de contacto");
        long tel = scanner.nextLong();
        usuario.setTel(tel);
        
        //Email
        System.out.println("Escriba su email");
        String email = scanner.next();
        usuario.setEmail(email);
        
        //Pidiendo los datos de la dirección
        //Creando la Dirección 
        Direccion dir = new Direccion();
        System.out.println("DIRECCION DE RESIDENCIA");
        System.out.println("Escriba la primera parte de su direccion (ej: calle,carrera,avenida, etc)");
        String calle = scanner.next();
        System.out.println("Esctiba la nomenclatura de su direccion (ej: 82a#90a-10)");
        String nomenclatura = scanner.next();
        System.out.println("Escriba el barrio donde se ubica esta direccion: ");
        String barrio = scanner.next();
        System.out.println("Escriba la ciudad donde se ubica esta direccion: ");
        String ciudad = scanner.next();
        System.out.println("Escriba el nombre del edificio donde vive (si no aplica escriba 'na')");
        String edificio = scanner.next();
        if (edificio.equalsIgnoreCase("na")){
            dir.setEdificio(null);
            }else{
            dir.setEdificio(edificio);
        }
        System.out.println("Escriba el numero de apartamento donde vive (si no aplica escriba 'na')");
        String apto = scanner.next();
        if (apto.equalsIgnoreCase("na")){
            dir.setApto(null);
            }else{
            dir.setApto(apto);
        }       
   
            
        
        //Llenando la dirección de los datos correspondientes
        dir.setCalle(calle);
        dir.setNomenclatura(nomenclatura);
        dir.setBarrio(barrio);
        dir.setCiudad(ciudad);
        
        //Estableciendo dirección en usuario
        usuario.setDireccion(dir);

        

        
        System.out.println("Resumen del usuario: ");
        System.out.println(usuario.toString());
    }

}
