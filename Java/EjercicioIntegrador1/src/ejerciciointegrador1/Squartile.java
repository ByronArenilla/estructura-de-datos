
package ejerciciointegrador1;


public class Squartile extends Pokemon implements IAgua{

    public Squartile() {
    }

    
    @Override
    protected void atacarPlacaje() {
        System.out.println("Hola, soy Squartile y este es mi ataque placaje");
    }

    @Override
    protected void atacarAraniazo() {
       System.out.println("Hola, soy Squartile y este es mi ataque arañazo");
    }

    @Override
    protected void atacarMordisco() {
       System.out.println("Hola, soy Squartile y este es mi ataque mordisco");
    }

    @Override
    public void atacarHidrobomba() {
        System.out.println("Hola, soy Squartile  y este es mi ataque hidrobomba");
    }

    @Override
    public void atacarBurbuja() {
        System.out.println("Hola, soy Squartile  y este es mi ataque atacar burbuja");
    }

    @Override
    public void atacarPistolaAgua() {
        System.out.println("Hola, soy Squartile  y este es mi ataque atacar pistola agua");
    }

}
