

package Lab3;


public class Usuario {
    //Atributos
    private String nombre;
    private long id;
    private Fecha fecha_nacimiento;
    private String ciudad_nacimiento;
    private long tel;
    private String email;
    private Direccion dir;
    
    //Constructores
    public Usuario(){
    }
    
    public Usuario(String nombre, long id, Fecha fecha_nacimiento, String ciudad_nacimiento, long tel, String email, Direccion dir){
        this.nombre = nombre;
        this.id = id;
        this.fecha_nacimiento = fecha_nacimiento;
        this.ciudad_nacimiento = ciudad_nacimiento;
        this.tel = tel;
        this.email = email;
        this.dir = dir;
        
    }
    
    //Getters and Setters
    public String getNombre(){
        return this.nombre;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public long getId(){
        return this.id;
    }
    
    public void setId(long id){
        this.id = id;
    }
    
    public Fecha getFecha_nacimiento(){
        return this.fecha_nacimiento;
    }
    
    public void setFecha_nacimiento(Fecha fecha_nacimiento){
        this.fecha_nacimiento = fecha_nacimiento;
    }

    public String getCiudad_nacimiento() {
        return ciudad_nacimiento;
    }

    public void setCiudad_nacimiento(String ciudad_nacimiento) {
        this.ciudad_nacimiento = ciudad_nacimiento;
    }
    
    
    public long getTel(){
        return this.tel;
    }
    
    public void setTel(long tel){
        this.tel = tel;
    }
    
    public String getEmail(){
        return this.email;
    }
    
    public void setEmail(String email){
        this.email = email;
    }
    
    public Direccion getDireccion(){
        return this.dir;
    }
    
    public void setDireccion(Direccion dir){
        this.dir = dir;
    }

    @Override
    public String toString() {
        return "Usuario: " + nombre + ", id :" + id + ", fecha de nacimiento: " + fecha_nacimiento + ", ciudad de nacimiento: " + ciudad_nacimiento + ", tel: " + tel + ", email: " + email + ", direccion: " + dir ;
    }
   

}

