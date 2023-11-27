package interfaces;

/**
 * Defines the Locatable2D characteristic. Objects that are Locatable2D have both an
 * x-coordinate and a y-coordinate that is retrievable.
 *
 * @author Ethan Nguyen-Tu
 * @version 1.0.0
 */
public interface Locatable2D {

    /**
     * Returns the x-coordinate of an object.
     * @return int of the object's x-coordinate
     */
    int getX();


    /**
     * Returns the y-coordinate of an object.
     * @return int of the object's y-coordinate
     */
    int getY();

} // FIN
