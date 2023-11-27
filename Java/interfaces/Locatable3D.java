package interfaces;

/**
 * Defines the Locatable3D characteristic. Objects that are Locatable3D have an
 * x-coordinate, a y-coordinate, and a z-coordinate that is retrievable.
 *
 * @author Ethan Nguyen-Tu
 * @version 1.0.0
 */
public interface Locatable3D { // Can add "extends Locatable2D" and remove getX() and getY()

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


    /**
     * Returns the z-coordinate of an object.
     * @return int of the object's z-coordinate
     */
    int getZ();

} // FIN
