import binascii
from capstone import Cs, CS_ARCH_X86, CS_MODE_64

def hexdump(shellcode, length=16):
	"""
	Generate hexdump-style representation of shellcode
	"""
	return "\n".join(
		[f"{i:04x}  {binascii.hexlify(data).decode('utf-8')}  {repr(data)[2:-1]}" 
		 for i, data in enumerate([shellcode[i:i+length] 
		 for i in range(0, len(shellcode), length)])
		 
def disassemble(shellcode, arch=CS_ARCH_X86, mode=CS_MODE_64):
	"""
	Disassemble shellcode using Capstone
	"""
	md = Cs(arch, mode)
	disasm = []
	for i in md.disasm(shellcode, 0x1000):
		disasm.append(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
	return "\n".join(disasm)