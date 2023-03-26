import Vector.Vector;

public class App {
    public static void main(String[] args) {        
        Vector v = new Vector(5);
        v.set(2, 0);
        v.set(1, 1);
        v.set(3, 2);
        v.set(5, 3);
        v.set(4, 4);
        
        v.print();
        v.print_lenght();
        v.print_min();
        v.print_max();

        v.print();
        v.sort_asc();
        v.print();
    }
}

