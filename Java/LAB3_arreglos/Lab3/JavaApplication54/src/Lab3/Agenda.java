
package Lab3;


public class Agenda {
    //Atributos
    private Usuario[] registro;
    private int no_reg;
    
    //Constructores
    public Agenda(int capacity){
        this.registro = new Usuario[capacity];
        this.no_reg = 0;
    }
    
    //Métodos
    
    public Boolean agregar(Usuario u){
        return true;
    }

}
