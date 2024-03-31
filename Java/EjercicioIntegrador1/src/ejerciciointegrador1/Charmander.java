
package ejerciciointegrador1;


public class Charmander extends Pokemon implements IFuego {

    public Charmander() {
    }

    
    
    @Override
    protected void atacarPlacaje() {
       System.out.println("Hola, soy Charmander y este es mi ataque arañazo");
    }

    @Override
    protected void atacarAraniazo() {
        System.out.println("Hola, soy Charmander y este es mi ataque arañazo");
    }

    @Override
    protected void atacarMordisco() {
       System.out.println("Hola, soy Charmander y este es mi ataque mordizco");
    }

    @Override
    public void atacarPunioFuego() {
        System.out.println("Hola, soy Charmander y este es mi ataque puño fuego");
    }

    @Override
    public void atacarLanzaLlamas() {
        System.out.println("Hola, soy Charmander y este es mi ataque lanza llamas");
    }

    @Override
    public void atacarAscuas() {
        System.out.println("Hola, soy Charmander y este es mi ataque atacar asucas");
    }

}
