/* cpp_learning.h
 * autor: hanjiangtao
 * all rights resverd
*/

#ifdef CPP_LEARNING
#define MAIN main
#else
#define MAIN test_main
#endif

int MAIN(int argc, char* argv[]);