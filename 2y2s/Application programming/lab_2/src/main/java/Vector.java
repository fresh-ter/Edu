package Vector;

public class Vector {
    // int len = 0;
    int[] vector;
    
    public Vector(int len) {
        System.out.println("Vector");

        this.vector = new int[len];
    }

    public void print() {
        System.out.println();
        System.out.println("vvvvvv Vector vvvvvv");
        for(int x: this.vector) {
            System.out.println(x);
        }
        System.out.println("^^^^^^^^^^^^^^^^^^^^");
        System.out.println();
    }

    public void set(int number, int index) {
        this.vector[index] = number;
    }

    public int get(int index) {
        return this.vector[index];
    }

    public int get_length() {
        return this.vector.length;
    }

    public void print_lenght() {
        System.out.println("Length: " + this.get_length());
    }

    public int get_min() {
        int x_min = this.get(0);
        for(int x: this.vector) {
            if(x < x_min) {
                x_min = x;
            }
        }

        return x_min;
    }

    public void print_min() {
        System.out.println("Min: " + this.get_min());
    }

    public int get_max() {
        int x_max = this.get(0);
        for(int x: this.vector) {
            if(x > x_max) {
                x_max = x;
            }
        }

        return x_max;
    }

    public void print_max() {
        System.out.println("Max: " + this.get_max());
    }

    void swap(int id1, int id2) {
        int m = this.vector[id1];
        this.vector[id1] = this.vector[id2];
        this.vector[id2] = m;
    }

    public void sort_asc() {
        boolean e;
        
        while(true) {
            e = true;
        
            for(int i=0; i<this.get_length()-1; i++) {
                if(this.vector[i] > this.vector[i+1]) {
                    this.swap(i, i+1);
                    e = false;
                }
            }

            if(e) {
            break;
            }
        }
    }
}
