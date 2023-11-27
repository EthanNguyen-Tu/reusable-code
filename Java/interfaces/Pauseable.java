package interfaces;

/**
 * Interface that characterizes something as able to pause and start.
 *
 * @author Ethan Nguyen-Tu
 * @version 1.0.0
 */
public interface Pauseable {

    /**
     * Method that halts the object.
     */
    void pause();


    /**
     * Method that starts the object
     */
    void start();

} // FIN
