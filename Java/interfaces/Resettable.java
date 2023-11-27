package interfaces;

/**
 * Interface that characterizes something as able to be reset.
 *
 * @author Ethan Nguyen-Tu
 * @version 1.0.0
 */
public interface Resettable {

    /**
     * Method that resets all of the parameters of the object.
     * @return boolean true if the reset is successful, else false
     */
    boolean reset();

} // FIN
