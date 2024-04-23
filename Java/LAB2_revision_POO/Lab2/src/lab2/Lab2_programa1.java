
package lab2;


public class Lab2_programa1 {


    public static void main(String[] args) {
        
        //Creando el objeto tipo fecha
        Fecha fecha = new Fecha((short)23,(short)03,(short)2002);
        System.out.println(fecha.toString());
        
        
        //Creando el objeto tipo direccion
        Direccion dir = new Direccion();
        dir.setCalle("calle");
        dir.setNomenclatura("82a#90a-10");
        dir.setBarrio("Robledo");
        dir.setCiudad("Medellin");
        
        System.out.println(dir.toString());
        
        //Creando el objeto tipo usuario
        Usuario usuario = new Usuario("Byron",1000192293L,fecha,"Medellin",3148839303L,"byronarenilla7@gmail.com",dir);
        System.out.println(usuario.toString());
    }

}
