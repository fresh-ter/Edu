#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("MIT");
MODULE_AUTHOR("Student");
MODULE_DESCRIPTION("A simple example Linux module.");
MODULE_VERSION("1.0");

static char *whom = "world";
static int howmany = 1;
static bool onlyint = false;
static bool arr[6] = {1,1,1,1,1,0};
static int arr_argc = 0;

module_param(howmany, int, S_IRUGO);
module_param(whom, charp, S_IRUGO);
module_param(onlyint, bool, S_IRUGO);
module_param_array(arr, bool, &arr_argc, S_IRUGO);

static int __init lkm_example_init(void) {
    printk(KERN_INFO "Hello world!\n");

    if(onlyint) {
        printk(KERN_INFO "%d\n", howmany);
        printk(KERN_INFO "%d\n", arr_argc);
    } else {
        for(int c = 0; c < howmany; c++) {
            printk(KERN_INFO "%s\n", whom);
        }

        if(arr[5] == false) {
            printk(KERN_INFO "");
            for (int i = 0; i < 6; ++i) {
                printk(KERN_CONT "%s ", arr[i] ? "true" : "false");
            }
            printk(KERN_CONT "\n");
        }
    }

    return 0;
}

static void __exit lkm_example_exit(void) {
    printk(KERN_INFO "Goodbye, World!\n");
}

module_init(lkm_example_init);
module_exit(lkm_example_exit);
