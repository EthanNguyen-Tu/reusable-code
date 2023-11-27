package interfaces;

/**
 * Interface that characterizes something as able to be added to the clock.
 * In other words, should be used for anything that needs to be periodically assessed.
 *
 * @author Ethan Nguyen-Tu
 * @version 1.0.0
 */
public interface Tickable {

    /**
     * Method that is called every tick of the clock.
     */
    void onTick();

} // FIN
