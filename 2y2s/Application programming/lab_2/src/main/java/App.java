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
        v.mul(2);
        v.print();

        Vector v2 = new Vector(5);
        for(int c=0;c<5;c++) {
            v2.set(1,c);
        }
        v2.print();

        v.sum(v2);
        v.print();

        Vector v3 = new Vector(5);
        for(int c=0;c<5;c++) {
            v3.set(2,c);
        }
        v3.print();

        v.print_mul_scalar(v3);

        v.print();
        
        v.print_norm();
    }
}

