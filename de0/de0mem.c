//**********************************************************
// Basic memory access.
//**********************************************************

// #include "fcntl.h"			// open
// #include "unistd.h"			// close
// #include "sys/mman.h"		// mmap
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdio.h>
#include "py/runtime.h"		// micropython api

// #include "hwlib.h"
// #include "socal/hps.h"		// hps memory offset
// #include "socal/socal.h"	// altera memory access macros

// #define DE0MEM_SPAN 0x1F0000	// Copied from fft.c

// ===============================
// mmap(pa: int, nbytes: int): int
// ===============================
// map physical address [pa, pa + nbytes), return virtual address base
// 
STATIC mp_obj_t mod_de0mem_mmap(mp_obj_t pa_in, mp_obj_t nbytes_in) {
	mp_int_t pa;
	mp_int_t nbytes;
	int fd;
	mp_int_t va;
	
	if (MP_OBJ_IS_INT(pa_in)) {
		pa = mp_obj_get_int(pa_in);
	} else {
		// printf("pa is not int");
		return mp_obj_new_int(-1);
	}
	
	if (MP_OBJ_IS_INT(nbytes_in)) {
		nbytes = mp_obj_get_int(nbytes_in);
	} else {
		// printf("nbytes is not int");
		return mp_obj_new_int(-2);
	}
	
	// Open the memory as a file
	if ((fd = open("/dev/mem", O_RDWR | O_SYNC)) < 0) {
		// printf("Cannot open file");
		return mp_obj_new_int(-3);
	}
	
	// Call mmap
	if ((va = (mp_int_t)mmap(NULL, nbytes, PROT_READ | PROT_WRITE, MAP_SHARED, fd, pa)) == -1) {
		// printf("Cannot mmap");
		return mp_obj_new_int(-4);
	}
	
	if (close(fd) < 0) {
		// printf("Cannot close");
		return mp_obj_new_int(-5);
	}
	
	return mp_obj_new_int(va);
}

STATIC MP_DEFINE_CONST_FUN_OBJ_2(mod_de0mem_mmap_obj, mod_de0mem_mmap);

//
// memory base address.
//
// static void *virtual_base;
// static int mem;

//
// Initialize the memory, map:
// [ALT_LWFPGASLVS_LB_ADDR, ALT_LWFPGASLVS_UB_ADDR)
// [base, ...)
//
// Returns 0 on success, < 0 on error.
// Looks like there is no __init__ for mp modules.
//
// STATIC mp_int_t mod_de0mem_init(void) {

	// Open the memory as a file.
	// if ((mem = open("/dev/mem", (O_RDWR | O_SYNC))) == -1) {
	// 	return -1;
	// }

	// // Map.
	// virtual_base = mmap(NULL, DE0MEM_SPAN, PROT_READ | PROT_WRITE, MAP_SHARED, mem, ALT_LWFPGASLVS_OFST);
	// if (virtual_base == (void *)-1) {
	// 	return -1;
	// }

	// return 0;
// }

// STATIC MP_DEFINE_CONST_FUN_OBJ_0(mod_de0mem_init_obj, mod_de0mem_init);

//
// Unmap and close file.
//
// Returns 0 on success, -1 on error.
// 
// STATIC mp_int_t mod_de0mem_close(void) {

// 	if (munmap(virtual_base, DE0MEM_SPAN) != 0) {
// 		close(mem);
// 		return -1;
// 	}

// 	close(mem);
// 	return 0;
// }

// STATIC MP_DEFINE_CONST_FUN_OBJ_0(mod_de0mem_close_obj, mod_de0mem_close);

//
// Get the virtual_base.
//
// STATIC mp_obj_t mod_de0mem_get_base(void) {
// 	return mp_obj_new_int_from_ull((unsigned long long)virtual_base);
// }

// STATIC MP_DEFINE_CONST_FUN_OBJ_0(mod_de0mem_get_base_obj, mod_de0mem_get_base);

//
// Write a word to memory.
//
// Return 0 on success, -1 if the address is illegal.
//
// STATIC mp_int_t mod_de0mem_write_word(void *dst, int src) {
// 	if ((unsigned long)dst < (unsigned long)virtual_base ||
// 		(unsigned long)dst >= (unsigned long)virtual_base + DE0MEM_SPAN) {
// 		return -1;
// 	}

// 	alt_write_word(dst, src);
// 	return 0;
// }

// STATIC MP_DEFINE_CONST_FUN_OBJ_2(mod_de0mem_write_word_obj, mod_de0mem_write_word);

STATIC const mp_map_elem_t mp_module_de0mem_globals_table[] = {
	{ MP_OBJ_NEW_QSTR(MP_QSTR___name__), MP_OBJ_NEW_QSTR(MP_QSTR_de0mem) },

#define FUN(name) { MP_OBJ_NEW_QSTR(MP_QSTR_ ## name), (mp_obj_t)&mod_de0mem_ ## name ## _obj }
	FUN(mmap)
	// FUN(init),
	// FUN(close),
	// FUN(get_base),
	// FUN(write_word),
#undef FUN

};

STATIC MP_DEFINE_CONST_DICT(mp_module_de0mem_globals, mp_module_de0mem_globals_table);

const mp_obj_module_t mp_module_de0mem = {
	.base = { &mp_type_module },
	.name = MP_QSTR_de0mem,
	.globals = (mp_obj_dict_t *)&mp_module_de0mem_globals,
};