
package lab2;


public class Direccion {
    //Atributos
    private String calle;
    private String nomenclatura;
    private String barrio;
    private String ciudad;
    private String edificio;
    private String apto;
    
    //Constructores
    public Direccion(){
    }
    
    public Direccion(String calle,String nomenclatura,String barrio, String ciudad, String edificio, String apto){
        this.calle = calle;
        this.nomenclatura = nomenclatura;
        this.barrio = barrio;
        this.ciudad = ciudad;
        this.edificio = edificio;
        this.apto = apto;

    }
    
    //Getters and setters

    public String getCalle() {
        return calle;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public String getNomenclatura() {
        return nomenclatura;
    }

    public void setNomenclatura(String nomenclatura) {
        this.nomenclatura = nomenclatura;
    }
    
    public String getBarrio(){
        return this.barrio;
    }
    
    public void setBarrio(String barrio){
        this.barrio = barrio;
    }

    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }

    public String getEdificio() {
        return edificio;
    }

    public void setEdificio(String edificio) {
        this.edificio = edificio;
    }

    public String getApto() {
        return apto;
    }

    public void setApto(String apto) {
        this.apto = apto;
    }
    
    //Método toString

    @Override
    public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(calle);
    sb.append(nomenclatura);
    sb.append(" barrio: ").append(barrio);
    sb.append(", Ciudad: ").append(ciudad);
    
    // Verifica si hay un edificio y un apartamento
    if (edificio != null && !edificio.isEmpty()) {
        sb.append(", edificio : ").append(edificio);
    }
    if (apto != null && !apto.isEmpty()) {
        sb.append(" apto: ").append(apto);
    }
    return sb.toString();
}
    

}
