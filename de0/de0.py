import de0mem

# (pa_begin, pa_end, va_begin)
ranges = [
	(0, 0x10, -1),
	(0x10, 0x20, -1),
	(0x20, 0x30, -1),
]
#  *  0x00000000 - 0xfbffffff | Undefined       
#  *  0xfc000000 - 0xfc000003 | ALT_STM         
#  *  0xfc000004 - 0xfeffffff | Undefined       
#  *  0xff000000 - 0xff000003 | ALT_DAP         
#  *  0xff000004 - 0xff1fffff | Undefined       
#  *  0xff200000 - 0xff3fffff | ALT_LWFPGASLVS  
#  *  0xff400000 - 0xff47ffff | ALT_LWH2F       
#  *  0xff480000 - 0xff4fffff | Undefined       
#  *  0xff500000 - 0xff507fff | ALT_H2F         
#  *  0xff508000 - 0xff5fffff | Undefined       
#  *  0xff600000 - 0xff67ffff | ALT_F2H         
#  *  0xff680000 - 0xff6fffff | Undefined       
#  *  0xff700000 - 0xff701fff | ALT_EMAC0       
#  *  0xff702000 - 0xff703fff | ALT_EMAC1       
#  *  0xff704000 - 0xff7043ff | ALT_SDMMC       
#  *  0xff704400 - 0xff704fff | Undefined       
#  *  0xff705000 - 0xff7050ff | ALT_QSPI        
#  *  0xff705100 - 0xff705fff | Undefined       
#  *  0xff706000 - 0xff706fff | ALT_FPGAMGR     
#  *  0xff707000 - 0xff707fff | ALT_ACPIDMAP    
#  *  0xff708000 - 0xff70807f | ALT_GPIO0       
#  *  0xff708080 - 0xff708fff | Undefined       
#  *  0xff709000 - 0xff70907f | ALT_GPIO1       
#  *  0xff709080 - 0xff709fff | Undefined       
#  *  0xff70a000 - 0xff70a07f | ALT_GPIO2       
#  *  0xff70a080 - 0xff7fffff | Undefined       
#  *  0xff800000 - 0xff87ffff | ALT_L3          
#  *  0xff880000 - 0xff8fffff | Undefined       
#  *  0xff900000 - 0xff9fffff | ALT_NANDDATA    
#  *  0xffa00000 - 0xffafffff | ALT_QSPIDATA    
#  *  0xffb00000 - 0xffb3ffff | ALT_USB0        
#  *  0xffb40000 - 0xffb7ffff | ALT_USB1        
#  *  0xffb80000 - 0xffb807ff | ALT_NAND        
#  *  0xffb80800 - 0xffb8ffff | Undefined       
#  *  0xffb90000 - 0xffb90003 | ALT_FPGAMGRDATA 
#  *  0xffb90004 - 0xffbfffff | Undefined       
#  *  0xffc00000 - 0xffc001ff | ALT_CAN0        
#  *  0xffc00200 - 0xffc00fff | Undefined       
#  *  0xffc01000 - 0xffc011ff | ALT_CAN1        
#  *  0xffc01200 - 0xffc01fff | Undefined       
#  *  0xffc02000 - 0xffc020ff | ALT_UART0       
#  *  0xffc02100 - 0xffc02fff | Undefined       
#  *  0xffc03000 - 0xffc030ff | ALT_UART1       
#  *  0xffc03100 - 0xffc03fff | Undefined       
#  *  0xffc04000 - 0xffc040ff | ALT_I2C0        
#  *  0xffc04100 - 0xffc04fff | Undefined       
#  *  0xffc05000 - 0xffc050ff | ALT_I2C1        
#  *  0xffc05100 - 0xffc05fff | Undefined       
#  *  0xffc06000 - 0xffc060ff | ALT_I2C2        
#  *  0xffc06100 - 0xffc06fff | Undefined       
#  *  0xffc07000 - 0xffc070ff | ALT_I2C3        
#  *  0xffc07100 - 0xffc07fff | Undefined       
#  *  0xffc08000 - 0xffc080ff | ALT_SPTMR0      
#  *  0xffc08100 - 0xffc08fff | Undefined       
#  *  0xffc09000 - 0xffc090ff | ALT_SPTMR1      
#  *  0xffc09100 - 0xffc1ffff | Undefined       
#  *  0xffc20000 - 0xffc3ffff | ALT_SDR         
#  *  0xffc40000 - 0xffcfffff | Undefined       
#  *  0xffd00000 - 0xffd000ff | ALT_OSC1TMR0    
#  *  0xffd00100 - 0xffd00fff | Undefined       
#  *  0xffd01000 - 0xffd010ff | ALT_OSC1TMR1    
#  *  0xffd01100 - 0xffd01fff | Undefined       
#  *  0xffd02000 - 0xffd020ff | ALT_L4WD0       
#  *  0xffd02100 - 0xffd02fff | Undefined       
#  *  0xffd03000 - 0xffd030ff | ALT_L4WD1       
#  *  0xffd03100 - 0xffd03fff | Undefined       
#  *  0xffd04000 - 0xffd041ff | ALT_CLKMGR      
#  *  0xffd04200 - 0xffd04fff | Undefined       
#  *  0xffd05000 - 0xffd050ff | ALT_RSTMGR      
#  *  0xffd05100 - 0xffd07fff | Undefined       
#  *  0xffd08000 - 0xffd0bfff | ALT_SYSMGR      
#  *  0xffd0c000 - 0xffdfffff | Undefined       
#  *  0xffe00000 - 0xffe00003 | ALT_DMANONSECURE
#  *  0xffe00004 - 0xffe00fff | Undefined       
#  *  0xffe01000 - 0xffe01003 | ALT_DMASECURE   
#  *  0xffe01004 - 0xffe01fff | Undefined       
#  *  0xffe02000 - 0xffe0207f | ALT_SPIS0       
#  *  0xffe02080 - 0xffe02fff | Undefined       
#  *  0xffe03000 - 0xffe0307f | ALT_SPIS1       
#  *  0xffe03080 - 0xffefffff | Undefined       
#  *  0xfff00000 - 0xfff000ff | ALT_SPIM0       
#  *  0xfff00100 - 0xfff00fff | Undefined       
#  *  0xfff01000 - 0xfff010ff | ALT_SPIM1       
#  *  0xfff01100 - 0xfff01fff | Undefined       
#  *  0xfff02000 - 0xfff0201f | ALT_SCANMGR     
#  *  0xfff02020 - 0xfffcffff | Undefined       
#  *  0xfffd0000 - 0xfffdffff | ALT_ROM         
#  *  0xfffe0000 - 0xfffebfff | Undefined       
#  *  0xfffec000 - 0xfffec003 | ALT_MPUSCU      
#  *  0xfffec004 - 0xfffeefff | Undefined       
#  *  0xfffef000 - 0xfffef003 | ALT_MPUL2       
#  *  0xfffef004 - 0xfffeffff | Undefined       
#  *  0xffff0000 - 0xffffffff | ALT_OCRAM 

def __get_va__(pa):
	for idx in range(len(ranges)):
		(pa_begin, pa_end, va_begin) = ranges[idx]
		if pa >= pa_begin and pa < pa_end:
			print("In pa [%d, %d)" % (pa_begin, pa_end))
			offset = pa - pa_begin
			if va_begin == -1:
				va_begin = de0mem.mmap(pa_begin, pa_end - pa_begin)
				ranges[idx] = (pa_begin, pa_end, va_begin)
			return va_begin + offset
	return -1