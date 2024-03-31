
package ejerciciointegrador1;


public class Pikachu extends Pokemon implements IElectrico {

    public Pikachu() {
    }
    
    
    @Override
    protected void atacarPlacaje() {
        System.out.println("Hola, soy Pikachu y este es mi ataque placaje");
    }

    @Override
    protected void atacarAraniazo() {
        System.out.println("Hola, soy Pikachu y este es mi ataque arañazo");
    }

    @Override
    protected void atacarMordisco() {
       System.out.println("Hola, soy Pikachu y este es mi ataque mordisco");
    }

    @Override
    public void atacarImpactrueno() {
        System.out.println("Hola, soy Pikachu y este es mi ataque impactar trueno");
    }

    @Override
    public void atacarPunioTrueno() {
        System.out.println("Hola, soy Pikachu y este es mi ataque puño trueno");
    }

}
