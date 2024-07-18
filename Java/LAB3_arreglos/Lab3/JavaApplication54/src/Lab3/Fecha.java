

package Lab3;


public class Fecha {
    //Atributos
    private short dd;
    private short mm;
    private short aa;
    
    //Constructores

    public Fecha() {
    }

    public Fecha(short dd, short mm, short aa) {
        this.dd = dd;
        this.mm = mm;
        this.aa = aa;
    }
    //Getter and setters
    public short getDia() {
        return dd;
    }

    public void setDia(short dd) {
        this.dd = dd;
    }

    public short getMes() {
        return mm;
    }

    public void setMes(short mm) {
        this.mm = mm;
    }

    public short getA() {
        return aa;
    }

    public void setA(short aa) {
        this.aa = aa;
    }

    @Override
    public String toString() {
        return (dd+"-"+ mm +"-"+aa);
    }
    
}
    
    
    
    
    