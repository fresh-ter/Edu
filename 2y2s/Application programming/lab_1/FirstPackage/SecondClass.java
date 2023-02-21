package FirstPackage;

public class SecondClass {
    private int a;
    private int b;

    public int get_a() {
        return a;
    }

    public int get_b() {
        return b;
    }

    public void set_a(int val) {
        this.a = val;
    }

    public void set_b(int val) {
        this.b = val;
    }
    
    public SecondClass(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int sum() {
        return this.a + this.b;
    }
}
