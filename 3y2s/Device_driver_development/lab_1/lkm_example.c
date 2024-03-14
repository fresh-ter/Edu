#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("MIT");
MODULE_AUTHOR("Student");
MODULE_DESCRIPTION("A simple example Linux module.");
MODULE_VERSION("1.0");

static int __init lkm_example_init(void) {
    for(int c=0; c < 18; c++) {
        printk(KERN_INFO "%d - Terminator\n", c);
    }
    return 0;
}

long factorial(const int n)
{
    long f = 1;
    for (int i=1; i<=n; ++i)
        f *= i;
    return f;
}

static void __exit lkm_example_exit(void) {
    for (int c = 11; c <= 20; c++) {
        printk(KERN_INFO "%d! = %ld\n", c, factorial(c));
    }
}

module_init(lkm_example_init);
module_exit(lkm_example_exit);
