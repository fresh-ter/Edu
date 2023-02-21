package FirstPackage;

class SecondClass {
    private int a;
    private int b;

    int get_a() {
        return a;
    }

    int get_b() {
        return b;
    }

    void set_a(int val) {
        this.a = val;
    }

    void set_b(int val) {
        this.b = val;
    }
    
    SecondClass(int a, int b) {
        this.a = a;
        this.b = b;
    }

    int sum() {
        return this.a + this.b;
    }
}
