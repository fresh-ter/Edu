import FirstPackage.*;

class FirstClass {
    public static void main(String[] s) {
        // System.out.println("Hello world!!!");

        // for (int i=0; i<s.length; i++) {
        //     System.out.println(s[i]);
        // }

        var o = new SecondClass(1,2);
        System.out.println(o.sum());

        int i,j;
        for (i=0; i<=8; i++) {
            for (j=0; j<=8; j++) {
                o.set_a(i);
                o.set_b(j);

                System.out.print(o.sum());
                System.out.print("\t");
            }

            System.out.println();
        }
    }
}
